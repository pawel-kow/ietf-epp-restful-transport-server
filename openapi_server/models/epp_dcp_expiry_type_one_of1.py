from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class EppDcpExpiryTypeOneOf1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, relative=None):  # noqa: E501
        """EppDcpExpiryTypeOneOf1 - a model defined in OpenAPI

        :param relative: The relative of this EppDcpExpiryTypeOneOf1.  # noqa: E501
        :type relative: str
        """
        self.openapi_types = {
            'relative': str
        }

        self.attribute_map = {
            'relative': 'relative'
        }

        self._relative = relative

    @classmethod
    def from_dict(cls, dikt) -> 'EppDcpExpiryTypeOneOf1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_dcpExpiryType_oneOf_1 of this EppDcpExpiryTypeOneOf1.  # noqa: E501
        :rtype: EppDcpExpiryTypeOneOf1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def relative(self) -> str:
        """Gets the relative of this EppDcpExpiryTypeOneOf1.


        :return: The relative of this EppDcpExpiryTypeOneOf1.
        :rtype: str
        """
        return self._relative

    @relative.setter
    def relative(self, relative: str):
        """Sets the relative of this EppDcpExpiryTypeOneOf1.


        :param relative: The relative of this EppDcpExpiryTypeOneOf1.
        :type relative: str
        """
        if relative is None:
            raise ValueError("Invalid value for `relative`, must not be `None`")  # noqa: E501

        self._relative = relative
