from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.eppcom_pw_auth_info_type import EppcomPwAuthInfoType
from openapi_server import util

from openapi_server.models.eppcom_pw_auth_info_type import EppcomPwAuthInfoType  # noqa: E501

class DomainAuthInfoChgTypeOneOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pw=None):  # noqa: E501
        """DomainAuthInfoChgTypeOneOf - a model defined in OpenAPI

        :param pw: The pw of this DomainAuthInfoChgTypeOneOf.  # noqa: E501
        :type pw: EppcomPwAuthInfoType
        """
        self.openapi_types = {
            'pw': EppcomPwAuthInfoType
        }

        self.attribute_map = {
            'pw': 'pw'
        }

        self._pw = pw

    @classmethod
    def from_dict(cls, dikt) -> 'DomainAuthInfoChgTypeOneOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The domain_authInfoChgType_oneOf of this DomainAuthInfoChgTypeOneOf.  # noqa: E501
        :rtype: DomainAuthInfoChgTypeOneOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pw(self) -> EppcomPwAuthInfoType:
        """Gets the pw of this DomainAuthInfoChgTypeOneOf.


        :return: The pw of this DomainAuthInfoChgTypeOneOf.
        :rtype: EppcomPwAuthInfoType
        """
        return self._pw

    @pw.setter
    def pw(self, pw: EppcomPwAuthInfoType):
        """Sets the pw of this DomainAuthInfoChgTypeOneOf.


        :param pw: The pw of this DomainAuthInfoChgTypeOneOf.
        :type pw: EppcomPwAuthInfoType
        """
        if pw is None:
            raise ValueError("Invalid value for `pw`, must not be `None`")  # noqa: E501

        self._pw = pw
