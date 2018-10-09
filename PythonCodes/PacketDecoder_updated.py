import socket, struct, os, array

class IPSniff:
 
    def __init__(self, interface_name, on_ip_incoming, on_ip_outgoing):
 
        self.interface_name = interface_name
        self.on_ip_incoming = on_ip_incoming
        self.on_ip_outgoing = on_ip_outgoing
 
        # The raw in (listen) socket is a L2 raw socket that listens
        # for all packets going through a specific interface.
        self.ins = socket.socket(
            socket.AF_PACKET, socket.SOCK_RAW, socket.htons(65535))
        self.ins.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 2**30)
        self.ins.bind((self.interface_name, 3))
 
    def __process_ipframe(self, pkt_type, ip_header, payload):
 
        # Extract the 20 bytes IP header, ignoring the IP options
        fields = struct.unpack("!BBHHHBBHII", ip_header)
 
        dummy_hdrlen = fields[0] & 0xf
        iplen = fields[2]
 
        ip_src = payload[12:16]
        ip_dst = payload[16:20]
        port_src = payload[20:22]
        port_dst = payload[22:24]
        ip_frame = payload[0:iplen]
 
        if pkt_type == socket.PACKET_OUTGOING:
            if self.on_ip_outgoing is not None:
                self.on_ip_outgoing(ip_src, port_src, ip_dst, port_dst, ip_frame)
 
        else:
            if self.on_ip_incoming is not None:
                self.on_ip_incoming(ip_src, port_src, ip_dst, port_dst, ip_frame)
 
    def recv(self):
        while True:
 
            pkt, sa_ll = self.ins.recvfrom(65535)
 
            if type == socket.PACKET_OUTGOING and self.on_ip_outgoing is None:
                continue
            elif self.on_ip_outgoing is None:
                continue
 
            if len(pkt) <= 0:
                break
 
            eth_header = struct.unpack("!6s6sH", pkt[0:14])
 
            dummy_eth_protocol = socket.ntohs(eth_header[2])
 
            if eth_header[2] != 0x800 :
                continue
 
            ip_header = pkt[14:34]
            payload = pkt[14:]
 
            self.__process_ipframe(sa_ll[2], ip_header, payload)
 
#code to use IPSniff
def test_incoming_callback(src, port_src, dst, port_dst, frame):
    print("incoming - src=%s:%s, dst=%s:%s, frame len = %d"
        %(socket.inet_ntoa(src), struct.unpack('!H', port_src)[0], socket.inet_ntoa(dst), struct.unpack('!H', port_dst)[0], len(frame)))
 
def test_outgoing_callback(src, port_src, dst, port_dst, frame):
    print("outgoing - src=%s:%s, dst=%s:%s, frame len = %d"
        %(socket.inet_ntoa(src), struct.unpack('!H', port_src)[0], socket.inet_ntoa(dst), struct.unpack('!H', port_dst)[0], len(frame)))


# ********************* Main *******************************************************

networkInterface = input('Enter the network interface:') 
ip_sniff = IPSniff(networkInterface, test_incoming_callback, test_outgoing_callback)
ip_sniff.recv()
