from json2xlsclient.exceptions import ClientException


class Templates(object):

    def __init__(self, conn=None):
        if not conn:
            raise ClientException(u'I need a connection object')
        self.conn = conn

    def _upload_template(self, path, token=None):
        data = open(path, 'rb')
        resp = self.conn.put(u'/templates/{}'.format(token), None, data.read()) \
            if token else \
            self.conn.post(u'/templates', None, data.read())

        if type(data) is file:
            data.close()

        return resp.text

    def create(self, template_path):
        return self._upload_template(template_path)

    def get(self, token):
        resp = self.conn.get(u'/templates/{}'.format(token), None)
        return resp.text

    def update(self, token, template_path):
        return self._upload_template(template_path, token)
