import connexion
from typing import Dict
from typing import Tuple
from typing import Union
from flask import request

from openapi_server import util



try:
   from ..controller_impl import contacts_impl
except ImportError:
    pass

def contacts_id_delete(id, ):  # noqa: E501
    """Contact delete

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
        return contacts_impl.contacts_id_delete(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_id_delete in contacts_impl: {e}")


def contacts_id_get(id, filter=None, val=None, ):  # noqa: E501
    """Contact info

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
    :param repp_auth_info: Object authorization details
    :type repp_auth_info: str
    :param repp_roid: Object linked to authorization
    :type repp_roid: str
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
    repp_auth_info = request.headers.get('repp_auth_info')
    repp_roid = request.headers.get('repp_roid')










    body = None
    if connexion.request.is_json:
        body = connexion.request.get_json()



    try:
        return contacts_impl.contacts_id_get(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, repp_auth_info, repp_roid, filter, val, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_id_get in contacts_impl: {e}")


def contacts_id_head(id, ):  # noqa: E501
    """Contact check

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
        return contacts_impl.contacts_id_head(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_id_head in contacts_impl: {e}")


def contacts_id_patch(id, ):  # noqa: E501
    """Contact update

     # noqa: E501

    :param id: Object identifier
    :type id: str
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
        return contacts_impl.contacts_id_patch(id, repp_cltrid, repp_svcs, accept_language, body, repp_svcs_ext)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_id_patch in contacts_impl: {e}")


def contacts_id_transfers_latest_delete(id, ):  # noqa: E501
    """Contact transfer cancel

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
    :param repp_auth_info: Object authorization details
    :type repp_auth_info: str
    :param repp_roid: Object linked to authorization
    :type repp_roid: str
    :param body: Default request body for XML of JSON message
    :type body: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """

    repp_cltrid = request.headers.get('repp_cltrid')
    repp_svcs = request.headers.get('repp_svcs')
    accept_language = request.headers.get('accept_language')
    repp_svcs_ext = request.headers.get('repp_svcs_ext')
    repp_auth_info = request.headers.get('repp_auth_info')
    repp_roid = request.headers.get('repp_roid')








    body = None
    if connexion.request.is_json:
        body = connexion.request.get_json()



    try:
        return contacts_impl.contacts_id_transfers_latest_delete(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, repp_auth_info, repp_roid, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_id_transfers_latest_delete in contacts_impl: {e}")


def contacts_id_transfers_latest_get(id, ):  # noqa: E501
    """Contact transfer query

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
    :param repp_auth_info: Object authorization details
    :type repp_auth_info: str
    :param repp_roid: Object linked to authorization
    :type repp_roid: str
    :param body: Default request body for XML of JSON message
    :type body: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """

    repp_cltrid = request.headers.get('repp_cltrid')
    repp_svcs = request.headers.get('repp_svcs')
    accept_language = request.headers.get('accept_language')
    repp_svcs_ext = request.headers.get('repp_svcs_ext')
    repp_auth_info = request.headers.get('repp_auth_info')
    repp_roid = request.headers.get('repp_roid')








    body = None
    if connexion.request.is_json:
        body = connexion.request.get_json()



    try:
        return contacts_impl.contacts_id_transfers_latest_get(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, repp_auth_info, repp_roid, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_id_transfers_latest_get in contacts_impl: {e}")


def contacts_id_transfers_latest_put(id, ):  # noqa: E501
    """Contact transfer approve

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
    :param repp_auth_info: Object authorization details
    :type repp_auth_info: str
    :param repp_roid: Object linked to authorization
    :type repp_roid: str
    :param body: Default request body for XML of JSON message
    :type body: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """

    repp_cltrid = request.headers.get('repp_cltrid')
    repp_svcs = request.headers.get('repp_svcs')
    accept_language = request.headers.get('accept_language')
    repp_svcs_ext = request.headers.get('repp_svcs_ext')
    repp_auth_info = request.headers.get('repp_auth_info')
    repp_roid = request.headers.get('repp_roid')








    body = None
    if connexion.request.is_json:
        body = connexion.request.get_json()



    try:
        return contacts_impl.contacts_id_transfers_latest_put(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, repp_auth_info, repp_roid, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_id_transfers_latest_put in contacts_impl: {e}")


def contacts_id_transfers_post(id, ):  # noqa: E501
    """Contact transfer request

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
    :param repp_auth_info: Object authorization details
    :type repp_auth_info: str
    :param repp_roid: Object linked to authorization
    :type repp_roid: str
    :param body: Default request body for XML of JSON message
    :type body: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """

    repp_cltrid = request.headers.get('repp_cltrid')
    repp_svcs = request.headers.get('repp_svcs')
    accept_language = request.headers.get('accept_language')
    repp_svcs_ext = request.headers.get('repp_svcs_ext')
    repp_auth_info = request.headers.get('repp_auth_info')
    repp_roid = request.headers.get('repp_roid')








    body = None
    if connexion.request.is_json:
        body = connexion.request.get_json()



    try:
        return contacts_impl.contacts_id_transfers_post(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, repp_auth_info, repp_roid, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_id_transfers_post in contacts_impl: {e}")


def contacts_post():  # noqa: E501
    """Contact create

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
        return contacts_impl.contacts_post(repp_cltrid, repp_svcs, accept_language, body, repp_svcs_ext)
    except NameError as e:
        raise NotImplementedError(f"Missing module contacts_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function contacts_post in contacts_impl: {e}")

