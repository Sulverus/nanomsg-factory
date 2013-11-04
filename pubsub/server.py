from core.base import NanoServer
from pynanomsg import SURVEYOR
from time import sleep
from datetime import datetime


class PublishSubscribeServer(NanoServer):
    """
    Pub/Sub using survey socket type
    """
    socket_type = SURVEYOR

    def __init__(self, tick=1, **kwargs):
        super(PublishSubscribeServer, self).__init__(**kwargs)
        self.tick = tick

    def server_loop(self):
        """
        Send heartbeat every tick
        """
        heartbeat = datetime.now().strftime('HEARTBEAT %Y.%m.%d-%H:%M:%S')
        self.log_msg('BROADCASTING', heartbeat)
        self.sock.send(heartbeat)
        sleep(self.tick)

if __name__ == '__main__':
    p = PublishSubscribeServer(name='pubsub_server')
    p.run()