from openapi_server.models import (
    EppResponseType,
    EppTrIDType,
    EppResultType,
    EppExtAnyType
)

import datetime

def domains_post(repp_cltrid, repp_svcs, accept_language, domain_create_request, repp_svcs_ext):
    if domain_create_request.command.extension is not None:
        if domain_create_request.command.extension.sec_dns is not None and \
            'urn:ietf:params:xml:ns:secDNS-1.1' not in repp_svcs.split(','):
            raise ValueError(f"secDNS extension provided but not specified in repp_svcs: {repp_svcs}")
    # if domain_create_request.command.cl_trid is not None \
    #     and repp_cltrid is not None \
    #     and domain_create_request.command.cl_trid != repp_cltrid:
    #     raise ValueError(f"repp_cltrid {repp_cltrid} and cl_trid {domain_create_request.command.cl_trid} are not equal.")

    print(f"{domain_create_request}")
    return EppResponseType(
        tr_id=EppTrIDType(
            cl_trid=repp_cltrid,
            sv_trid=datetime.datetime.now().isoformat()
        ),
        res_data=EppExtAnyType()
    )