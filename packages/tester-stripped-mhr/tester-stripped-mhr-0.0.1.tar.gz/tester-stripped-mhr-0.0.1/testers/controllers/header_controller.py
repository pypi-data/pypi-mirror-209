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
from testers.models.server_response import ServerResponse


class HeaderController(BaseController):

    """A Controller to access Endpoints in the testers API."""
    def __init__(self, config):
        super(HeaderController, self).__init__(config)

    def send_headers(self,
                     custom_header,
                     value):
        """Does a POST request to /header.

        Sends a single header params

        Args:
            custom_header (string): TODO: type description here.
            value (string): Represents the value of the custom header

        Returns:
            ServerResponse: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/header')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('custom-header')
                          .value(custom_header)
                          .is_required(True))
            .form_param(Parameter()
                        .key('value')
                        .value(value)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/x-www-form-urlencoded'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()
