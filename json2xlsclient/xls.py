from json2xlsclient.exceptions import ClientException


class Xls(object):

    def __init__(self, conn=None):
        if not conn:
            raise ClientException(u'I need a connection object')
        self.conn = conn

    def _generate_xls(self, token, path, method='POST'):
        data = open(path, 'rb')
        if method == 'PUT':
            resp = self.conn.put(u'/xls/{}'.format(token), None, data.read())
        else:
            resp = self.conn.post(u'/xls/{}'.format(token), None, data.read())

        if type(data) is file:
            data.close()

        return resp.text

    def create(self, token, json_data):
        return self._generate_xls(json_data, token)

    def get_xls(self, token):
        resp = self.conn.get(u'/xls/{}'.format(token), None)
        return resp.text

    def regenerate_xls(self, token, json_data):
        return self._generate_xls(json_data, token, method='PUT')