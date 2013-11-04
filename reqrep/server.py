from core.base import NanoServer
from pynanomsg import REP
from datetime import datetime


class RequestReplayServer(NanoServer):
    """
    Request/Reply (I ask, you answer)
    """
    socket_type = REP

    def server_loop(self):
        """
        Receive msg and process date request
        """
        msg = self.sock.recv(32)
        self.log_msg('RECEIVED', msg)
        response = 'ONLY DATE REQUESTS'
        if msg.lower() == 'date':
            response = datetime.now().strftime('%Y.%m.%d-%H:%M')
        self.sock.send(response)
        return msg


if __name__ == '__main__':
    p = RequestReplayServer(name='rr_server')
    p.run()