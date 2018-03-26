import os
from unittest import TestCase

import httpretty

from json2xlsclient.client import Client


class TestTemplates(TestCase):

        def setUp(self):
            super(TestTemplates, self).setUp()
            self.server_url = 'http://localhost'
            self.client = Client(self.server_url)
            self.template_token = 'weqwe123123'
            self.expected_xls_token = 'sakdhasjasd'
            self.template_path = \
                os.path.abspath("tests/fixtures/school-example.xls")

        @httpretty.activate
        def test_create_template(self):
            body = '/xls/{}'.format(self.expected_xls_token)
            end_point = self.server_url + '/templates/'
            httpretty.register_uri(httpretty.POST,
                                   end_point,
                                   body=body,
                                   status=201)

            self.client.template.create(self.template_path)
            status_code = self.client.template.conn.last_response.status_code
            self.assertEquals(status_code, 201)

            expected_response = '/xls/{}'.format(self.expected_xls_token)
            self.assertEquals(self.client.template.conn.last_response.content,
                              expected_response)

        @httpretty.activate
        def test_update_template(self):
            update_endpoint = \
                self.server_url + '/templates/{}'.format(self.template_token)
            body = '/xls/{}'.format(self.expected_xls_token)
            httpretty.register_uri(httpretty.PUT, update_endpoint,
                                   body=body,
                                   status=201)

            self.client.template.update(self.template_token,
                                        self.template_path)

            status_code = self.client.template.conn.last_response.status_code
            self.assertEquals(status_code, 201)

            expected_response = '/xls/{}'.format(self.expected_xls_token)

            status_content = self.client.template.conn.last_response.content
            self.assertEquals(status_content, expected_response)

        @httpretty.activate
        def test_get_template(self):
            get_endpoint = \
                self.server_url + '/templates/{}'.format(self.template_token)
            httpretty.register_uri(httpretty.GET, get_endpoint,
                                   status=200)

            self.client.template.get(self.template_token)

            status_code = self.client.template.conn.last_response.status_code
            self.assertEquals(status_code, 200)

        @httpretty.activate
        def test_create_template_file_object(self):
            body = '/xls/{}'.format(self.expected_xls_token)
            end_point = self.server_url + '/templates/'
            httpretty.register_uri(httpretty.POST,
                                   end_point,
                                   body=body,
                                   status=201)

            fo = open(self.template_path, "rb")
            self.client.template.create(template_file=fo)
            status_code = self.client.template.conn.last_response.status_code
            self.assertEquals(status_code, 201)

            expected_response = '/xls/{}'.format(self.expected_xls_token)
            self.assertEquals(self.client.template.conn.last_response.content,
                              expected_response)
