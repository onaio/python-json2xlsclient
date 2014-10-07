class ApiException(Exception):

    def __init__(self, msg, resp=None):
        self.msg = msg
        if resp is not None:
            self.api_response = resp
            self.msg = u'Api Error: {}, {}'.format(
                self.api_response.status_code, self.api_response.reason)
        self.api_response = resp
        Exception.__init__(self, msg)

    def __str__(self):
        return self.msg


class ClientException(Exception):
    pass
