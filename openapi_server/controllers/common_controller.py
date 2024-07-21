import connexion
from typing import Dict
from typing import Tuple
from typing import Union
from flask import request

from openapi_server import util



try:
   from ..controller_impl import common_impl
except ImportError:
    pass

def messages_get():  # noqa: E501
    """Poll request

     # noqa: E501

    :param repp_cltrid: Client transaction identifier
    :type repp_cltrid: str
    :param repp_svcs: Namespace used
    :type repp_svcs: str
    :param accept_language: Language used for response
    :type accept_language: str
    :param repp_svcs_ext: Extension namespace used
    :type repp_svcs_ext: str
    :param body: Default request body for XML of JSON message
    :type body: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """

    repp_cltrid = request.headers.get('repp_cltrid')
    repp_svcs = request.headers.get('repp_svcs')
    accept_language = request.headers.get('accept_language')
    repp_svcs_ext = request.headers.get('repp_svcs_ext')





    body = None
    if connexion.request.is_json:
        body = connexion.request.get_json()



    try:
        return common_impl.messages_get(repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module common_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function messages_get in common_impl: {e}")


def messages_id_head(id, ):  # noqa: E501
    """Poll ack

     # noqa: E501

    :param id: Object identifier
    :type id: str
    :param repp_cltrid: Client transaction identifier
    :type repp_cltrid: str
    :param repp_svcs: Namespace used
    :type repp_svcs: str
    :param accept_language: Language used for response
    :type accept_language: str
    :param repp_svcs_ext: Extension namespace used
    :type repp_svcs_ext: str
    :param body: Default request body for XML of JSON message
    :type body: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """

    repp_cltrid = request.headers.get('repp_cltrid')
    repp_svcs = request.headers.get('repp_svcs')
    accept_language = request.headers.get('accept_language')
    repp_svcs_ext = request.headers.get('repp_svcs_ext')






    body = None
    if connexion.request.is_json:
        body = connexion.request.get_json()



    try:
        return common_impl.messages_id_head(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module common_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function messages_id_head in common_impl: {e}")


def root_get():  # noqa: E501
    """Hello

     # noqa: E501

    :param accept_language: Language used for response
    :type accept_language: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """

    accept_language = request.headers.get('accept_language')




    try:
        return common_impl.root_get(accept_language)
    except NameError as e:
        raise NotImplementedError(f"Missing module common_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function root_get in common_impl: {e}")

