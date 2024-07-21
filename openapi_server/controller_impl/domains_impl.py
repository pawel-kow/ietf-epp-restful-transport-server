from openapi_server.models import (
    EppResponseType,
    EppTrIDType,
    EppResultType,
    EppExtAnyType
)

def domains_post(repp_cltrid, repp_svcs, accept_language, domain_create_request, repp_svcs_ext):
    
    print(f"{domain_create_request}")
    return EppResponseType(
        tr_id=EppTrIDType(
            cl_trid=repp_cltrid,
            sv_trid='CCC'
        ),
        res_data=EppExtAnyType()
    )