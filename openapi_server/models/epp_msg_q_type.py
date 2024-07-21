from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.epp_mixed_msg_type import EppMixedMsgType
from openapi_server import util

from openapi_server.models.epp_mixed_msg_type import EppMixedMsgType  # noqa: E501

class EppMsgQType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, count=None, id=None, msg=None, q_date=None):  # noqa: E501
        """EppMsgQType - a model defined in OpenAPI

        :param count: The count of this EppMsgQType.  # noqa: E501
        :type count: int
        :param id: The id of this EppMsgQType.  # noqa: E501
        :type id: str
        :param msg: The msg of this EppMsgQType.  # noqa: E501
        :type msg: EppMixedMsgType
        :param q_date: The q_date of this EppMsgQType.  # noqa: E501
        :type q_date: datetime
        """
        self.openapi_types = {
            'count': int,
            'id': str,
            'msg': EppMixedMsgType,
            'q_date': datetime
        }

        self.attribute_map = {
            'count': '@count',
            'id': '@id',
            'msg': 'msg',
            'q_date': 'qDate'
        }

        self._count = count
        self._id = id
        self._msg = msg
        self._q_date = q_date

    @classmethod
    def from_dict(cls, dikt) -> 'EppMsgQType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_msgQType of this EppMsgQType.  # noqa: E501
        :rtype: EppMsgQType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self) -> int:
        """Gets the count of this EppMsgQType.


        :return: The count of this EppMsgQType.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int):
        """Sets the count of this EppMsgQType.


        :param count: The count of this EppMsgQType.
        :type count: int
        """

        self._count = count

    @property
    def id(self) -> str:
        """Gets the id of this EppMsgQType.


        :return: The id of this EppMsgQType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this EppMsgQType.


        :param id: The id of this EppMsgQType.
        :type id: str
        """
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def msg(self) -> EppMixedMsgType:
        """Gets the msg of this EppMsgQType.


        :return: The msg of this EppMsgQType.
        :rtype: EppMixedMsgType
        """
        return self._msg

    @msg.setter
    def msg(self, msg: EppMixedMsgType):
        """Sets the msg of this EppMsgQType.


        :param msg: The msg of this EppMsgQType.
        :type msg: EppMixedMsgType
        """

        self._msg = msg

    @property
    def q_date(self) -> datetime:
        """Gets the q_date of this EppMsgQType.


        :return: The q_date of this EppMsgQType.
        :rtype: datetime
        """
        return self._q_date

    @q_date.setter
    def q_date(self, q_date: datetime):
        """Sets the q_date of this EppMsgQType.


        :param q_date: The q_date of this EppMsgQType.
        :type q_date: datetime
        """

        self._q_date = q_date
