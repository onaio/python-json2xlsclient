class Template(object):

    def __init__(self, conn):
        self.conn = conn

    def create(self, template_path):
        return self.conn.post(
            u'/templates/', template_path).text

    def get(self, template_token):
        return self.conn.get(
            u'/templates/{}'.format(template_token)).text

    def update(self, template_token, template_path):
        return self.conn.put(
            u'/templates/{}'.format(template_token), template_path).text
