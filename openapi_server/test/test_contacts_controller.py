import unittest

from flask import json

from openapi_server.test import BaseTestCase


class TestContactsController(BaseTestCase):
    """ContactsController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_contacts_id_delete(self):
        """Test case for contacts_id_delete

        Contact delete
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
            '/repp/v1/contacts/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_contacts_id_get(self):
        """Test case for contacts_id_get

        Contact info
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
            '/repp/v1/contacts/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_contacts_id_head(self):
        """Test case for contacts_id_head

        Contact check
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
            '/repp/v1/contacts/{id}'.format(id='id_example'),
            method='HEAD',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_contacts_id_patch(self):
        """Test case for contacts_id_patch

        Contact update
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
            '/repp/v1/contacts/{id}'.format(id='id_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_contacts_id_transfers_latest_delete(self):
        """Test case for contacts_id_transfers_latest_delete

        Contact transfer cancel
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
            '/repp/v1/contacts/{id}/transfers/latest'.format(id='id_example'),
            method='DELETE',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_contacts_id_transfers_latest_get(self):
        """Test case for contacts_id_transfers_latest_get

        Contact transfer query
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
            '/repp/v1/contacts/{id}/transfers/latest'.format(id='id_example'),
            method='GET',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_contacts_id_transfers_latest_put(self):
        """Test case for contacts_id_transfers_latest_put

        Contact transfer approve
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
            '/repp/v1/contacts/{id}/transfers/latest'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_contacts_id_transfers_post(self):
        """Test case for contacts_id_transfers_post

        Contact transfer request
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
            '/repp/v1/contacts/{id}/transfers'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_contacts_post(self):
        """Test case for contacts_post

        Contact create
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
            '/repp/v1/contacts',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/epp+xml')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
