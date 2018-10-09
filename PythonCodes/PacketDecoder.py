# Packet sniffer in python
# For Linux - Sniffs all incoming and outgoing packets :)

import socket, sys
from struct import *
import struct
import fcntl

# Convert a string of 6 characters of ethernet address into a dash separated hex string
def eth_addr(a):
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]), ord(a[1]), ord(a[2]), ord(a[3]), ord(a[4]), ord(a[5]))
    return b

# create a AF_PACKET type raw socket (thats basically packet level)
# define ETH_P_ALL 0x0003 /*Every packet (be careful!!!)*/
try:
    #s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, 25, str("wlo1" + '\0').encode('utf-8'))
    
except socket.error as msg:
    print('Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

# receive a packet
while True:
    packet = s.recvfrom(65565)

    #conn, addr = s.accept()
    #packet = conn.recv(65565) 

    # packet string from tuple
    packet = packet[0]

    # parse ethernet header
    eth_length  = 14
    eth_header  = packet[:eth_length]
    eth         = unpack('!6s6sH', eth_header)
    eth_protocol= socket.ntohs(eth[2])
    print('Destination MAC:' + eth_addr(str(bytearray(packet[0:6]))) + ' Source MAC:' + eth_addr(str(bytearray(packet[6:12]))) + 
          ' Protocol:' + str(eth_protocol))

    # Parse IP packets, IP Protocol number = 8
    if eth_protocol == 8:
        # Parse IP header
        # take first 20 characters for the ip header
        ip_header = packet[eth_length:20 + eth_length]

        # now unpack them :)
        iph = unpack('!BBHHHBBH4s4s', ip_header)

        version_ihl = iph[0]
        version     = version_ihl >> 4
        ihl         = version_ihl & 0xF
        iph_length  = ihl * 4

        protocol    = iph[6]
        s_addr      = socket.inet_ntoa(iph[8]);
        d_addr      = socket.inet_ntoa(iph[9]);

        print('Protocol:' + str(protocol) + ' Source Address:' + str(s_addr) + ' Destination Address:' + str(d_addr))

        # TCP protocol
        if protocol == 6:
            t = iph_length + eth_length
            tcp_header = packet[t:t + 20]

            # now unpack them
            tcph = unpack('!HHLLBBHHH', tcp_header)
            source_port = tcph[0]
            dest_port = tcph[1]

            print('Source Port:' + str(source_port) + ' Dest Port:' + str(dest_port))

        # ICMP Packets
        elif protocol == 1:
            u = iph_length + eth_length
            icmph_length = 4
            icmp_header = packet[u:u + 4]

            # now unpack them :)
            icmph = unpack('!BBH', icmp_header)

            icmp_type = icmph[0]
            code = icmph[1]

            print('Type:' + str(icmp_type) + ' Code:' + str(code))

        # UDP packets
        elif protocol == 17:
            u = iph_length + eth_length
            udph_length = 8
            udp_header = packet[u:u + 8]

            # now unpack them :)
            udph = unpack('!HHHH', udp_header)

            source_port = udph[0]
            dest_port = udph[1]
            length = udph[2]

            print('Source Port:' + str(source_port) + ' Dest Port:' + str(dest_port) + ' Length:' + str(length))

        # some other IP packet like IGMP
        else:
            print('Protocol other than TCP/UDP/ICMP')
