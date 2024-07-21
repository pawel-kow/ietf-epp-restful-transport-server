from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class DomainAuthInfoChgTypeOneOf2(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, null=False):  # noqa: E501
        """DomainAuthInfoChgTypeOneOf2 - a model defined in OpenAPI

        :param null: The null of this DomainAuthInfoChgTypeOneOf2.  # noqa: E501
        :type null: bool
        """
        self.openapi_types = {
            'null': bool
        }

        self.attribute_map = {
            'null': 'null'
        }

        self._null = null

    @classmethod
    def from_dict(cls, dikt) -> 'DomainAuthInfoChgTypeOneOf2':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The domain_authInfoChgType_oneOf_2 of this DomainAuthInfoChgTypeOneOf2.  # noqa: E501
        :rtype: DomainAuthInfoChgTypeOneOf2
        """
        return util.deserialize_model(dikt, cls)

    @property
    def null(self) -> bool:
        """Gets the null of this DomainAuthInfoChgTypeOneOf2.


        :return: The null of this DomainAuthInfoChgTypeOneOf2.
        :rtype: bool
        """
        return self._null

    @null.setter
    def null(self, null: bool):
        """Sets the null of this DomainAuthInfoChgTypeOneOf2.


        :param null: The null of this DomainAuthInfoChgTypeOneOf2.
        :type null: bool
        """
        if null is None:
            raise ValueError("Invalid value for `null`, must not be `None`")  # noqa: E501

        self._null = null