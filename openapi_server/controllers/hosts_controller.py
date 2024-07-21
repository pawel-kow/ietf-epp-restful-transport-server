import connexion
from typing import Dict
from typing import Tuple
from typing import Union
from flask import request

from openapi_server import util



try:
   from ..controller_impl import hosts_impl
except ImportError:
    pass

def hosts_id_delete(id, ):  # noqa: E501
    """Host delete

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
        return hosts_impl.hosts_id_delete(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module hosts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function hosts_id_delete in hosts_impl: {e}")


def hosts_id_get(id, filter=None, val=None, ):  # noqa: E501
    """Host info

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
    :param filter: 
    :type filter: str
    :param val: 
    :type val: str
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
        return hosts_impl.hosts_id_get(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, filter, val, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module hosts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function hosts_id_get in hosts_impl: {e}")


def hosts_id_head(id, ):  # noqa: E501
    """Host check

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
        return hosts_impl.hosts_id_head(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module hosts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function hosts_id_head in hosts_impl: {e}")


def hosts_id_patch(id, ):  # noqa: E501
    """Host update

     # noqa: E501

    :param repp_cltrid: Client transaction identifier
    :type repp_cltrid: str
    :param repp_svcs: Namespace used
    :type repp_svcs: str
    :param accept_language: Language used for response
    :type accept_language: str
    :param id: Object identifier
    :type id: str
    :param body: Default request body for XML of JSON message
    :type body: str
    :param repp_svcs_ext: Extension namespace used
    :type repp_svcs_ext: str

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
        return hosts_impl.hosts_id_patch(repp_cltrid, repp_svcs, accept_language, id, body, repp_svcs_ext)
    except NameError as e:
        raise NotImplementedError(f"Missing module hosts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function hosts_id_patch in hosts_impl: {e}")


def hosts_post():  # noqa: E501
    """Host create

     # noqa: E501

    :param repp_cltrid: Client transaction identifier
    :type repp_cltrid: str
    :param repp_svcs: Namespace used
    :type repp_svcs: str
    :param accept_language: Language used for response
    :type accept_language: str
    :param body: Default request body for XML of JSON message
    :type body: str
    :param repp_svcs_ext: Extension namespace used
    :type repp_svcs_ext: str

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
        return hosts_impl.hosts_post(repp_cltrid, repp_svcs, accept_language, body, repp_svcs_ext)
    except NameError as e:
        raise NotImplementedError(f"Missing module hosts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function hosts_post in hosts_impl: {e}")

