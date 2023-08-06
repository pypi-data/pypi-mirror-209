# -*- coding: utf-8 -*-

"""
testers

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from testers.api_helper import APIHelper
import testers.exceptions.api_exception


class GlobalTestException(testers.exceptions.api_exception.APIException):
    def __init__(self, reason, response):
        """Constructor for the GlobalTestException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(GlobalTestException, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.text)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.server_message = dictionary.get("ServerMessage") if dictionary.get("ServerMessage") else None
        self.server_code = dictionary.get("ServerCode") if dictionary.get("ServerCode") else None
