from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.domain_auth_info_chg_type_one_of import DomainAuthInfoChgTypeOneOf
from openapi_server.models.domain_auth_info_chg_type_one_of1 import DomainAuthInfoChgTypeOneOf1
from openapi_server.models.eppcom_ext_auth_info_type import EppcomExtAuthInfoType
from openapi_server.models.eppcom_pw_auth_info_type import EppcomPwAuthInfoType
from openapi_server import util

from openapi_server.models.domain_auth_info_chg_type_one_of import DomainAuthInfoChgTypeOneOf  # noqa: E501
from openapi_server.models.domain_auth_info_chg_type_one_of1 import DomainAuthInfoChgTypeOneOf1  # noqa: E501
from openapi_server.models.eppcom_ext_auth_info_type import EppcomExtAuthInfoType  # noqa: E501
from openapi_server.models.eppcom_pw_auth_info_type import EppcomPwAuthInfoType  # noqa: E501

class DomainAuthInfoType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pw=None, ext=None):  # noqa: E501
        """DomainAuthInfoType - a model defined in OpenAPI

        :param pw: The pw of this DomainAuthInfoType.  # noqa: E501
        :type pw: EppcomPwAuthInfoType
        :param ext: The ext of this DomainAuthInfoType.  # noqa: E501
        :type ext: EppcomExtAuthInfoType
        """
        self.openapi_types = {
            'pw': EppcomPwAuthInfoType,
            'ext': EppcomExtAuthInfoType
        }

        self.attribute_map = {
            'pw': 'pw',
            'ext': 'ext'
        }

        self._pw = pw
        self._ext = ext

    @classmethod
    def from_dict(cls, dikt) -> 'DomainAuthInfoType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The domain_authInfoType of this DomainAuthInfoType.  # noqa: E501
        :rtype: DomainAuthInfoType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pw(self) -> EppcomPwAuthInfoType:
        """Gets the pw of this DomainAuthInfoType.


        :return: The pw of this DomainAuthInfoType.
        :rtype: EppcomPwAuthInfoType
        """
        return self._pw

    @pw.setter
    def pw(self, pw: EppcomPwAuthInfoType):
        """Sets the pw of this DomainAuthInfoType.


        :param pw: The pw of this DomainAuthInfoType.
        :type pw: EppcomPwAuthInfoType
        """
        if pw is None:
            raise ValueError("Invalid value for `pw`, must not be `None`")  # noqa: E501

        self._pw = pw

    @property
    def ext(self) -> EppcomExtAuthInfoType:
        """Gets the ext of this DomainAuthInfoType.


        :return: The ext of this DomainAuthInfoType.
        :rtype: EppcomExtAuthInfoType
        """
        return self._ext

    @ext.setter
    def ext(self, ext: EppcomExtAuthInfoType):
        """Sets the ext of this DomainAuthInfoType.


        :param ext: The ext of this DomainAuthInfoType.
        :type ext: EppcomExtAuthInfoType
        """
        if ext is None:
            raise ValueError("Invalid value for `ext`, must not be `None`")  # noqa: E501

        self._ext = ext