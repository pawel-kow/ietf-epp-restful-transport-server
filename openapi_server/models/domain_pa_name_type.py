from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class DomainPaNameType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value=None, pa_result=None):  # noqa: E501
        """DomainPaNameType - a model defined in OpenAPI

        :param value: The value of this DomainPaNameType.  # noqa: E501
        :type value: str
        :param pa_result: The pa_result of this DomainPaNameType.  # noqa: E501
        :type pa_result: bool
        """
        self.openapi_types = {
            'value': str,
            'pa_result': bool
        }

        self.attribute_map = {
            'value': '#value',
            'pa_result': '@paResult'
        }

        self._value = value
        self._pa_result = pa_result

    @classmethod
    def from_dict(cls, dikt) -> 'DomainPaNameType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The domain_paNameType of this DomainPaNameType.  # noqa: E501
        :rtype: DomainPaNameType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> str:
        """Gets the value of this DomainPaNameType.


        :return: The value of this DomainPaNameType.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this DomainPaNameType.


        :param value: The value of this DomainPaNameType.
        :type value: str
        """
        if value is not None and len(value) > 255:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `255`")  # noqa: E501
        if value is not None and len(value) < 1:
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  # noqa: E501

        self._value = value

    @property
    def pa_result(self) -> bool:
        """Gets the pa_result of this DomainPaNameType.


        :return: The pa_result of this DomainPaNameType.
        :rtype: bool
        """
        return self._pa_result

    @pa_result.setter
    def pa_result(self, pa_result: bool):
        """Sets the pa_result of this DomainPaNameType.


        :param pa_result: The pa_result of this DomainPaNameType.
        :type pa_result: bool
        """

        self._pa_result = pa_result