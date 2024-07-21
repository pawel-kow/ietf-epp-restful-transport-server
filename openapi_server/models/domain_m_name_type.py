from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class DomainMNameType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None):  # noqa: E501
        """DomainMNameType - a model defined in OpenAPI

        :param name: The name of this DomainMNameType.  # noqa: E501
        :type name: List[str]
        """
        self.openapi_types = {
            'name': List[str]
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'DomainMNameType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The domain_mNameType of this DomainMNameType.  # noqa: E501
        :rtype: DomainMNameType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> List[str]:
        """Gets the name of this DomainMNameType.


        :return: The name of this DomainMNameType.
        :rtype: List[str]
        """
        return self._name

    @name.setter
    def name(self, name: List[str]):
        """Sets the name of this DomainMNameType.


        :param name: The name of this DomainMNameType.
        :type name: List[str]
        """
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._name = name