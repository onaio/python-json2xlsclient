from exceptions import ApiException
import requests
from urlparse import urlparse


class Connection(object):

    def __init__(self, url, user_agent=None):
        self.url = urlparse(url)
        self.session = requests.Session()

        self.user_agent = user_agent or "python-json2xlsclient"

    def request(self, method, full_path, data=None, headers=None, files=None):
        headers = headers or {}
        headers['user-agent'] = self.user_agent

        self.last_response = self.session.request(
            method,
            u'{}://{}{}'.format(
                self.url.scheme, self.url.netloc, full_path),
            headers=headers, data=data, files=files)

        status_code = self.last_response.status_code

        if status_code < 200 or status_code >= 300:
            raise ApiException(None, self.last_response)

        return self.last_response

    def get(self, path, headers=None):
        return self.request('GET', path)

    def post(self, path, headers=None, data=None, files=None):
        return self.request('POST', path, data, headers)

    def put(self, path, headers=None, data=None, files=None):
        return self.request('PUT', path, data, headers)

    def delete(self, path, headers=None):
        return self.request('DELETE', path)
