# PacketCrafting.py

import socket
import struct
import random

# Create a raw socket for crafting custom IP packets
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)  # AF_INET = IPv4, SOCK_RAW = raw socket, IPPROTO_RAW = custom IP header

# Checksum function implementing RFC 1071 Internet Checksum
def checksum(data):  # This function allows the receiver to verify the integrity of the TCP segment.
    if len(data) % 2 != 0:  # If the length of the data is odd, we need to pad it with a null byte
        data += b'\0'  # Padding with a null byte if the length is odd
    res = 0  # Initialize the result to 0
    for i in range(0, len(data), 2):  # Iterating through the data in 2-byte chunks
        w = (data[i] << 8) + data[i + 1]  # First byte is shifted left by 8 bits and added to the second byte to create a 16-bit word
        res += w  # Storing the sum of the 16-bit words in the result
    res = (res >> 16) + (res & 0xffff)  # Add overflow bits to the lower 16 bits
    res = res + (res >> 16)  # Add carry if needed
    return ~res & 0xffff  # Return the one's complement as the checksum

# Function to craft the SYN packet
def packet_crafting(ip_input: str, port: int) -> bytes:
    print(f"Crafting packet for {ip_input}:{port}...")  # Indicating that the packet is being crafted
    source_ip = '192.168.0.104'
    dest_ip = ip_input  # Destination IP address from user input

    # Constructing IP Header:
    ip_ver = 4  # Indicates that we're using IPv4
    ip_ihl = 5  # Header Length 5 (minimum header length size)
    ip_tos = 0  # Used to indicate priority/quality of flags in routing (0 for standard packets)
    ip_tot_len = 20 + 20  # IP header (20 bytes) + TCP header (20 bytes) = 40 bytes total
    ip_id = random.randint(0, 65535)  # Random ID helps when reassembling fragments of packets
    ip_frag_off = 0  # Fragment offset (0 = unfragmented)
    ip_ttl = 225  # Time to live so that the packet doesn't circulate infinitely in case of a routing loop
    ip_proto = socket.IPPROTO_TCP  # TCP as the upper-layer protocol
    ip_check = 0  # Header checksum left as 0 (calculated by OS if required)
    ip_srcaddr = socket.inet_aton(source_ip)  # Convert source IP to 4-byte binary format
    ip_destaddr = socket.inet_aton(dest_ip)  # Convert destination IP to 4-byte binary format

    ip_ihl_ver = (ip_ver << 4) + ip_ihl  # Combining IP version and header length into a single byte

    # Packing the IP header fields into a binary structure
    ip_header = struct.pack(
        '!BBHHHBBH4s4s',
        ip_ihl_ver, ip_tos, ip_tot_len, ip_id,
        ip_frag_off, ip_ttl, ip_proto, ip_check,
        ip_srcaddr, ip_destaddr
    )

    # Constructing TCP Header:
    port_srcaddr = random.randint(1024, 65535)  # Random high port
    port_destaddr = port  # Destination port from user input
    seq = 0  # For SYN scan
    ack_seq = 0  # No ACK yet
    doff = 5  # Data offset (5 * 4 = 20 bytes, no options)

    # TCP Flags
    fin = 0
    syn = 1  # SYN flag set to initiate the connection
    rst = 0
    psh_flag = 0
    ack = 0
    urg = 0

    tcp_flags = fin + (syn << 1) + (rst << 2) + (psh_flag << 3) + (ack << 4) + (urg << 5)  # Creating the flags byte

    window = socket.htons(5840)  # Maximum window size, converted to network byte order
    check = 0  # Checksum will be calculated later
    urg_ptr = 0  # Urgent pointer is 0 (no urgent data)

    # Pack the initial TCP header with a zero checksum
    tcp_header = struct.pack(
        '!HHLLBBHHH',
        port_srcaddr, port_destaddr, seq, ack_seq,
        doff << 4, tcp_flags, window, check, urg_ptr
    )

    # Creating pseudo-header for checksum calculation
    placeholder = 0  # Placeholder for checksum calculation
    protocol = socket.IPPROTO_TCP  # TCP protocol number
    tcp_length = len(tcp_header)  # Length of TCP header

    # Packing the pseudo-header
    psh = struct.pack(
        '!4s4sBBH',
        ip_srcaddr, ip_destaddr, placeholder, protocol, tcp_length
    ) + tcp_header

    tcp_check = checksum(psh)  # Calculating TCP checksum using pseudo-header

    # Pack the final TCP header with the correct checksum
    tcp_header = struct.pack(
        '!HHLLBBHHH',
        port_srcaddr, port_destaddr, seq, ack_seq,
        doff << 4, tcp_flags, window, tcp_check, urg_ptr
    )

    # Final packet: IP header + TCP header
    packet = ip_header + tcp_header
    return packet  # Returning the crafted SYN packet
