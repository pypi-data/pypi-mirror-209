# -*- coding: utf-8 -*-

"""
jsonvaluetester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from jsonvaluetester.api_helper import APIHelper


class SchemaContainer(object):

    """Implementation of the 'SchemaContainer' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        id (string): TODO: type description here.
        schema (dict): TODO: type description here.
        schema_array (list of dict): TODO: type description here.
        schema_map (dict): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "schema": 'schema',
        "schema_array": 'schemaArray',
        "schema_map": 'schemaMap'
    }

    _optionals = [
        'schema_array',
        'schema_map',
    ]

    def __init__(self,
                 id=None,
                 name=None,
                 schema=None,
                 schema_array=APIHelper.SKIP,
                 schema_map=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the SchemaContainer class"""

        # Initialize members of the class
        self.name = name 
        self.id = id 
        self.schema = schema 
        if schema_array is not APIHelper.SKIP:
            self.schema_array = schema_array 
        if schema_map is not APIHelper.SKIP:
            self.schema_map = schema_map 

        # Add additional model properties to the instance
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        id = dictionary.get("id") if dictionary.get("id") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        schema = dictionary.get("schema") if dictionary.get("schema") else None
        schema_array = dictionary.get("schemaArray") if dictionary.get("schemaArray") else APIHelper.SKIP
        schema_map = dictionary.get("schemaMap") if dictionary.get("schemaMap") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(id,
                   name,
                   schema,
                   schema_array,
                   schema_map,
                   dictionary)
