from pynanomsg import Domain, AF_SP, REQ, REQ_RESEND_IVL, PUSH, RESPONDENT
from datetime import datetime


class NanoServerException(Exception):
    pass


class NanoServer(object):
    """
    Common server class
    """
    domain_type = AF_SP
    socket_type = None

    def __init__(self, address='127.0.0.1', port=8888, name='server', protocol='tcp'):
        self.addr = address
        self.port = port
        self.domain = None
        self.sock = None
        self.node_name = name
        self.protocol = protocol

    def init_server(self, d_type, s_type):
        if self.socket_type is None:
            raise NanoServerException('Socket type is not specified')
        self.domain = Domain(d_type)
        self.sock = self.domain.socket(s_type)
        if self.port is not None:
            server_addr = '%s://%s:%d' % (self.protocol, self.addr, self.port)
        else:
            server_addr = '%s:///tmp/%s.ipc' % (self.protocol, self.node_name)
        self.log_msg('INIT in %s' % server_addr)

        return self.sock.bind(server_addr)

    def log_msg(self, action, data=''):
        print "[%s]: %s %s %s" % (
            datetime.now().strftime('%Y.%m.%d-%H:%M'),
            self.node_name, action, data
        )

    def server_loop(self):
        raise NotImplementedError

    def run(self):
        if self.sock is None or self.domain is None:
            self.init_server(self.domain_type, self.socket_type)
        state = ''
        while state != 'shut_down':
            state = self.server_loop()


class NanoClient(object):
    """
    Common client class
    """
    domain_type = AF_SP
    socket_type = None

    def __init__(self, address='127.0.0.1', port=8888, protocol='tcp'):
        self.addr = address
        self.port = port
        self.protocol = protocol
        self.domain = None
        self.sock = None

        self.create_client()

    def set_socket_options(self):
        pass

    def create_client(self):
        self.domain = Domain(self.domain_type)
        self.sock = self.domain.socket(self.socket_type)
        self.set_socket_options()

        address = '%s://%s:%d' % (self.protocol, self.addr, self.port)
        self.sock.connect(address)

    def action(self, msg=None):
        raise NotImplementedError