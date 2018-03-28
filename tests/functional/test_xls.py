import os
from unittest import TestCase

import httpretty

from json2xlsclient.client import Client


class TestFunctionalXLS(TestCase):

    @httpretty.activate
    def test_generate_xls(self):
        gen_endpoint = self.server_url + '/xls/{}'.format(self.template_token)

        httpretty.register_uri(httpretty.POST, gen_endpoint,
                               body='/xls/{}'.format(self.expected_xls_token),
                               status=201)

        self.client.xls.create(self.template_token, self.json_path)
        self.assertEquals(self.client.xls.conn.last_response.status_code,
                          201)
        expected_response = '/xls/{}'.format(self.expected_xls_token)
        expected_response = expected_response.encode('utf-8')

        self.assertEquals(self.client.xls.conn.last_response.content,
                          expected_response)

    @httpretty.activate
    def test_get_generated_xls(self):
        get_endpoint = self.server_url + '/xls/{}'.format(self.xls_token)

        httpretty.register_uri(httpretty.GET, get_endpoint, status=200)

        self.client.xls.get(self.xls_token)
        self.assertEquals(self.client.xls.conn.last_response.status_code,
                          200)

    @httpretty.activate
    def test_regenerate_xls(self):
        up_endpoint = self.server_url + '/xls/{}'.format(self.template_token)
        httpretty.register_uri(httpretty.PUT, up_endpoint,
                               body='/xls/{}'.format(self.expected_xls_token),
                               status=201)

# TODO(james): uncomment when `PUT /xls/` gets fixed (see onaio/json-to-xls#3)
        # self.client.xls.update(self.template_token, self.json_path)
        # self.assertEquals(self.client.xls.conn.last_response.status_code,
        #                   201)

        # expected_response = '/xls/{}'.format(self.expected_xls_token)
        # self.assertEquals(self.client.xls.conn.last_response.content,
        #                   expected_response)

    def setUp(self):
        super(TestFunctionalXLS, self).setUp()

        self.server_url = 'http://localhost'
        self.client = Client(self.server_url)
        self.template_token = 'weqwe123123'
        self.xls_token = 'fsasdfosansdoq3'
        self.expected_xls_token = 'sakdhasjasd'
        self.json_path = \
            os.path.abspath("tests/fixtures/schools.json")

    def tearDown(self):
        super(TestFunctionalXLS, self).tearDown()
