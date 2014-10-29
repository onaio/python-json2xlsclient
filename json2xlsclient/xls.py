class Xls():
    """ Class used to manage xls related functions. """

    def __init__(self, conn):
        self.conn = conn

    def create(self, template_token, json_data):
        """ Generates an Excel file from an existing template and JSON data.

        :param template_token: A token corresponding to an existing template.
        :param json_data: Data used to populate the template into a usable xls
        :returns: string -- a token corresponding to the generated xls file.
        """
        return self.conn.post(
            u'/xls/{}'.format(template_token), None, json_data).text

    def get(self, xls_token):
        """ Get an Excel file generated after a previous call to `create()`

        :param xls_token: A token corresponding to a generated xls file
        :returns: string -- representation of the downloaded binary - an xls
        file escaped in a mix of \\xhh notation & regular escape sequences.
        """
        return self.conn.get(
            u'/xls/{}'.format(xls_token), None).text

# TODO(james): uncomment when `PUT /xls/` gets fixed (see onaio/json-to-xls#3)
#     def update(self, xls_token, json_data):
#         """ Update a previously generated an Excel file

#         :param xls_token: A token corresponding to an existing xls file
#         :param json_data: Dataset used to populate the template into an xls.
#         :returns: string -- a token corresponding to the updated excel file.
#         """
#         return self.conn.put(
#             u'/xls/{}'.format(xls_token), None, json_data).text
