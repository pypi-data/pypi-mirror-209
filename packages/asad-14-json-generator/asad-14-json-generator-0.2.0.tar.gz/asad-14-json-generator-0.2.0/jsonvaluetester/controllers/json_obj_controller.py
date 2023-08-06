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
from jsonvaluetester.models.schema_container import SchemaContainer


class JsonObjController(BaseController):

    """A Controller to access Endpoints in the jsonvaluetester API."""
    def __init__(self, config):
        super(JsonObjController, self).__init__(config)

    def send_schemain_model(self,
                            body):
        """Does a POST request to /body/sendSchemaInModel.

        Send Schema in Model

        Args:
            body (SchemaContainer): TODO: type description here.

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
            .path('/body/sendSchemaInModel')
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

    def send_schemaas_body(self,
                           body):
        """Does a POST request to /body/sendSchema.

        Send Schema as Body

        Args:
            body (dict): TODO: type description here.

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
            .path('/body/sendSchema')
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

    def send_schemaas_form(self,
                           options=dict()):
        """Does a POST request to /form/sendSchema.

        Send Schema as Form

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    content_type -- ContentType -- TODO: type description
                        here.
                    id -- int -- TODO: type description here.
                    model -- dict -- TODO: type description here.
                    model_array -- list of dict -- TODO: type description
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
            .path('/form/sendSchema')
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

    def send_schemaas_query(self,
                            options=dict()):
        """Does a POST request to /query/sendSchema.

        Send Schema as Query

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    id -- int -- TODO: type description here.
                    model -- dict -- TODO: type description here.
                    model_array -- list of dict -- TODO: type description
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
            .path('/query/sendSchema')
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

    def get_schema(self):
        """Does a GET request to /response/getSchema.

        Get Schema

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
            .path('/response/getSchema')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def get_schema_array(self):
        """Does a GET request to /response/getSchemaArray.

        Get Schema Array

        Returns:
            list of dict: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/getSchemaArray')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def get_schema_map(self):
        """Does a GET request to /response/getSchemaMap.

        Get Schema Map

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
            .path('/response/getSchemaMap')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
        ).execute()

    def get_schemain_model(self):
        """Does a GET request to /response/getSchemaInModel.

        Get Schema in Model

        Returns:
            SchemaContainer: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/response/getSchemaInModel')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SchemaContainer.from_dictionary)
        ).execute()
