import connexion
from typing import Dict
from typing import Tuple
from typing import Union
from flask import request

from openapi_server.models.domain_create_request import DomainCreateRequest  # noqa: E501
from openapi_server import util



try:
   from ..controller_impl import domains_impl
except ImportError:
    pass

def domains_id_delete(id, ):  # noqa: E501
    """Domain delete

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
        return domains_impl.domains_id_delete(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_delete in domains_impl: {e}")


def domains_id_get(id, filter=None, val=None, ):  # noqa: E501
    """Domain info

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
    :param filter: Name of attibute to filter on
    :type filter: str
    :param val: Value to use for filter
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
        return domains_impl.domains_id_get(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, repp_auth_info, repp_roid, filter, val, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_get in domains_impl: {e}")


def domains_id_head(id, ):  # noqa: E501
    """Domain check

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
        return domains_impl.domains_id_head(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_head in domains_impl: {e}")


def domains_id_patch(id, ):  # noqa: E501
    """Domain update

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
        return domains_impl.domains_id_patch(id, repp_cltrid, repp_svcs, accept_language, body, repp_svcs_ext)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_patch in domains_impl: {e}")


def domains_id_renewals_post(id, unit=None, value=None, current_date=None, ):  # noqa: E501
    """Domain renew

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
    :param unit: Unit used for renewal value (e.g. y for year)
    :type unit: str
    :param value: Value for renewal
    :type value: int
    :param current_date: Date on which the current validity period ends
    :type current_date: str
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
        return domains_impl.domains_id_renewals_post(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, unit, value, current_date, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_renewals_post in domains_impl: {e}")


def domains_id_transfers_latest_delete(id, ):  # noqa: E501
    """Domain transfer cancel

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
        return domains_impl.domains_id_transfers_latest_delete(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_transfers_latest_delete in domains_impl: {e}")


def domains_id_transfers_latest_get(id, ):  # noqa: E501
    """Domain transfer query

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
        return domains_impl.domains_id_transfers_latest_get(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, repp_auth_info, repp_roid, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_transfers_latest_get in domains_impl: {e}")


def domains_id_transfers_latest_put(id, ):  # noqa: E501
    """Domain transfer approve

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
        return domains_impl.domains_id_transfers_latest_put(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_transfers_latest_put in domains_impl: {e}")


def domains_id_transfers_post(id, unit=None, value=None, ):  # noqa: E501
    """Domain transfer request

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
    :param unit: Unit used for renewal value (e.g. y for year)
    :type unit: str
    :param value: Value for renewal
    :type value: int
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
        return domains_impl.domains_id_transfers_post(id, repp_cltrid, repp_svcs, accept_language, repp_svcs_ext, repp_auth_info, repp_roid, unit, value, body)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_id_transfers_post in domains_impl: {e}")


def domains_post():  # noqa: E501
    """Domain create

     # noqa: E501

    :param repp_cltrid: Client transaction identifier
    :type repp_cltrid: str
    :param repp_svcs: Namespace used
    :type repp_svcs: str
    :param accept_language: Language used for response
    :type accept_language: str
    :param domain_create_request: 
    :type domain_create_request: dict | bytes
    :param repp_svcs_ext: Extension namespace used
    :type repp_svcs_ext: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """

    repp_cltrid = request.headers.get('repp_cltrid')
    repp_svcs = request.headers.get('repp_svcs')
    accept_language = request.headers.get('accept_language')
    repp_svcs_ext = request.headers.get('repp_svcs_ext')




    if connexion.request.is_json:
        # deserialization happens here
        domain_create_request = DomainCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501




    try:
        return domains_impl.domains_post(repp_cltrid, repp_svcs, accept_language, domain_create_request, repp_svcs_ext)
    except NameError as e:
        raise NotImplementedError(f"Missing module domains_impl: {e}")
    except AttributeError as e:
        raise NotImplementedError(f"Missing controller implementation function domains_post in domains_impl: {e}")

