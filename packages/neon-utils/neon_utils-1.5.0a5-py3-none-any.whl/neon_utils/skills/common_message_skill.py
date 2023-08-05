# NEON AI (TM) SOFTWARE, Software Development Kit & Application Framework
# All trademark and other rights reserved by their respective owners
# Copyright 2008-2022 Neongecko.com Inc.
# Contributors: Daniel McKnight, Guy Daniels, Elon Gasper, Richard Leeds,
# Regina Bloomstine, Casimiro Ferreira, Andrii Pernatii, Kirill Hrymailo
# BSD-3 License
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from this
#    software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS;  OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE,  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from abc import ABC, abstractmethod
from enum import IntEnum

from neon_utils.skills.neon_skill import NeonSkill
from neon_utils.logger import LOG


class CMSMatchLevel(IntEnum):
    EXACT = 1  # Skill was requested specifically
    MEDIA = 2  # Skill can handle the requested type of message (text, email, call, etc)
    LOOSE = 3  # Skill can handle a generic message request


class CommonMessageSkill(NeonSkill, ABC):
    """
    Skills that handle calls or messaging should be based on this class.
    Skills must implement 'CMS_match_query_phrase'
    This skill works with Communcation skill which handles intent matching and skill selection
    """
    def __init__(self, name=None, bus=None, **kwargs):
        super().__init__(name, bus, **kwargs)

    def bind(self, bus):
        if bus:
            super().bind(bus)
            self.add_event("communication:request.message", self.__handle_send_message_request)
            self.add_event("communication:send.message", self.__handle_send_message)

            self.add_event("communication:request.call", self.__handle_place_call_request)
            self.add_event("communication:place.call", self.__handle_place_call)

    def __handle_place_call_request(self, message):
        """
        Handler for a send message request. This is the entry point for this skill to handle a request.
        :param message: message generated by Communcation skill
        """
        request_string = message.data["request"]

        # notify Communcation skill that this skill is working on it
        self.bus.emit(message.response({"request": request_string,
                                        "skill_id": self.skill_id,
                                        "searching": True}))

        # Calculate match for this skill and respond
        result: dict = self.CMS_match_call_phrase(request_string, message.context)
        if result:
            confidence = self.__calc_confidence(result, result.pop("conf"), message.context)
            LOG.debug(f"DM: Response from {self.skill_id} ({message.msg_type})")
            self.bus.emit(message.response({"request": request_string,
                                            "skill_id": self.skill_id,
                                            "conf": confidence,
                                            "skill_data": result}))
        else:
            # Notify not handling request
            self.bus.emit(message.response({"request": request_string,
                                            "skill_id": self.skill_id,
                                            "searching": False}))

    def __handle_send_message_request(self, message):
        """
        Handler for a send message request. This is the entry point for this skill to handle a request.
        :param message: message generated by Communcation skill
        """

        request_string = message.data["request"]

        # notify Communcation skill that this skill is working on it
        self.bus.emit(message.response({"request": request_string,
                                        "skill_id": self.skill_id,
                                        "searching": True}))

        # Calculate match for this skill and respond
        result: dict = self.CMS_match_message_phrase(request_string, message.context)
        if result:
            confidence = self.__calc_confidence(result, result.pop("conf"), message.context)
            LOG.debug(f"DM: Response from {self.skill_id} ({message.msg_type})")
            self.bus.emit(message.response({"request": request_string,
                                            "skill_id": self.skill_id,
                                            "conf": confidence,
                                            "skill_data": result}))
        else:
            # Notify not handling request
            self.bus.emit(message.response({"request": request_string,
                                            "skill_id": self.skill_id,
                                            "searching": False}))

    def __handle_place_call(self, message):
        """
        Callback method that handles when this skill has been selected to respond
        :param message: message object associated with request
        :return:
        """
        if message.data["skill_id"] != self.skill_id:
            # Not for this skill!
            return
        else:
            self.CMS_handle_place_call(message)

    def __handle_send_message(self, message):
        """
        Callback method that handles when this skill has been selected to respond
        :param message: message object associated with request
        :return:
        """
        if message.data["skill_id"] != self.skill_id:
            # Not for this skill!
            return
        else:
            self.CMS_handle_send_message(message)

    @staticmethod
    def __calc_confidence(result_data, level, context):
        """
        Translates a confidence level to a 0-1 value
        :param result_data (dict): data returned by skill
        :param level (CMSMatchLevel): match level
        :param context (dict): message context
        :return (float): confidence level
        """

        # Add 0.1 for each matched element (message, recipeint, subject, etc)
        bonus = (len(result_data.keys()) - 1) * 0.1

        # Lower confidence for sms requests that can't be handled
        if result_data.get("kind") == "sms" and not context.get("mobile"):
            bonus = -0.2
        # Modify confidences for phone call if mobile can handle request
        elif result_data.get("kind") == "call":
            if context.get("mobile"):
                bonus = 0.2
            else:
                bonus = -0.2

        if level == CMSMatchLevel.EXACT:
            return 1.0
        elif level == CMSMatchLevel.MEDIA:
            return 0.6 + bonus
        elif level == CMSMatchLevel.LOOSE:
            return 0.3 + bonus
        else:
            return 0.0

    @abstractmethod
    def CMS_match_message_phrase(self, request, context):
        """
        Checks if this skill can handle the given message request
        :param request: (str) user literal request to handle
        :param context: (dict) message context
        :return: (dict) confidence, data to be used in the callback if skill is selected
        """
        return {}

    @abstractmethod
    def CMS_handle_send_message(self, message):
        """
        Handles when this skill has been selected to respond
        :param message: message associated with this skills match submission
        """
        pass

    @abstractmethod
    def CMS_match_call_phrase(self, contact, context):
        """
        Checks if this skill can handle the given call request
        :param contact: (str) requested contact (name or address)
        :param context: (dict) message context
        :return: (dict) confidence, data to be used in the callback if skill is selected
        """
        return {}

    @abstractmethod
    def CMS_handle_place_call(self, message):
        """
        Handles when this skill has been selected to respond
        :param message: message associated with this skills match submission
        """
        pass

    @staticmethod
    def _extract_message_content(text):
        """
        Generic method that attempts to extract the message content from a request to send a message
        :param text: Input string to evaluate
        :return: recipient_to_append(prefix), message
        """

        if "that says " in text:
            recipient_to_append, message = text.split("that says ", 1)
        elif "saying " in text:
            recipient_to_append, message = text.split("saying ", 1)
        elif len(text) <= 1:
            message = None
            recipient_to_append = text
        else:
            recipient_to_append = None
            message = text
        return recipient_to_append, message
