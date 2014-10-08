from json2xlsclient.templates import Template
from json2xlsclient.utils import Connection
from json2xlsclient.xls import Xls


class Client(object):
    def __init__(self, endpoint_url):
        self.template = Template(Connection(endpoint_url))
        self.xls = Xls(Connection(endpoint_url))
