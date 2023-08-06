# -*- coding: utf-8 -*-

"""
testers

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import platform
from apimatic_core.api_call import ApiCall
from apimatic_core.types.error_case import ErrorCase
from testers.exceptions.api_exception import APIException
from testers.exceptions.nested_model_exception import NestedModelException
from testers.exceptions.global_test_exception import GlobalTestException


class BaseController(object):

    """All controllers inherit from this base class.

    Attributes:
        config (Configuration): The HttpClient which a specific controller
            instance will use. By default all the controller objects share
            the same HttpClient. A user can use his own custom HttpClient
            as well.
        http_call_back (HttpCallBack): An object which holds call back
            methods to be called before and after the execution of an HttpRequest.
        new_api_call_builder (APICall): Returns the API Call builder instance.

    """


    @staticmethod
    def global_errors():
        return {
            'default': ErrorCase().error_message('Invalid response.').exception_type(GlobalTestException),
            '400': ErrorCase().error_message('400 Global').exception_type(APIException),
            '402': ErrorCase().error_message('402 Global').exception_type(APIException),
            '403': ErrorCase().error_message('403 Global').exception_type(APIException),
            '404': ErrorCase().error_message('404 Global').exception_type(APIException),
            '412': ErrorCase().error_message('Precondition Failed').exception_type(NestedModelException),
            '500': ErrorCase().error_message('500 Global').exception_type(GlobalTestException),
        }

    def __init__(self, config):
        self._global_config = config
        self._config = self._global_config.get_http_client_configuration()
        self._http_call_back = self.config.http_callback
        self.api_call = ApiCall(config)

    @property
    def config(self):
        return self._config

    @property
    def http_call_back(self):
        return self._http_call_back

    @property
    def new_api_call_builder(self):
        return self.api_call.new_builder

