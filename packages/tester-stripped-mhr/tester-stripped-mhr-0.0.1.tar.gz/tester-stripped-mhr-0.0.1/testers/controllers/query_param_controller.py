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


class QueryParamController(BaseController):

    """A Controller to access Endpoints in the testers API."""
    def __init__(self, config):
        super(QueryParamController, self).__init__(config)

    def date(self,
             date):
        """Does a GET request to /query/date.

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
            .path('/query/date')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('date')
                         .value(date)
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def date_array(self,
                   dates):
        """Does a GET request to /query/datearray.

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
            .path('/query/datearray')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('dates')
                         .value(dates)
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def no_params(self):
        """Does a GET request to /query/noparams.

        TODO: type endpoint description here.

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
            .path('/query/noparams')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def optional_dynamic_query_param(self,
                                     name,
                                     _optional_query_parameters=None):
        """Does a GET request to /query/optionalQueryParam.

        get optional dynamic query parameter

        Args:
            name (string): TODO: type description here.
            _optional_form_parameters (Array, optional): Additional optional
                query parameters are supported by this endpoint

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
            .path('/query/optionalQueryParam')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('name')
                         .value(name)
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .additional_query_params(_optional_query_parameters)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def unix_date_time_array(self,
                             datetimes):
        """Does a GET request to /query/unixdatetimearray.

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
            .path('/query/unixdatetimearray')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('datetimes')
                         .value([APIHelper.when_defined(APIHelper.UnixDateTime, element) for element in datetimes])
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def unix_date_time(self,
                       datetime):
        """Does a GET request to /query/unixdatetime.

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
            .path('/query/unixdatetime')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('datetime')
                         .value(APIHelper.when_defined(APIHelper.UnixDateTime, datetime))
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def rfc_1123_date_time(self,
                           datetime):
        """Does a GET request to /query/rfc1123datetime.

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
            .path('/query/rfc1123datetime')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('datetime')
                         .value(APIHelper.when_defined(APIHelper.HttpDateTime, datetime))
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def rfc_1123_date_time_array(self,
                                 datetimes):
        """Does a GET request to /query/rfc1123datetimearray.

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
            .path('/query/rfc1123datetimearray')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('datetimes')
                         .value([APIHelper.when_defined(APIHelper.HttpDateTime, element) for element in datetimes])
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def rfc_3339_date_time_array(self,
                                 datetimes):
        """Does a GET request to /query/rfc3339datetimearray.

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
            .path('/query/rfc3339datetimearray')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('datetimes')
                         .value([APIHelper.when_defined(APIHelper.RFC3339DateTime, element) for element in datetimes])
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def rfc_3339_date_time(self,
                           datetime):
        """Does a GET request to /query/rfc3339datetime.

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
            .path('/query/rfc3339datetime')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('datetime')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, datetime))
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def string_param(self,
                     string):
        """Does a GET request to /query/stringparam.

        TODO: type endpoint description here.

        Args:
            string (string): TODO: type description here.

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
            .path('/query/stringparam')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('string')
                         .value(string)
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def url_param(self,
                  url):
        """Does a GET request to /query/urlparam.

        TODO: type endpoint description here.

        Args:
            url (string): TODO: type description here.

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
            .path('/query/urlparam')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('url')
                         .value(url)
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def number_array(self,
                     integers):
        """Does a GET request to /query/numberarray.

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
            .path('/query/numberarray')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('integers')
                         .value(integers)
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def string_array(self,
                     strings):
        """Does a GET request to /query/stringarray.

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
            .path('/query/stringarray')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('strings')
                         .value(strings)
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def simple_query(self,
                     boolean,
                     number,
                     string,
                     _optional_query_parameters=None):
        """Does a GET request to /query.

        TODO: type endpoint description here.

        Args:
            boolean (bool): TODO: type description here.
            number (int): TODO: type description here.
            string (string): TODO: type description here.
            _optional_form_parameters (Array, optional): Additional optional
                query parameters are supported by this endpoint

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
            .path('/query')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('boolean')
                         .value(boolean)
                         .is_required(True))
            .query_param(Parameter()
                         .key('number')
                         .value(number)
                         .is_required(True))
            .query_param(Parameter()
                         .key('string')
                         .value(string)
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .additional_query_params(_optional_query_parameters)
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def string_enum_array(self,
                          days):
        """Does a GET request to /query/stringenumarray.

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
            .path('/query/stringenumarray')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('days')
                         .value(days)
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def multiple_params(self,
                        number,
                        precision,
                        string,
                        url):
        """Does a GET request to /query/multipleparams.

        TODO: type endpoint description here.

        Args:
            number (int): TODO: type description here.
            precision (float): TODO: type description here.
            string (string): TODO: type description here.
            url (string): TODO: type description here.

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
            .path('/query/multipleparams')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('number')
                         .value(number)
                         .is_required(True))
            .query_param(Parameter()
                         .key('precision')
                         .value(precision)
                         .is_required(True))
            .query_param(Parameter()
                         .key('string')
                         .value(string)
                         .is_required(True))
            .query_param(Parameter()
                         .key('url')
                         .value(url)
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def integer_enum_array(self,
                           suites):
        """Does a GET request to /query/integerenumarray.

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
            .path('/query/integerenumarray')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('suites')
                         .value(suites)
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()
