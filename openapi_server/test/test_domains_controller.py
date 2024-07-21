import unittest

from flask import json

from openapi_server.models.domain_create_request import DomainCreateRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDomainsController(BaseTestCase):
    """DomainsController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_domains_id_delete(self):
        """Test case for domains_id_delete

        Domain delete
        """
        body = 'body_example'
        headers = { 
            'Accept': 'application/epp+json',
            'Content-Type': 'application/epp+xml',
            'repp_cltrid': 'repp_cltrid_example',
            'repp_svcs': 'repp_svcs_example',
            'repp_svcs_ext': 'repp_svcs_ext_example',
            'accept_language': 'accept_language_example',
        }
        response = self.client.open(
            '/repp/v1/domains/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_domains_id_get(self):
        """Test case for domains_id_get

        Domain info
        """
        body = 'body_example'
        query_string = [('filter', 'filter_example'),
                        ('val', 'val_example')]
        headers = { 
            'Accept': 'application/epp+json',
            'Content-Type': 'application/epp+xml',
            'repp_cltrid': 'repp_cltrid_example',
            'repp_svcs': 'repp_svcs_example',
            'repp_svcs_ext': 'repp_svcs_ext_example',
            'accept_language': 'accept_language_example',
            'repp_auth_info': 'repp_auth_info_example',
            'repp_roid': 'repp_roid_example',
        }
        response = self.client.open(
            '/repp/v1/domains/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_domains_id_head(self):
        """Test case for domains_id_head

        Domain check
        """
        body = 'body_example'
        headers = { 
            'Content-Type': 'application/epp+xml',
            'repp_cltrid': 'repp_cltrid_example',
            'repp_svcs': 'repp_svcs_example',
            'repp_svcs_ext': 'repp_svcs_ext_example',
            'accept_language': 'accept_language_example',
        }
        response = self.client.open(
            '/repp/v1/domains/{id}'.format(id='id_example'),
            method='HEAD',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_domains_id_patch(self):
        """Test case for domains_id_patch

        Domain update
        """
        body = 'body_example'
        headers = { 
            'Accept': 'application/epp+json',
            'Content-Type': 'application/epp+xml',
            'repp_cltrid': 'repp_cltrid_example',
            'repp_svcs': 'repp_svcs_example',
            'repp_svcs_ext': 'repp_svcs_ext_example',
            'accept_language': 'accept_language_example',
        }
        response = self.client.open(
            '/repp/v1/domains/{id}'.format(id='id_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_domains_id_renewals_post(self):
        """Test case for domains_id_renewals_post

        Domain renew
        """
        body = 'body_example'
        query_string = [('unit', 'y'),
                        ('value', 1),
                        ('current-date', '2023-12-01')]
        headers = { 
            'Accept': 'application/epp+json',
            'Content-Type': 'application/epp+xml',
            'repp_cltrid': 'repp_cltrid_example',
            'repp_svcs': 'repp_svcs_example',
            'repp_svcs_ext': 'repp_svcs_ext_example',
            'accept_language': 'accept_language_example',
        }
        response = self.client.open(
            '/repp/v1/domains/{id}/renewals'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_domains_id_transfers_latest_delete(self):
        """Test case for domains_id_transfers_latest_delete

        Domain transfer cancel
        """
        body = 'body_example'
        headers = { 
            'Accept': 'application/epp+json',
            'Content-Type': 'application/epp+xml',
            'repp_cltrid': 'repp_cltrid_example',
            'repp_svcs': 'repp_svcs_example',
            'repp_svcs_ext': 'repp_svcs_ext_example',
            'accept_language': 'accept_language_example',
        }
        response = self.client.open(
            '/repp/v1/domains/{id}/transfers/latest'.format(id='id_example'),
            method='DELETE',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_domains_id_transfers_latest_get(self):
        """Test case for domains_id_transfers_latest_get

        Domain transfer query
        """
        body = 'body_example'
        headers = { 
            'Accept': 'application/epp+json',
            'Content-Type': 'application/epp+xml',
            'repp_cltrid': 'repp_cltrid_example',
            'repp_svcs': 'repp_svcs_example',
            'repp_svcs_ext': 'repp_svcs_ext_example',
            'accept_language': 'accept_language_example',
            'repp_auth_info': 'repp_auth_info_example',
            'repp_roid': 'repp_roid_example',
        }
        response = self.client.open(
            '/repp/v1/domains/{id}/transfers/latest'.format(id='id_example'),
            method='GET',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_domains_id_transfers_latest_put(self):
        """Test case for domains_id_transfers_latest_put

        Domain transfer approve
        """
        body = 'body_example'
        headers = { 
            'Accept': 'application/epp+json',
            'Content-Type': 'application/epp+xml',
            'repp_cltrid': 'repp_cltrid_example',
            'repp_svcs': 'repp_svcs_example',
            'repp_svcs_ext': 'repp_svcs_ext_example',
            'accept_language': 'accept_language_example',
        }
        response = self.client.open(
            '/repp/v1/domains/{id}/transfers/latest'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_domains_id_transfers_post(self):
        """Test case for domains_id_transfers_post

        Domain transfer request
        """
        body = 'body_example'
        query_string = [('unit', 'y'),
                        ('value', 1)]
        headers = { 
            'Accept': 'application/epp+json',
            'Content-Type': 'application/epp+xml',
            'repp_cltrid': 'repp_cltrid_example',
            'repp_svcs': 'repp_svcs_example',
            'repp_svcs_ext': 'repp_svcs_ext_example',
            'accept_language': 'accept_language_example',
            'repp_auth_info': 'repp_auth_info_example',
            'repp_roid': 'repp_roid_example',
        }
        response = self.client.open(
            '/repp/v1/domains/{id}/transfers'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_domains_post(self):
        """Test case for domains_post

        Domain create
        """
        domain_create_request = {"command":{"create":{"period":{"#value":8,"@unit":"y"},"ns":{"hostObj":[null,null]},"contact":[{"@type":"admin","#value":"#value"},{"@type":"admin","#value":"#value"}],"name":"name","registrant":"registrant","authInfo":{"pw":"{}"}}}}
        headers = { 
            'Accept': 'application/epp+json',
            'Content-Type': 'application/json',
            'repp_cltrid': 'repp_cltrid_example',
            'repp_svcs': 'repp_svcs_example',
            'repp_svcs_ext': 'repp_svcs_ext_example',
            'accept_language': 'accept_language_example',
        }
        response = self.client.open(
            '/repp/v1/domains',
            method='POST',
            headers=headers,
            data=json.dumps(domain_create_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
