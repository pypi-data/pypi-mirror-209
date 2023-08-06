# -*- coding: utf-8 -*-

"""
testers

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from testers.api_helper import APIHelper
from testers.configuration import Server
from testers.utilities.file_wrapper import FileWrapper
from testers.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from testers.http.http_method_enum import HttpMethodEnum
from testers.models.server_response import ServerResponse


class FormParamsController(BaseController):

    """A Controller to access Endpoints in the testers API."""
    def __init__(self, config):
        super(FormParamsController, self).__init__(config)

    def send_file(self,
                  file):
        """Does a POST request to /form/file.

        TODO: type endpoint description here.

        Args:
            file (typing.BinaryIO): TODO: type description here.

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
            .path('/form/file')
            .http_method(HttpMethodEnum.POST)
            .multipart_param(Parameter()
                             .key('file')
                             .value(file)
                             .default_content_type('application/octet-stream')
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

    def send_model(self,
                   model):
        """Does a POST request to /form/model.

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
            .path('/form/model')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('model')
                        .value(model)
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

    def send_date(self,
                  date):
        """Does a POST request to /form/date.

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
            .path('/form/date')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('date')
                        .value(date)
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

    def send_delete_form(self,
                         body):
        """Does a DELETE request to /form/deleteForm.

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
            .path('/form/deleteForm')
            .http_method(HttpMethodEnum.DELETE)
            .form_param(Parameter()
                        .key('body')
                        .value(body)
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

    def send_delete_multipart(self,
                              file):
        """Does a DELETE request to /form/deleteMultipart.

        TODO: type endpoint description here.

        Args:
            file (typing.BinaryIO): TODO: type description here.

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
            .path('/form/deleteMultipart')
            .http_method(HttpMethodEnum.DELETE)
            .multipart_param(Parameter()
                             .key('file')
                             .value(file)
                             .default_content_type('application/octet-stream')
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

    def send_date_array(self,
                        dates):
        """Does a POST request to /form/date.

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
            .path('/form/date')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('dates')
                        .value(dates)
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

    def send_unix_date_time(self,
                            datetime):
        """Does a POST request to /form/unixdatetime.

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
            .path('/form/unixdatetime')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('datetime')
                        .value(APIHelper.when_defined(APIHelper.UnixDateTime, datetime))
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

    def send_rfc_1123_date_time(self,
                                datetime):
        """Does a POST request to /form/rfc1123datetime.

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
            .path('/form/rfc1123datetime')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('datetime')
                        .value(APIHelper.when_defined(APIHelper.HttpDateTime, datetime))
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

    def send_rfc_3339_date_time(self,
                                datetime):
        """Does a POST request to /form/rfc3339datetime.

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
            .path('/form/rfc3339datetime')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('datetime')
                        .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, datetime))
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

    def send_unix_date_time_array(self,
                                  datetimes):
        """Does a POST request to /form/unixdatetime.

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
            .path('/form/unixdatetime')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('datetimes')
                        .value([APIHelper.when_defined(APIHelper.UnixDateTime, element) for element in datetimes])
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

    def send_rfc_1123_date_time_array(self,
                                      datetimes):
        """Does a POST request to /form/rfc1123datetime.

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
            .path('/form/rfc1123datetime')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('datetimes')
                        .value([APIHelper.when_defined(APIHelper.HttpDateTime, element) for element in datetimes])
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

    def send_long(self,
                  value):
        """Does a POST request to /form/number.

        TODO: type endpoint description here.

        Args:
            value (long|int): TODO: type description here.

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
            .path('/form/number')
            .http_method(HttpMethodEnum.POST)
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

    def send_integer_array(self,
                           integers):
        """Does a POST request to /form/number.

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
            .path('/form/number')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('integers')
                        .value(integers)
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

    def send_string_array(self,
                          strings):
        """Does a POST request to /form/string.

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
            .path('/form/string')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('strings')
                        .value(strings)
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

    def send_model_array(self,
                         models):
        """Does a POST request to /form/model.

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
            .path('/form/model')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('models')
                        .value(models)
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

    def send_string(self,
                    value):
        """Does a POST request to /form/string.

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
            .path('/form/string')
            .http_method(HttpMethodEnum.POST)
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

    def send_rfc_3339_date_time_array(self,
                                      datetimes):
        """Does a POST request to /form/rfc3339datetime.

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
            .path('/form/rfc3339datetime')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('datetimes')
                        .value([APIHelper.when_defined(APIHelper.RFC3339DateTime, element) for element in datetimes])
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

    def send_mixed_array(self,
                         options=dict()):
        """Does a POST request to /form/mixed.

        Send a variety for form params. Returns file count and body params

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    file -- typing.BinaryIO -- TODO: type description here.
                    integers -- list of int -- TODO: type description here.
                    models -- list of Employee -- TODO: type description
                        here.
                    strings -- list of string -- TODO: type description here.

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
            .path('/form/mixed')
            .http_method(HttpMethodEnum.POST)
            .multipart_param(Parameter()
                             .key('file')
                             .value(options.get('file', None))
                             .default_content_type('application/octet-stream')
                             .is_required(True))
            .form_param(Parameter()
                        .key('integers')
                        .value(options.get('integers', None))
                        .is_required(True))
            .form_param(Parameter()
                        .key('models')
                        .value(options.get('models', None))
                        .is_required(True))
            .form_param(Parameter()
                        .key('strings')
                        .value(options.get('strings', None))
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

    def update_model_with_form(self,
                               model):
        """Does a PUT request to /form/updateModel.

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
            .path('/form/updateModel')
            .http_method(HttpMethodEnum.PUT)
            .form_param(Parameter()
                        .key('model')
                        .value(model)
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

    def send_delete_form_1(self,
                           model):
        """Does a DELETE request to /form/deleteForm1.

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
            .path('/form/deleteForm1')
            .http_method(HttpMethodEnum.DELETE)
            .form_param(Parameter()
                        .key('model')
                        .value(model)
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

    def send_delete_form_with_model_array(self,
                                          models):
        """Does a DELETE request to /form/deleteForm1.

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
            .path('/form/deleteForm1')
            .http_method(HttpMethodEnum.DELETE)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('models')
                        .value(models)
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

    def update_model_array_with_form(self,
                                     models):
        """Does a PUT request to /form/updateModel.

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
            .path('/form/updateModel')
            .http_method(HttpMethodEnum.PUT)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('models')
                        .value(models)
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

    def update_string_with_form(self,
                                value):
        """Does a PUT request to /form/updateString.

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
            .path('/form/updateString')
            .http_method(HttpMethodEnum.PUT)
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

    def update_string_array_with_form(self,
                                      strings):
        """Does a PUT request to /form/updateString.

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
            .path('/form/updateString')
            .http_method(HttpMethodEnum.PUT)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('strings')
                        .value(strings)
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

    def send_integer_enum_array(self,
                                suites):
        """Does a POST request to /form/integerenum.

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
            .path('/form/integerenum')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('suites')
                        .value(suites)
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

    def send_string_enum_array(self,
                               days):
        """Does a POST request to /form/stringenum.

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
            .path('/form/stringenum')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('array')
                         .value(True))
            .form_param(Parameter()
                        .key('days')
                        .value(days)
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
