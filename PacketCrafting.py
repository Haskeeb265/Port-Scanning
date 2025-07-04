import socket
import struct
import random
from InputModule import target_input, port_input

# Create a raw socket for crafting custom IP packets
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW) # AF_INET = IPv4, SOCK_RAW = raw socket, IPPROTO_RAW = custom IP header

source_ip = '192.168.0.104'
dest_ip = target_input  # Destination IP address from user input

# Constructing IP Header:
ip_ver = 4 # Indicates that we're using IPv'4'.
ip_ihl = 5 # Header Length 5. 5 is minimum header length size.
ip_tos = 0 # Used to indicate priority/quality of flags in routing. We're creating standard packets so the value of tos is 0.
ip_tot_len = 20 + 20 # IP header = 20 + TCP header 20 = 40 bytes. This is the total length of the entire IP packet
ip_id = random.randint(0, 65535) # Random ID in the range of the available ports. This helps when reassembling the fragments of the packets.
ip_frag_off = 0 # IP fragment offset tells where the packet fragment belongs to. Since this is an unfragmented packet, the offset is set to 0 Don't Fragment(DF).
ip_ttl = 225 # Time to live is set to 225 so that incae of routing loop the packet doesn't circulate infinitely. Set to maximum
ip_proto = socket.IPPROTO_TCP # Using TCP as an upper layer protocol in our packet
ip_check = 0 # Leaving header checksum as 0. OS and NIC (Network interface Card) will compute it if required.
ip_srcaddr = socket.inet_aton(source_ip) # Converting IP address into a 4 byte binary format
ip_destaddr = socket.inet_aton(dest_ip) # Converting IP address into a 4 byte binary format

ip_ihl_ver = (ip_ver << 4) + ip_ihl # Packets IP header length and IP version into a single 8 bit field for the first byte of the header. In this line of code we're left shifting the ip_ver hence 4 in binary will become 0100 and upon 4 bit left shift, it would become 0100 0000. Then we add the header length which is 5 into the left shifted value. 5 in binary would become 0101. 0100 + 0101 = 0100 0101. This indicates Version = 4 and Header length = 5. This line of code is important because without it you would violate the header format and the destination would drop this packet.

# Packing the IP header fields into a binary structure
ip_header = struct.pack('!BBHHHBBH4s4s', ip_ihl_ver, ip_tos, ip_tot_len, ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check, ip_srcaddr, ip_destaddr) # Packing the IP header

# Constructing TCP Header:
port_srcaddr = random.randint(1024, 65535) # Randomizing a high port
port_destaddr = port_input  # Destination port from user input
seq = 0 # Set to 0 for SYN scan
ack_seq = 0 # Set to 0 because we're initiating the connnection but haven't recieved data. ACK is used to 
doff = 5 # Indicates size of the TCP header. For now we're keeping it to the minimum value.

# TCP Flags
fin = 0 # Terminates the connection (indicates no more data from the sender)
syn = 1 # Initiating the connection
rst = 0 # Reset the connection
psh = 0 # Push function
ack = 0 # Acknowledgment field significant
urg = 0 # Urgent pointer field significant. All of the other flags remain 0 because in SYN we only want to initiate the connection and not complete the handshake.

tcp_flags = fin + (syn << 1) + (rst << 2) + (psh << 3) + (ack << 4) + (urg << 5) # Creating a single byte for TCP flags by combining the individual flags using bitwise operations. Each flag is shifted to its respective position in the byte.

window = socket.htons(5840) # Window size is set to 5840. This is the size of the TCP window which indicates how much data can be sent before an acknowledgment is required. Here 5840 is a common default value used in TCP connections.
check = 0 # Leaving TCP header checksum as 0. OS and NIC (Network interface Card) will compute it if required.
urg_ptr = 0 # Urgent pointer is set to 0 because we're not using urgent data in this packet.

tcp_header = struct.pack(' !HHLLBBHHH', port_srcaddr, port_destaddr, seq, ack_seq, doff << 4, tcp_flags, window, check, urg_ptr) # Packing the TCP header fields into a binary structure. The doff is left shifted by 4 bits to make space for the flags in the first byte of the TCP header. The !HHHLLBBHHH indicates the format of the TCP header fields.

# Creating Psuedo Header: