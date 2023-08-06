# -*- coding: utf-8 -*-

"""
testers

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from testers.api_helper import APIHelper
from testers.models.query_parameter import QueryParameter


class EchoResponse(object):

    """Implementation of the 'EchoResponse' model.

    Raw http Request info

    Attributes:
        body (dict): TODO: type description here.
        headers (dict): TODO: type description here.
        method (string): TODO: type description here.
        path (string): relativePath
        query (dict): TODO: type description here.
        upload_count (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "body": 'body',
        "headers": 'headers',
        "method": 'method',
        "path": 'path',
        "query": 'query',
        "upload_count": 'uploadCount'
    }

    _optionals = [
        'body',
        'headers',
        'method',
        'path',
        'query',
        'upload_count',
    ]

    def __init__(self,
                 body=APIHelper.SKIP,
                 headers=APIHelper.SKIP,
                 method=APIHelper.SKIP,
                 path=APIHelper.SKIP,
                 query=APIHelper.SKIP,
                 upload_count=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the EchoResponse class"""

        # Initialize members of the class
        if body is not APIHelper.SKIP:
            self.body = body 
        if headers is not APIHelper.SKIP:
            self.headers = headers 
        if method is not APIHelper.SKIP:
            self.method = method 
        if path is not APIHelper.SKIP:
            self.path = path 
        if query is not APIHelper.SKIP:
            self.query = query 
        if upload_count is not APIHelper.SKIP:
            self.upload_count = upload_count 

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

        body = dictionary.get("body") if dictionary.get("body") else APIHelper.SKIP
        headers = dictionary.get("headers") if dictionary.get("headers") else APIHelper.SKIP
        method = dictionary.get("method") if dictionary.get("method") else APIHelper.SKIP
        path = dictionary.get("path") if dictionary.get("path") else APIHelper.SKIP
        query = QueryParameter.from_dictionary(dictionary.get('query')) if 'query' in dictionary.keys() else APIHelper.SKIP
        upload_count = dictionary.get("uploadCount") if dictionary.get("uploadCount") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(body,
                   headers,
                   method,
                   path,
                   query,
                   upload_count,
                   dictionary)
