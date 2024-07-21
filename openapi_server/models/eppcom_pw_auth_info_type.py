from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class EppcomPwAuthInfoType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value=None, roid=None):  # noqa: E501
        """EppcomPwAuthInfoType - a model defined in OpenAPI

        :param value: The value of this EppcomPwAuthInfoType.  # noqa: E501
        :type value: str
        :param roid: The roid of this EppcomPwAuthInfoType.  # noqa: E501
        :type roid: str
        """
        self.openapi_types = {
            'value': str,
            'roid': str
        }

        self.attribute_map = {
            'value': '#value',
            'roid': '@roid'
        }

        self._value = value
        self._roid = roid

    @classmethod
    def from_dict(cls, dikt) -> 'EppcomPwAuthInfoType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The eppcom_pwAuthInfoType of this EppcomPwAuthInfoType.  # noqa: E501
        :rtype: EppcomPwAuthInfoType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> str:
        """Gets the value of this EppcomPwAuthInfoType.


        :return: The value of this EppcomPwAuthInfoType.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this EppcomPwAuthInfoType.


        :param value: The value of this EppcomPwAuthInfoType.
        :type value: str
        """

        self._value = value

    @property
    def roid(self) -> str:
        """Gets the roid of this EppcomPwAuthInfoType.


        :return: The roid of this EppcomPwAuthInfoType.
        :rtype: str
        """
        return self._roid

    @roid.setter
    def roid(self, roid: str):
        """Sets the roid of this EppcomPwAuthInfoType.


        :param roid: The roid of this EppcomPwAuthInfoType.
        :type roid: str
        """

        self._roid = roid
