class ApiException(Exception):

    def __init__(self, msg, resp=None):
        self.msg = msg
        if resp:
            self.api_response = resp
            self.msg = u'Http Error: {}, Reason: {}'.format(
                self.api_response.status_code, self.api_response.reason)
        Exception.__init__(self, msg)
        
    def __str__(self):
        return self.msg

class ClientException(Exception):
    pass
