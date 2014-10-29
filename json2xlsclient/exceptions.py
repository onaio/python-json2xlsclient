class ExceptionMixin(object):
    """ Mixin containing common exception functionality. """

    def msg_init(self, msg, resp=None):
        self.msg = msg
        if resp is not None:
            self.api_response = resp
            self.msg = u'Api Error: {}, {}'.format(
                self.api_response.status_code, self.api_response.reason)
        self.api_response = resp
        Exception.__init__(self, msg)

    def __str__(self):
        return self.msg


class ApiException(Exception, ExceptionMixin):
    """ Exception class riased for 500 series REST Api replies. """

    def __init__(self, resp):
        self.msg_init(None, resp)


class ClientException(Exception, ExceptionMixin):
    """ Exception class riased when errors occur on the client's part.

        This includes 400 series REST Api replies.
    """
    def __init__(self, msg, resp=None):
        self.msg_init(msg, resp)
