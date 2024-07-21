from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.domain_auth_info_type import DomainAuthInfoType
from openapi_server.models.domain_contact_type import DomainContactType
from openapi_server.models.domain_ns_type import DomainNsType
from openapi_server.models.domain_period_type import DomainPeriodType
from openapi_server import util

from openapi_server.models.domain_auth_info_type import DomainAuthInfoType  # noqa: E501
from openapi_server.models.domain_contact_type import DomainContactType  # noqa: E501
from openapi_server.models.domain_ns_type import DomainNsType  # noqa: E501
from openapi_server.models.domain_period_type import DomainPeriodType  # noqa: E501

class DomainCreateType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, auth_info=None, contact=None, name=None, ns=None, period=None, registrant=None):  # noqa: E501
        """DomainCreateType - a model defined in OpenAPI

        :param auth_info: The auth_info of this DomainCreateType.  # noqa: E501
        :type auth_info: DomainAuthInfoType
        :param contact: The contact of this DomainCreateType.  # noqa: E501
        :type contact: List[DomainContactType]
        :param name: The name of this DomainCreateType.  # noqa: E501
        :type name: str
        :param ns: The ns of this DomainCreateType.  # noqa: E501
        :type ns: DomainNsType
        :param period: The period of this DomainCreateType.  # noqa: E501
        :type period: DomainPeriodType
        :param registrant: The registrant of this DomainCreateType.  # noqa: E501
        :type registrant: str
        """
        self.openapi_types = {
            'auth_info': DomainAuthInfoType,
            'contact': List[DomainContactType],
            'name': str,
            'ns': DomainNsType,
            'period': DomainPeriodType,
            'registrant': str
        }

        self.attribute_map = {
            'auth_info': 'authInfo',
            'contact': 'contact',
            'name': 'name',
            'ns': 'ns',
            'period': 'period',
            'registrant': 'registrant'
        }

        self._auth_info = auth_info
        self._contact = contact
        self._name = name
        self._ns = ns
        self._period = period
        self._registrant = registrant

    @classmethod
    def from_dict(cls, dikt) -> 'DomainCreateType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The domain_createType of this DomainCreateType.  # noqa: E501
        :rtype: DomainCreateType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def auth_info(self) -> DomainAuthInfoType:
        """Gets the auth_info of this DomainCreateType.


        :return: The auth_info of this DomainCreateType.
        :rtype: DomainAuthInfoType
        """
        return self._auth_info

    @auth_info.setter
    def auth_info(self, auth_info: DomainAuthInfoType):
        """Sets the auth_info of this DomainCreateType.


        :param auth_info: The auth_info of this DomainCreateType.
        :type auth_info: DomainAuthInfoType
        """
        if auth_info is None:
            raise ValueError("Invalid value for `auth_info`, must not be `None`")  # noqa: E501

        self._auth_info = auth_info

    @property
    def contact(self) -> List[DomainContactType]:
        """Gets the contact of this DomainCreateType.


        :return: The contact of this DomainCreateType.
        :rtype: List[DomainContactType]
        """
        return self._contact

    @contact.setter
    def contact(self, contact: List[DomainContactType]):
        """Sets the contact of this DomainCreateType.


        :param contact: The contact of this DomainCreateType.
        :type contact: List[DomainContactType]
        """
        if contact is not None and len(contact) < 0:
            raise ValueError("Invalid value for `contact`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._contact = contact

    @property
    def name(self) -> str:
        """Gets the name of this DomainCreateType.


        :return: The name of this DomainCreateType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this DomainCreateType.


        :param name: The name of this DomainCreateType.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def ns(self) -> DomainNsType:
        """Gets the ns of this DomainCreateType.


        :return: The ns of this DomainCreateType.
        :rtype: DomainNsType
        """
        return self._ns

    @ns.setter
    def ns(self, ns: DomainNsType):
        """Sets the ns of this DomainCreateType.


        :param ns: The ns of this DomainCreateType.
        :type ns: DomainNsType
        """

        self._ns = ns

    @property
    def period(self) -> DomainPeriodType:
        """Gets the period of this DomainCreateType.


        :return: The period of this DomainCreateType.
        :rtype: DomainPeriodType
        """
        return self._period

    @period.setter
    def period(self, period: DomainPeriodType):
        """Sets the period of this DomainCreateType.


        :param period: The period of this DomainCreateType.
        :type period: DomainPeriodType
        """

        self._period = period

    @property
    def registrant(self) -> str:
        """Gets the registrant of this DomainCreateType.


        :return: The registrant of this DomainCreateType.
        :rtype: str
        """
        return self._registrant

    @registrant.setter
    def registrant(self, registrant: str):
        """Sets the registrant of this DomainCreateType.


        :param registrant: The registrant of this DomainCreateType.
        :type registrant: str
        """
        if registrant is not None and len(registrant) > 16:
            raise ValueError("Invalid value for `registrant`, length must be less than or equal to `16`")  # noqa: E501
        if registrant is not None and len(registrant) < 3:
            raise ValueError("Invalid value for `registrant`, length must be greater than or equal to `3`")  # noqa: E501

        self._registrant = registrant
