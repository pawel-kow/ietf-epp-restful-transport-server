from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class EppcomReasonType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value=None, lang=None):  # noqa: E501
        """EppcomReasonType - a model defined in OpenAPI

        :param value: The value of this EppcomReasonType.  # noqa: E501
        :type value: str
        :param lang: The lang of this EppcomReasonType.  # noqa: E501
        :type lang: str
        """
        self.openapi_types = {
            'value': str,
            'lang': str
        }

        self.attribute_map = {
            'value': '#value',
            'lang': '@lang'
        }

        self._value = value
        self._lang = lang

    @classmethod
    def from_dict(cls, dikt) -> 'EppcomReasonType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The eppcom_reasonType of this EppcomReasonType.  # noqa: E501
        :rtype: EppcomReasonType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> str:
        """Gets the value of this EppcomReasonType.


        :return: The value of this EppcomReasonType.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this EppcomReasonType.


        :param value: The value of this EppcomReasonType.
        :type value: str
        """
        if value is not None and len(value) > 32:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `32`")  # noqa: E501
        if value is not None and len(value) < 1:
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  # noqa: E501

        self._value = value

    @property
    def lang(self) -> str:
        """Gets the lang of this EppcomReasonType.


        :return: The lang of this EppcomReasonType.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang: str):
        """Sets the lang of this EppcomReasonType.


        :param lang: The lang of this EppcomReasonType.
        :type lang: str
        """

        self._lang = lang
