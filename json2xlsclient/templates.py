class Template(object):
    """ Class used to "contain" template related functions. """

    def __init__(self, conn):
        self.conn = conn

    def create(self, template_path=None, template_file=None):
        """ Creates a template used to generate xls files.

        :param template_path: Path to the template file to upload.
        :param template_file: File object of the file to be uploaded.
        :returns: string -- a token corresponding to the newly created template
        """
        payload = template_file.read() if template_file else None

        return self.conn.post(
            u'/templates/', template_path, payload).text

    def get(self, template_token):
        """ Downloads a template for a given token

        :param template_token: A token corresponding to an existing template.
        :returns: string -- string representation of the downloaded binary
        template data escaped in a mix of \\xhh notation and escape sequences.
        """
        return self.conn.get(
            u'/templates/{}'.format(template_token)).text

    def update(self, template_token, template_path):
        """ Update exsisting template from a given token

        :param template_token: A token corresponding to an existing template.
        :param template_path: Path to the replacement template file to upload.
        :returns: string -- a token corresponding to the updated template.
        """
        return self.conn.put(
            u'/templates/{}'.format(template_token), template_path).text
