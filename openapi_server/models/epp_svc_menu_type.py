from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.epp_ext_uri_type import EppExtURIType
from openapi_server.models.epp_version_type import EppVersionType
from openapi_server import util

from openapi_server.models.epp_ext_uri_type import EppExtURIType  # noqa: E501
from openapi_server.models.epp_version_type import EppVersionType  # noqa: E501

class EppSvcMenuType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, lang=None, obj_uri=None, svc_extension=None, version=None):  # noqa: E501
        """EppSvcMenuType - a model defined in OpenAPI

        :param lang: The lang of this EppSvcMenuType.  # noqa: E501
        :type lang: List[str]
        :param obj_uri: The obj_uri of this EppSvcMenuType.  # noqa: E501
        :type obj_uri: List[str]
        :param svc_extension: The svc_extension of this EppSvcMenuType.  # noqa: E501
        :type svc_extension: EppExtURIType
        :param version: The version of this EppSvcMenuType.  # noqa: E501
        :type version: List[EppVersionType]
        """
        self.openapi_types = {
            'lang': List[str],
            'obj_uri': List[str],
            'svc_extension': EppExtURIType,
            'version': List[EppVersionType]
        }

        self.attribute_map = {
            'lang': 'lang',
            'obj_uri': 'objURI',
            'svc_extension': 'svcExtension',
            'version': 'version'
        }

        self._lang = lang
        self._obj_uri = obj_uri
        self._svc_extension = svc_extension
        self._version = version

    @classmethod
    def from_dict(cls, dikt) -> 'EppSvcMenuType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The epp_svcMenuType of this EppSvcMenuType.  # noqa: E501
        :rtype: EppSvcMenuType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lang(self) -> List[str]:
        """Gets the lang of this EppSvcMenuType.


        :return: The lang of this EppSvcMenuType.
        :rtype: List[str]
        """
        return self._lang

    @lang.setter
    def lang(self, lang: List[str]):
        """Sets the lang of this EppSvcMenuType.


        :param lang: The lang of this EppSvcMenuType.
        :type lang: List[str]
        """
        if lang is None:
            raise ValueError("Invalid value for `lang`, must not be `None`")  # noqa: E501
        if lang is not None and len(lang) < 1:
            raise ValueError("Invalid value for `lang`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._lang = lang

    @property
    def obj_uri(self) -> List[str]:
        """Gets the obj_uri of this EppSvcMenuType.


        :return: The obj_uri of this EppSvcMenuType.
        :rtype: List[str]
        """
        return self._obj_uri

    @obj_uri.setter
    def obj_uri(self, obj_uri: List[str]):
        """Sets the obj_uri of this EppSvcMenuType.


        :param obj_uri: The obj_uri of this EppSvcMenuType.
        :type obj_uri: List[str]
        """
        if obj_uri is None:
            raise ValueError("Invalid value for `obj_uri`, must not be `None`")  # noqa: E501
        if obj_uri is not None and len(obj_uri) < 1:
            raise ValueError("Invalid value for `obj_uri`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._obj_uri = obj_uri

    @property
    def svc_extension(self) -> EppExtURIType:
        """Gets the svc_extension of this EppSvcMenuType.


        :return: The svc_extension of this EppSvcMenuType.
        :rtype: EppExtURIType
        """
        return self._svc_extension

    @svc_extension.setter
    def svc_extension(self, svc_extension: EppExtURIType):
        """Sets the svc_extension of this EppSvcMenuType.


        :param svc_extension: The svc_extension of this EppSvcMenuType.
        :type svc_extension: EppExtURIType
        """

        self._svc_extension = svc_extension

    @property
    def version(self) -> List[EppVersionType]:
        """Gets the version of this EppSvcMenuType.


        :return: The version of this EppSvcMenuType.
        :rtype: List[EppVersionType]
        """
        return self._version

    @version.setter
    def version(self, version: List[EppVersionType]):
        """Sets the version of this EppSvcMenuType.


        :param version: The version of this EppSvcMenuType.
        :type version: List[EppVersionType]
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if version is not None and len(version) < 1:
            raise ValueError("Invalid value for `version`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._version = version
