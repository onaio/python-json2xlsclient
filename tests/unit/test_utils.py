from json2xlsclient.utils import Connection
from json2xlsclient.exceptions import ClientException
from json2xlsclient.exceptions import ApiException
import json
import mock
import unittest


class MockResponse(object):

    def __init__(self, status_code, reason=None, text=None):
        self.status_code = status_code
        self.reason = reason
        self.text = text


class HTTPConnectionTestCase(unittest.TestCase):

    def test_connection_create(self):
        with self.assertRaises(ClientException):
            Connection('ftp://localhost')


class HTTPMethodsTestCase(unittest.TestCase):

    def setUp(self):
        self.host = 'http://localhost'
        self.path = '/path/to/resource'
        self.url = '{}{}'.format(self.host, self.path)
        self.ua_header = {'user-agent': 'python-json2xlsclient'}
        self.conn = Connection(self.host)
        self.json_data = {
            "district": "District A",
            "schools": [
                {"name": "School A",
                 "males": 40,
                 "females": 50},
                {"name": "School B",
                 "males": 56,
                 "females": 45},
                {"name": "School C",
                 "males": 34,
                 "females": 63}]
        }

    def test_request(self):
        with mock.patch.object(self.conn, '_request',
                               return_value=MockResponse(400)):
            with self.assertRaises(ApiException):
                self.conn.request('PUT', self.path)

        with mock.patch.object(self.conn, '_request',
                               return_value=MockResponse(500)):
            with self.assertRaises(ApiException):
                self.conn.request('PUT', self.path)

        with mock.patch.object(self.conn, '_request',
                               return_value=MockResponse(100)):
            with self.assertRaises(ApiException):
                self.conn.request('PUT', self.path)

    def test_upload(self):
        ffname = u'tests/fixtures/school-example.xls'
        with mock.patch.object(self.conn, '_request',
                               return_value=MockResponse(200)):
            with self.assertRaises(ClientException):
                self.conn._upload('PUT', self.path, ffname, '{}')

    def test_get(self):
        with mock.patch.object(self.conn, '_request',
                               return_value=MockResponse(200)) as mock_request:
            self.conn.get(self.path)
            mock_request.assert_called_with('GET', self.url, files=None,
                                            headers=self.ua_header, data=None)

    def try_upload(self, call, method):
        ffname = u'tests/fixtures/school-example.xls'
        handle = open(ffname, 'rb')
        data = handle.read()
        handle.close()

        with mock.patch.object(self.conn, '_request',
                               return_value=MockResponse(200)) as mock_request:
            call(self.path, ffname)
            mock_request.assert_called_with(method, self.url, files=None,
                                            headers=self.ua_header, data=data)

            data = json.dumps(self.json_data)
            call(self.path, None, data)
            mock_request.assert_called_with(method, self.url, files=None,
                                            headers=self.ua_header,
                                            data=json.dumps(self.json_data))

    def test_post_upload(self):
        self.try_upload(self.conn.post, 'POST')

    def test_put_upload(self):
        self.try_upload(self.conn.put, 'PUT')
