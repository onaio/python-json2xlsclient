from json2xlsclient.exceptions import ApiException
from json2xlsclient.exceptions import ClientException
import requests
from future.moves.urllib.parse import urlparse


class Connection(object):

    def __init__(self, url, user_agent=None):
        self.url = urlparse(url)

        if self.url.scheme not in ['http', 'https']:
            raise ClientException(
                u'{} protocol is not supported'.format(self.url.scheme))

        self.session = requests.Session()

        self.user_agent = user_agent or "python-json2xlsclient"
        self.last_response = None

    def _request(self, *args, **kwargs):
        return self.session.request(*args, **kwargs)

    def request(self, method, path, data=None, headers=None, files=None):
        headers = headers or {}
        headers['user-agent'] = self.user_agent

        if not path.startswith('/'):
            path = u'/{}'.format(path)

        self.last_response = self._request(
            method,
            u'{}://{}{}'.format(
                self.url.scheme, self.url.netloc, path),
            headers=headers, data=data, files=files)

        status_code = self.last_response.status_code

        if status_code < 200 or status_code >= 300:
            raise ApiException(self.last_response)

        return self.last_response

    def get(self, path, headers=None):
        return self.request('GET', path, headers)

    def post(self, url_path, file_path=None, payload=None, headers=None):
        return self._upload('POST', url_path, file_path, payload, headers)

    def put(self, url_path, file_path=None, payload=None, headers=None):
        return self._upload('PUT', url_path, file_path, payload, headers)

    def delete(self, path, headers=None):
        return self.request('DELETE', path)

    def _upload(self, method, url_path, file_path=None,
                payload=None, headers=None):

        if not (file_path is None) ^ (payload is None):
            raise ClientException(u'You must provide a file_path or payload '
                                  'for upload. They are mutually exclusive!')
        if method not in ['POST', 'PUT']:
            raise ClientException(u'method arg must either be a POST or PUT!')

        data = payload
        if file_path is not None:
            file_data = open(file_path, 'rb')
            data = file_data.read()
            file_data.close()

        return self.request(method, url_path, data, headers)
