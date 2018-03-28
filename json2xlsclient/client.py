from builtins import object

from json2xlsclient.templates import Template
from json2xlsclient.utils import Connection
from json2xlsclient.xls import Xls


class Client(object):
    """ Convenience class used to "collect" all client library functions. """

    def __init__(self, endpoint_url):
        self.template = Template(Connection(endpoint_url))
        self.xls = Xls(Connection(endpoint_url))
