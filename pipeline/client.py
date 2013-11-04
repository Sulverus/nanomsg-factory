from core.base import NanoClient, PUSH


class PipeClient(NanoClient):
    """
    Pipeline client
    """
    socket_type = PUSH

    def action(self, msg=None):
        self.sock.send(msg)
        print 'msg pushed out'