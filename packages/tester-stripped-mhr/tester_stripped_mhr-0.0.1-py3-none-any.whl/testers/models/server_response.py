# -*- coding: utf-8 -*-

"""
testers

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from testers.api_helper import APIHelper


class ServerResponse(object):

    """Implementation of the 'ServerResponse' model.

    TODO: type model description here.

    Attributes:
        passed (bool): TODO: type description here.
        message (string): TODO: type description here.
        input (dict): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "passed": 'passed',
        "message": 'Message',
        "input": 'input'
    }

    _optionals = [
        'message',
        'input',
    ]

    def __init__(self,
                 passed=None,
                 message=APIHelper.SKIP,
                 input=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ServerResponse class"""

        # Initialize members of the class
        self.passed = passed 
        if message is not APIHelper.SKIP:
            self.message = message 
        if input is not APIHelper.SKIP:
            self.input = input 

        # Add additional model properties to the instance
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        passed = dictionary.get("passed") if "passed" in dictionary.keys() else None
        message = dictionary.get("Message") if dictionary.get("Message") else APIHelper.SKIP
        input = dictionary.get("input") if dictionary.get("input") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(passed,
                   message,
                   input,
                   dictionary)
