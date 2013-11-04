from core.base import NanoServer
from pynanomsg import PULL


class PipeServer(NanoServer):
    """
    Pipeline (A One-Way Pipe) server
    """
    socket_type = PULL

    def server_loop(self):
        msg = self.sock.recv(32)
        self.log_msg('RECEIVED', msg)
        return msg


if __name__ == '__main__':
    p = PipeServer(name='pipe_server')
    p.run()