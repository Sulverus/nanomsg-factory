from core.base import NanoServer, Domain
from pynanomsg import BUS, SOL_SOCKET, RCVTIMEO
from time import sleep
import sys


class BusNode(NanoServer):
    """
    Bus (Routing)
    """
    socket_type = BUS

    def __init__(self, nodes, **kwargs):
        """
        Nodes fields added to base class
        """
        super(BusNode, self).__init__(**kwargs)
        self.nodes = nodes

    def server_loop(self):
        msg = self.sock.recv(32)
        self.log_msg('RECEIVED', msg)
        return msg

    def connect_nodes(self):
        """
        Connect other nodes and send online notification
        """
        for bus_node in self.nodes:
            self.sock.connect(bus_node)
        sleep(1)
        self.sock.send('%s is online' % self.node_name)

    def init_server(self, d_type, s_type):
        """
        Init as inp and connect other nodes
        """
        bind = super(BusNode, self).init_server(d_type, s_type)
        if not len(self.nodes):
            return bind
        self.connect_nodes()
        return bind


if __name__ == '__main__':
    node_name = 'bus_node%s' % sys.argv[1]
    p = BusNode(nodes=sys.argv[2:], name=node_name, port=None, protocol='ipc')
    p.run()