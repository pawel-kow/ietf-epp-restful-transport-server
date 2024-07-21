from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class HostChgType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None):  # noqa: E501
        """HostChgType - a model defined in OpenAPI

        :param name: The name of this HostChgType.  # noqa: E501
        :type name: str
        """
        self.openapi_types = {
            'name': str
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'HostChgType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The host_chgType of this HostChgType.  # noqa: E501
        :rtype: HostChgType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this HostChgType.


        :return: The name of this HostChgType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this HostChgType.


        :param name: The name of this HostChgType.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name
