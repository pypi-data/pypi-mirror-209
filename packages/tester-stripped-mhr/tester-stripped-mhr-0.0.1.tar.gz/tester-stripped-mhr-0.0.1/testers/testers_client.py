# -*- coding: utf-8 -*-

"""
testers

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.global_configuration import GlobalConfiguration
from apimatic_core.decorators.lazy_property import LazyProperty
from testers.configuration import Configuration
from testers.controllers.base_controller import BaseController
from testers.configuration import Environment
from testers.controllers.response_types_controller\
    import ResponseTypesController
from testers.controllers.form_params_controller import FormParamsController
from testers.controllers.body_params_controller import BodyParamsController
from testers.controllers.error_codes_controller import ErrorCodesController
from testers.controllers.query_param_controller import QueryParamController
from testers.controllers.echo_controller import EchoController
from testers.controllers.header_controller import HeaderController
from testers.controllers.template_params_controller\
    import TemplateParamsController


class TestersClient(object):

    @LazyProperty
    def response_types(self):
        return ResponseTypesController(self.global_configuration)

    @LazyProperty
    def form_params(self):
        return FormParamsController(self.global_configuration)

    @LazyProperty
    def body_params(self):
        return BodyParamsController(self.global_configuration)

    @LazyProperty
    def error_codes(self):
        return ErrorCodesController(self.global_configuration)

    @LazyProperty
    def query_param(self):
        return QueryParamController(self.global_configuration)

    @LazyProperty
    def echo(self):
        return EchoController(self.global_configuration)

    @LazyProperty
    def header(self):
        return HeaderController(self.global_configuration)

    @LazyProperty
    def template_params(self):
        return TemplateParamsController(self.global_configuration)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
                 retry_methods=['GET', 'PUT'], environment=Environment.TESTING,
                 port='80', suites=1, config=None):
        if config is None:
            self.config = Configuration(
                                         http_client_instance=http_client_instance,
                                         override_http_client_configuration=override_http_client_configuration,
                                         http_call_back=http_call_back,
                                         timeout=timeout,
                                         max_retries=max_retries,
                                         backoff_factor=backoff_factor,
                                         retry_statuses=retry_statuses,
                                         retry_methods=retry_methods,
                                         environment=environment, port=port,
                                         suites=suites)
        else:
            self.config = config

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)

