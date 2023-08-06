# -*- coding: utf-8 -*-

"""
jsonvaluetester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from jsonvaluetester.api_helper import APIHelper
from jsonvaluetester.configuration import Server
from jsonvaluetester.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from jsonvaluetester.http.http_method_enum import HttpMethodEnum
from jsonvaluetester.models.server_response import ServerResponse
from jsonvaluetester.models.value_container import ValueContainer


class JsonValController(BaseController):

    """A Controller to access Endpoints in the jsonvaluetester API."""
    def __init__(self, config):
        super(JsonValController, self).__init__(config)

    def send_valuein_model(self,
                           body):
        """Does a POST request to /body/sendValueInModel.

        Send Value in Model

        Args:
            body (ValueContainer): TODO: type description here.

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
            .path('/body/sendValueInModel')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body)
                        .is_required(True))
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

    def send_valueas_body(self,
                          body):
        """Does a POST request to /body/sendValue.

        Send Value as Body

        Args:
            body (object): TODO: type description here.

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
            .path('/body/sendValue')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('text/plain'))
            .body_param(Parameter()
                        .value(body)
                        .is_required(True))
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

    def send_valueas_form(self,
                          options=dict()):
        """Does a POST request to /form/sendValue.

        Send Value as Form

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    content_type -- ContentType -- TODO: type description
                        here.
                    id -- int -- TODO: type description here.
                    model -- object -- TODO: type description here.
                    model_array -- list of object -- TODO: type description
                        here.
                    model_map -- dict -- TODO: type description here.

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
            .path('/form/sendValue')
            .http_method(HttpMethodEnum.POST)
            .form_param(Parameter()
                        .key('id')
                        .value(options.get('id', None))
                        .is_required(True))
            .form_param(Parameter()
                        .key('model')
                        .value(options.get('model', None))
                        .is_required(True))
            .form_param(Parameter()
                        .key('modelArray')
                        .value(options.get('model_array', None)))
            .form_param(Parameter()
                        .key('modelMap')
                        .value(options.get('model_map', None)))
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

    def send_valueas_query(self,
                           options=dict()):
        """Does a POST request to /query/sendValue.

        Send Value as Query

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    id -- int -- TODO: type description here.
                    model -- object -- TODO: type description here.
                    model_array -- list of object -- TODO: type description
                        here.
                    model_map -- dict -- TODO: type description here.

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
            .path('/query/sendValue')
            .http_method(HttpMethodEnum.POST)
            .query_param(Parameter()
                         .key('id')
                         .value(options.get('id', None))
                         .is_required(True))
            .query_param(Parameter()
                         .key('model')
                         .value(options.get('model', None))
                         .is_required(True))
            .query_param(Parameter()
                         .key('modelArray')
                         .value(options.get('model_array', None)))
            .query_param(Parameter()
                         .key('modelMap')
                         .value(options.get('model_map', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServerResponse.from_dictionary)
        ).execute()

    def get_value(self):
        """Does a GET request to /response/getValue.

        Get Value

        Returns:
            object: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/getValue')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def get_value_array(self):
        """Does a GET request to /response/getValueArray.

        Get Value Array

        Returns:
            list of object: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/getValueArray')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def get_value_map(self):
        """Does a GET request to /response/getValueMap.

        Get Value Map

        Returns:
            dict: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/getValueMap')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def get_valuein_model(self):
        """Does a GET request to /response/getValueInModel.

        Get Value in Model

        Returns:
            ValueContainer: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/getValueInModel')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ValueContainer.from_dictionary)
        ).execute()
