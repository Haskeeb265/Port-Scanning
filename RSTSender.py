from scapy.all import IP, TCP, send

def send_rst(ip_input, open_ports, source_ip):
    print("[+] Sending RST packets to gracefully terminate connections...")
    for port in open_ports:
        rst_pkt = IP(dst=ip_input, src=source_ip)/TCP(dport=port, flags="R", seq=1, ack=1)
        send(rst_pkt, verbose=0)
        print(f"[+] Sent RST to {ip_input}:{port}")