from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.domain_host_attr_type import DomainHostAttrType
from openapi_server import util

from openapi_server.models.domain_host_attr_type import DomainHostAttrType  # noqa: E501

class DomainNsTypeOneOf1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, host_attr=None):  # noqa: E501
        """DomainNsTypeOneOf1 - a model defined in OpenAPI

        :param host_attr: The host_attr of this DomainNsTypeOneOf1.  # noqa: E501
        :type host_attr: List[DomainHostAttrType]
        """
        self.openapi_types = {
            'host_attr': List[DomainHostAttrType]
        }

        self.attribute_map = {
            'host_attr': 'hostAttr'
        }

        self._host_attr = host_attr

    @classmethod
    def from_dict(cls, dikt) -> 'DomainNsTypeOneOf1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The domain_nsType_oneOf_1 of this DomainNsTypeOneOf1.  # noqa: E501
        :rtype: DomainNsTypeOneOf1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def host_attr(self) -> List[DomainHostAttrType]:
        """Gets the host_attr of this DomainNsTypeOneOf1.


        :return: The host_attr of this DomainNsTypeOneOf1.
        :rtype: List[DomainHostAttrType]
        """
        return self._host_attr

    @host_attr.setter
    def host_attr(self, host_attr: List[DomainHostAttrType]):
        """Sets the host_attr of this DomainNsTypeOneOf1.


        :param host_attr: The host_attr of this DomainNsTypeOneOf1.
        :type host_attr: List[DomainHostAttrType]
        """
        if host_attr is not None and len(host_attr) < 1:
            raise ValueError("Invalid value for `host_attr`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._host_attr = host_attr
