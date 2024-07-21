from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class EppMsgType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value=None, lang=None):  # noqa: E501
        """EppMsgType - a model defined in OpenAPI

        :param value: The value of this EppMsgType.  # noqa: E501
        :type value: str
        :param lang: The lang of this EppMsgType.  # noqa: E501
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
    def from_dict(cls, dikt) -> 'EppMsgType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_msgType of this EppMsgType.  # noqa: E501
        :rtype: EppMsgType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> str:
        """Gets the value of this EppMsgType.


        :return: The value of this EppMsgType.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this EppMsgType.


        :param value: The value of this EppMsgType.
        :type value: str
        """

        self._value = value

    @property
    def lang(self) -> str:
        """Gets the lang of this EppMsgType.


        :return: The lang of this EppMsgType.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang: str):
        """Sets the lang of this EppMsgType.


        :param lang: The lang of this EppMsgType.
        :type lang: str
        """

        self._lang = lang
