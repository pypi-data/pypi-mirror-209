# -*- coding: utf-8 -*-

"""
jsonvaluetester

This file was automatically generated for Stamplay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from jsonvaluetester.api_helper import APIHelper


class ValueContainer(object):

    """Implementation of the 'ValueContainer' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        id (string): TODO: type description here.
        value (object): TODO: type description here.
        value_array (list of object): TODO: type description here.
        value_map (dict): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "value": 'value',
        "value_array": 'valueArray',
        "value_map": 'valueMap'
    }

    _optionals = [
        'value_array',
        'value_map',
    ]

    def __init__(self,
                 id=None,
                 name=None,
                 value=None,
                 value_array=APIHelper.SKIP,
                 value_map=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ValueContainer class"""

        # Initialize members of the class
        self.name = name 
        self.id = id 
        self.value = value 
        if value_array is not APIHelper.SKIP:
            self.value_array = value_array 
        if value_map is not APIHelper.SKIP:
            self.value_map = value_map 

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
        value = dictionary.get("value") if dictionary.get("value") else None
        value_array = dictionary.get("valueArray") if dictionary.get("valueArray") else APIHelper.SKIP
        value_map = dictionary.get("valueMap") if dictionary.get("valueMap") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(id,
                   name,
                   value,
                   value_array,
                   value_map,
                   dictionary)
