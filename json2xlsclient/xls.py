class Xls():

    def __init__(self, conn):
        self.conn = conn

    def create(self, template_token, json_data):
        return self.conn.post(
            u'/xls/{}'.format(template_token), None, json_data).text

    def get(self, xls_token):
        return self.conn.get(
            u'/xls/{}'.format(xls_token), None).text

    def update(self, xls_token, json_data):
        return self.conn.put(
            u'/xls/{}'.format(xls_token), None, json_data).text
