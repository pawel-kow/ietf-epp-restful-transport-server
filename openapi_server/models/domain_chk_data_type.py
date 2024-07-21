from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.domain_check_type import DomainCheckType
from openapi_server import util

from openapi_server.models.domain_check_type import DomainCheckType  # noqa: E501

class DomainChkDataType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cd=None):  # noqa: E501
        """DomainChkDataType - a model defined in OpenAPI

        :param cd: The cd of this DomainChkDataType.  # noqa: E501
        :type cd: List[DomainCheckType]
        """
        self.openapi_types = {
            'cd': List[DomainCheckType]
        }

        self.attribute_map = {
            'cd': 'cd'
        }

        self._cd = cd

    @classmethod
    def from_dict(cls, dikt) -> 'DomainChkDataType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The domain_chkDataType of this DomainChkDataType.  # noqa: E501
        :rtype: DomainChkDataType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cd(self) -> List[DomainCheckType]:
        """Gets the cd of this DomainChkDataType.


        :return: The cd of this DomainChkDataType.
        :rtype: List[DomainCheckType]
        """
        return self._cd

    @cd.setter
    def cd(self, cd: List[DomainCheckType]):
        """Sets the cd of this DomainChkDataType.


        :param cd: The cd of this DomainChkDataType.
        :type cd: List[DomainCheckType]
        """
        if cd is None:
            raise ValueError("Invalid value for `cd`, must not be `None`")  # noqa: E501
        if cd is not None and len(cd) < 1:
            raise ValueError("Invalid value for `cd`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._cd = cd
