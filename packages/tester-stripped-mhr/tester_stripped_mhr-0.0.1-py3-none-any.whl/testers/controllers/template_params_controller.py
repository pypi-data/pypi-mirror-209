# -*- coding: utf-8 -*-

"""
testers

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from testers.api_helper import APIHelper
from testers.configuration import Server
from testers.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from testers.http.http_method_enum import HttpMethodEnum
from testers.models.echo_response import EchoResponse


class TemplateParamsController(BaseController):

    """A Controller to access Endpoints in the testers API."""
    def __init__(self, config):
        super(TemplateParamsController, self).__init__(config)

    def send_string_array(self,
                          strings):
        """Does a GET request to /{strings}.

        TODO: type endpoint description here.

        Args:
            strings (list of string): TODO: type description here.

        Returns:
            EchoResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/{strings}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('strings')
                            .value(strings)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(EchoResponse.from_dictionary)
        ).execute()

    def send_integer_array(self,
                           integers):
        """Does a GET request to /{integers}.

        TODO: type endpoint description here.

        Args:
            integers (list of int): TODO: type description here.

        Returns:
            EchoResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/{integers}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('integers')
                            .value(integers)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(EchoResponse.from_dictionary)
        ).execute()
