from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class EppDcpRetentionTypeOneOf1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, indefinite=False):  # noqa: E501
        """EppDcpRetentionTypeOneOf1 - a model defined in OpenAPI

        :param indefinite: The indefinite of this EppDcpRetentionTypeOneOf1.  # noqa: E501
        :type indefinite: bool
        """
        self.openapi_types = {
            'indefinite': bool
        }

        self.attribute_map = {
            'indefinite': 'indefinite'
        }

        self._indefinite = indefinite

    @classmethod
    def from_dict(cls, dikt) -> 'EppDcpRetentionTypeOneOf1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_dcpRetentionType_oneOf_1 of this EppDcpRetentionTypeOneOf1.  # noqa: E501
        :rtype: EppDcpRetentionTypeOneOf1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def indefinite(self) -> bool:
        """Gets the indefinite of this EppDcpRetentionTypeOneOf1.


        :return: The indefinite of this EppDcpRetentionTypeOneOf1.
        :rtype: bool
        """
        return self._indefinite

    @indefinite.setter
    def indefinite(self, indefinite: bool):
        """Sets the indefinite of this EppDcpRetentionTypeOneOf1.


        :param indefinite: The indefinite of this EppDcpRetentionTypeOneOf1.
        :type indefinite: bool
        """
        if indefinite is None:
            raise ValueError("Invalid value for `indefinite`, must not be `None`")  # noqa: E501

        self._indefinite = indefinite