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
from apimatic_core.types.datetime_format import DateTimeFormat
from apimatic_core.configurations.endpoint_configuration import EndpointConfiguration
import dateutil.parser
from testers.models.person import Person
from testers.models.response_with_enum import ResponseWithEnum


class ResponseTypesController(BaseController):

    """A Controller to access Endpoints in the testers API."""
    def __init__(self, config):
        super(ResponseTypesController, self).__init__(config)

    def get_integer(self):
        """Does a GET request to /response/integer.

        Gets a integer response

        Returns:
            int: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/integer')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def get_binary(self):
        """Does a GET request to /response/binary.

        gets a binary object

        Returns:
            binary: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/binary')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
        ).endpoint_configuration(
            EndpointConfiguration()
            .has_binary_response(True)
        ).execute()

    def get_precision(self):
        """Does a GET request to /response/precision.

        TODO: type endpoint description here.

        Returns:
            float: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/precision')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def get_model_array(self):
        """Does a GET request to /response/model.

        TODO: type endpoint description here.

        Returns:
            list of Person: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/model')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Person.from_dictionary)
        ).execute()

    def get_model(self):
        """Does a GET request to /response/model.

        TODO: type endpoint description here.

        Returns:
            Person: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/model')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Person.from_dictionary)
        ).execute()

    def get_long(self):
        """Does a GET request to /response/long.

        TODO: type endpoint description here.

        Returns:
            long|int: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/long')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def get_date_array(self):
        """Does a GET request to /response/date.

        TODO: type endpoint description here.

        Returns:
            list of date: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/date')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.date_deserialize)
        ).execute()

    def get_date(self):
        """Does a GET request to /response/date.

        TODO: type endpoint description here.

        Returns:
            date: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/date')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.date_deserialize)
        ).execute()

    def get_content_type_headers(self):
        """Does a GET request to /response/getContentType.

        TODO: type endpoint description here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/getContentType')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
        ).execute()

    def get_unix_date_time(self):
        """Does a GET request to /response/unixdatetime.

        TODO: type endpoint description here.

        Returns:
            datetime: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/unixdatetime')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.datetime_deserialize)
            .datetime_format(DateTimeFormat.UNIX_DATE_TIME)
        ).execute()

    def get_1123_date_time(self):
        """Does a GET request to /response/1123datetime.

        TODO: type endpoint description here.

        Returns:
            datetime: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/1123datetime')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.datetime_deserialize)
            .datetime_format(DateTimeFormat.HTTP_DATE_TIME)
        ).execute()

    def get_headers(self):
        """Does a GET request to /response/headers.

        TODO: type endpoint description here.

        Returns:
            void: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/headers')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
        ).execute()

    def get_boolean(self):
        """Does a GET request to /response/boolean.

        TODO: type endpoint description here.

        Returns:
            bool: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/boolean')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def get_3339_datetime(self):
        """Does a GET request to /response/3339datetime.

        TODO: type endpoint description here.

        Returns:
            datetime: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/3339datetime')
            .http_method(HttpMethodEnum.GET)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.datetime_deserialize)
            .datetime_format(DateTimeFormat.RFC3339_DATE_TIME)
        ).execute()

    def get_dynamic(self):
        """Does a GET request to /response/dynamic.

        TODO: type endpoint description here.

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
            .path('/response/dynamic')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.dynamic_deserialize)
        ).execute()

    def return_response_with_enums(self):
        """Does a GET request to /response/responseWitEnum.

        TODO: type endpoint description here.

        Returns:
            ResponseWithEnum: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/responseWitEnum')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ResponseWithEnum.from_dictionary)
        ).execute()

    def get_string_enum_array(self):
        """Does a GET request to /response/enum.

        TODO: type endpoint description here.

        Returns:
            list of Days: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/enum')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .query_param(Parameter()
                         .key('type')
                         .value('string'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def get_string_enum(self):
        """Does a GET request to /response/enum.

        TODO: type endpoint description here.

        Returns:
            Days: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/enum')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('type')
                         .value('string'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def get_int_enum(self):
        """Does a GET request to /response/enum.

        TODO: type endpoint description here.

        Returns:
            SuiteCode: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/enum')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('type')
                         .value('int'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def get_int_enum_array(self):
        """Does a GET request to /response/enum.

        TODO: type endpoint description here.

        Returns:
            list of SuiteCode: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/enum')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .query_param(Parameter()
                         .key('type')
                         .value('int'))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def get_integer_array(self):
        """Does a GET request to /response/integer.

        Get an array of integers.

        Returns:
            list of int: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/integer')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def get_dynamic_array(self):
        """Does a GET request to /response/dynamic.

        TODO: type endpoint description here.

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
            .path('/response/dynamic')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.dynamic_deserialize)
        ).execute()

    def get_3339_datetime_array(self):
        """Does a GET request to /response/3339datetime.

        TODO: type endpoint description here.

        Returns:
            list of datetime: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/3339datetime')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.datetime_deserialize)
            .datetime_format(DateTimeFormat.RFC3339_DATE_TIME)
        ).execute()

    def get_boolean_array(self):
        """Does a GET request to /response/boolean.

        TODO: type endpoint description here.

        Returns:
            list of bool: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/boolean')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def get_1123_date_time_array(self):
        """Does a GET request to /response/1123datetime.

        TODO: type endpoint description here.

        Returns:
            list of datetime: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/1123datetime')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.datetime_deserialize)
            .datetime_format(DateTimeFormat.HTTP_DATE_TIME)
        ).execute()

    def get_unix_date_time_array(self):
        """Does a GET request to /response/unixdatetime.

        TODO: type endpoint description here.

        Returns:
            list of datetime: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/unixdatetime')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.datetime_deserialize)
            .datetime_format(DateTimeFormat.UNIX_DATE_TIME)
        ).execute()
