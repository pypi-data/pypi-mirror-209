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


class BodyParamsController(BaseController):

    """A Controller to access Endpoints in the testers API."""
    def __init__(self, config):
        super(BodyParamsController, self).__init__(config)

    def send_model(self,
                   model):
        """Does a POST request to /body/model.

        TODO: type endpoint description here.

        Args:
            model (Employee): TODO: type description here.

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
            .path('/body/model')
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                        .value(model)
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_date(self,
                  date):
        """Does a POST request to /body/date.

        TODO: type endpoint description here.

        Args:
            date (date): TODO: type description here.

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
            .path('/body/date')
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                        .value(date)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('text/plain; charset=utf-8'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(str)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def update_model(self,
                     model):
        """Does a PUT request to /body/updateModel.

        TODO: type endpoint description here.

        Args:
            model (Employee): TODO: type description here.

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
            .path('/body/updateModel')
            .http_method(HttpMethodEnum.PUT)
            .body_param(Parameter()
                        .value(model)
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_delete_plain_text(self,
                               text_string):
        """Does a DELETE request to /body/deletePlainTextBody.

        TODO: type endpoint description here.

        Args:
            text_string (string): TODO: type description here.

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
            .path('/body/deletePlainTextBody')
            .http_method(HttpMethodEnum.DELETE)
            .body_param(Parameter()
                        .value(text_string)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('text/plain; charset=utf-8'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_delete_body(self,
                         body):
        """Does a DELETE request to /body/deleteBody.

        TODO: type endpoint description here.

        Args:
            body (DeleteBody): TODO: type description here.

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
            .path('/body/deleteBody')
            .http_method(HttpMethodEnum.DELETE)
            .body_param(Parameter()
                        .value(body)
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_date_array(self,
                        dates):
        """Does a POST request to /body/date.

        TODO: type endpoint description here.

        Args:
            dates (list of date): TODO: type description here.

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
            .path('/body/date')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .body_param(Parameter()
                        .value(dates)
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_unix_date_time(self,
                            datetime):
        """Does a POST request to /body/unixdatetime.

        TODO: type endpoint description here.

        Args:
            datetime (datetime): TODO: type description here.

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
            .path('/body/unixdatetime')
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                        .value(APIHelper.when_defined(APIHelper.UnixDateTime, datetime))
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('text/plain; charset=utf-8'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(str)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_rfc_1123_date_time(self,
                                datetime):
        """Does a POST request to /body/rfc1123datetime.

        TODO: type endpoint description here.

        Args:
            datetime (datetime): TODO: type description here.

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
            .path('/body/rfc1123datetime')
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                        .value(APIHelper.when_defined(APIHelper.HttpDateTime, datetime))
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('text/plain; charset=utf-8'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(str)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_rfc_3339_date_time(self,
                                datetime):
        """Does a POST request to /body/rfc3339datetime.

        TODO: type endpoint description here.

        Args:
            datetime (datetime): TODO: type description here.

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
            .path('/body/rfc3339datetime')
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                        .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, datetime))
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('text/plain; charset=utf-8'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(str)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_unix_date_time_array(self,
                                  datetimes):
        """Does a POST request to /body/unixdatetime.

        TODO: type endpoint description here.

        Args:
            datetimes (list of datetime): TODO: type description here.

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
            .path('/body/unixdatetime')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .body_param(Parameter()
                        .value([APIHelper.when_defined(APIHelper.UnixDateTime, element) for element in datetimes])
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_rfc_1123_date_time_array(self,
                                      datetimes):
        """Does a POST request to /body/rfc1123datetime.

        TODO: type endpoint description here.

        Args:
            datetimes (list of datetime): TODO: type description here.

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
            .path('/body/rfc1123datetime')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .body_param(Parameter()
                        .value([APIHelper.when_defined(APIHelper.HttpDateTime, element) for element in datetimes])
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_rfc_3339_date_time_array(self,
                                      datetimes):
        """Does a POST request to /body/rfc3339datetime.

        TODO: type endpoint description here.

        Args:
            datetimes (list of datetime): TODO: type description here.

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
            .path('/body/rfc3339datetime')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .body_param(Parameter()
                        .value([APIHelper.when_defined(APIHelper.RFC3339DateTime, element) for element in datetimes])
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_string_array(self,
                          sarray):
        """Does a POST request to /body/string.

        sends a string body param

        Args:
            sarray (list of string): TODO: type description here.

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
            .path('/body/string')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .body_param(Parameter()
                        .value(sarray)
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def update_string(self,
                      value):
        """Does a PUT request to /body/updateString.

        TODO: type endpoint description here.

        Args:
            value (string): TODO: type description here.

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
            .path('/body/updateString')
            .http_method(HttpMethodEnum.PUT)
            .body_param(Parameter()
                        .value(value)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('text/plain; charset=utf-8'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_integer_array(self,
                           integers):
        """Does a POST request to /body/number.

        TODO: type endpoint description here.

        Args:
            integers (list of int): TODO: type description here.

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
            .path('/body/number')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .body_param(Parameter()
                        .value(integers)
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_model_array(self,
                         models):
        """Does a POST request to /body/model.

        TODO: type endpoint description here.

        Args:
            models (list of Employee): TODO: type description here.

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
            .path('/body/model')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .body_param(Parameter()
                        .value(models)
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_dynamic(self,
                     dynamic):
        """Does a POST request to /body/dynamic.

        TODO: type endpoint description here.

        Args:
            dynamic (object): TODO: type description here.

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
            .path('/body/dynamic')
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                        .value(dynamic)
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_string(self,
                    value):
        """Does a POST request to /body/string.

        TODO: type endpoint description here.

        Args:
            value (string): TODO: type description here.

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
            .path('/body/string')
            .http_method(HttpMethodEnum.POST)
            .body_param(Parameter()
                        .value(value)
                        .is_required(True))
            .header_param(Parameter()
                          .key('content-type')
                          .value('text/plain; charset=utf-8'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_string_enum_array(self,
                               days):
        """Does a POST request to /body/stringenum.

        TODO: type endpoint description here.

        Args:
            days (list of Days): TODO: type description here.

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
            .path('/body/stringenum')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .body_param(Parameter()
                        .value(days)
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_integer_enum_array(self,
                                suites):
        """Does a POST request to /body/integerenum.

        TODO: type endpoint description here.

        Args:
            suites (list of SuiteCode): TODO: type description here.

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
            .path('/body/integerenum')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .body_param(Parameter()
                        .value(suites)
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def send_delete_body_with_model(self,
                                    model):
        """Does a DELETE request to /body/deleteBody1.

        TODO: type endpoint description here.

        Args:
            model (Employee): TODO: type description here.

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
            .path('/body/deleteBody1')
            .http_method(HttpMethodEnum.DELETE)
            .body_param(Parameter()
                        .value(model)
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def update_model_array(self,
                           models):
        """Does a PUT request to /body/updateModel.

        TODO: type endpoint description here.

        Args:
            models (list of Employee): TODO: type description here.

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
            .path('/body/updateModel')
            .http_method(HttpMethodEnum.PUT)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .body_param(Parameter()
                        .value(models)
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def update_string_array(self,
                            strings):
        """Does a PUT request to /body/updateString.

        TODO: type endpoint description here.

        Args:
            strings (list of string): TODO: type description here.

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
            .path('/body/updateString')
            .http_method(HttpMethodEnum.PUT)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .body_param(Parameter()
                        .value(strings)
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
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()
