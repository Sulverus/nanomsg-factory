from core.base import NanoClient, REQ, REQ_RESEND_IVL


class RRClient(NanoClient):
    """
    Request/Reply client
    """
    socket_type = REQ

    def set_socket_options(self):
        self.sock.setsockopt(REQ, REQ_RESEND_IVL, 1000)

    def action(self, msg=None):
        self.sock.send(msg)
        print self.sock.recv(32)
        print 'msg pushed out'