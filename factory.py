from pipeline.server import PipeServer
from pipeline.client import PipeClient
from reqrep.server import RequestReplayServer
from reqrep.client import RRClient
from pubsub.server import PublishSubscribeServer
from pubsub.client import PubSubClient

from bus.node import BusNode


class FactoryException(Exception):
    """
    Used in mode selection
    """
    pass


class NanoFactory(object):
    """
    Common factory class
    """
    entities = None

    def __init__(self, mode, **kwargs):
        if mode not in self.entities.keys():
            raise FactoryException('Unknown mode')

        self.entity = self.entities[mode](**kwargs)

    def run(self):
        raise NotImplementedError


class ServerFactory(NanoFactory):
    """
    Simple factory for pipeline, request/replay,
    publish/subscribe and bus nodes
    """
    entities = {
        'pipe': PipeServer,
        'reqrep': RequestReplayServer,
        'pubsup': PublishSubscribeServer,
        'bus': BusNode
    }

    def __init__(self, mode, **kwargs):
        """
        Init server in one of 4 modes or raise exception
        """
        if 'name' not in kwargs:
            kwargs['name'] = '%s_server' % mode

        super(ServerFactory, self).__init__(mode, **kwargs)

    def run(self):
        """
        Run server loop
        """
        self.entity.run()


class ClientFactory(NanoFactory):
    entities = {
        'pipe': PipeClient,
        'reqrep': RRClient,
        'pubsup': PubSubClient,
    }

    def run(self, **kwargs):
        """
        Do client action
        """
        self.entity.action(**kwargs)