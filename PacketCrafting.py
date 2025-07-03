import socket
import struct
import random
from InputModule import target_input, port_input

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW) #AF_INET = Indicating IPv4. SOCKET_RAW = indicating a raw socket, IPPROTO_RAW = indicating that we will construct the IP packet header ourselves.


source_ip = '192.168.0.104'
dest_ip = target_input

# Constructing the header of the packet:
ip_ver = 4 # Indicates that we're using IPv'4'.
ip_ihl = 5 # Header Length 5. 5 is mimimum header length size.
ip_tos = 0 # Used to indicate priority/quality of flags in routing. We're creating standard packets so the value of tos is 0.
ip_tot_len = 20 + 20 # IP header = 20 + TCP header 20 = 40 bytes. This is the total length of the entire IP packet
ip_id = random.randint(0, 65535) # Random ID in the range of the available ports. This helps when reassembling the fragments of the packets.
ip_frag_off = 0 # IP fragment offset tells where the packet fragment belongs to. Since this is an unfragmented packet, the offset is set to 0 Don't Fragment(DF).

 





