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


class EchoController(BaseController):

    """A Controller to access Endpoints in the testers API."""
    def __init__(self, config):
        super(EchoController, self).__init__(config)

    def query_echo(self,
                   _optional_query_parameters=None):
        """Does a GET request to /.

        TODO: type endpoint description here.

        Args:
            _optional_form_parameters (Array, optional): Additional optional
                query parameters are supported by this endpoint

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
            .path('/')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .additional_query_params(_optional_query_parameters)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(EchoResponse.from_dictionary)
        ).execute()

    def json_echo(self,
                  input):
        """Does a POST request to /.

        Echo's back the request

        Args:
            input (object): TODO: type description here.

        Returns:
            mixed: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/')
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                        .value(input)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('application/json; charset=utf-8'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.dynamic_deserialize)
        ).execute()

    def form_echo(self,
                  input):
        """Does a POST request to /.

        Sends the request including any form params as JSON

        Args:
            input (object): TODO: type description here.

        Returns:
            mixed: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('input')
                        .value(input)
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
            .deserializer(APIHelper.dynamic_deserialize)
        ).execute()
