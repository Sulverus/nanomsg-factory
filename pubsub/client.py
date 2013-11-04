from core.base import NanoClient, RESPONDENT


class PubSubClient(NanoClient):
    """
    Publish/subscribe client
    """
    socket_type = RESPONDENT

    def action(self, msg=None):
        status = ''
        while status != 'shut_down':
            status = self.sock.recv(32)
            print 'BROADCAST RECEIVED: %s' % status