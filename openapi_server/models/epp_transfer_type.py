from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class EppTransferType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, op=None):  # noqa: E501
        """EppTransferType - a model defined in OpenAPI

        :param op: The op of this EppTransferType.  # noqa: E501
        :type op: str
        """
        self.openapi_types = {
            'op': str
        }

        self.attribute_map = {
            'op': '@op'
        }

        self._op = op

    @classmethod
    def from_dict(cls, dikt) -> 'EppTransferType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_transferType of this EppTransferType.  # noqa: E501
        :rtype: EppTransferType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def op(self) -> str:
        """Gets the op of this EppTransferType.


        :return: The op of this EppTransferType.
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op: str):
        """Sets the op of this EppTransferType.


        :param op: The op of this EppTransferType.
        :type op: str
        """
        allowed_values = ["approve", "cancel", "query", "reject", "request"]  # noqa: E501
        if op not in allowed_values:
            raise ValueError(
                "Invalid value for `op` ({0}), must be one of {1}"
                .format(op, allowed_values)
            )

        self._op = op