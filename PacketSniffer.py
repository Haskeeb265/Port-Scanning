import socket
import struct
import time

from scapy.all import sniff, IP, TCP

def packet_sniffer(ip_input, port_list, timeout=5):
    print("[+] Starting packet sniffer for response capture...")
    open_ports = []

    def process_packet(packet):
        if packet.haslayer(TCP) and packet.haslayer(IP):
            ip_layer = packet.getlayer(IP)
            tcp_layer = packet.getlayer(TCP)

            if ip_layer.src == ip_input and tcp_layer.sport in port_list:
                if tcp_layer.flags == "SA":  # SYN-ACK received
                    print(f"[OPEN] Port {tcp_layer.sport} is open (SYN-ACK received)")
                    open_ports.append(tcp_layer.sport)
                elif tcp_layer.flags == "RA":  # RST-ACK received
                    print(f"[CLOSED] Port {tcp_layer.sport} is closed (RST received)")

    sniff(filter=f"tcp and host {ip_input}", prn=process_packet, timeout=timeout)
    return open_ports