import socket
from PacketCrafting import s, packet_crafting

def packet_transmission(ip_input: str, port_list: list[int]):
    print("[+] Starting packet transmission...")

    for port in port_list:
        packet = packet_crafting(ip_input, port)  # Craft packet for this specific port
        try:
            s.sendto(packet, (ip_input, 0))  # Send the crafted packet to the target IP (port is ignored for raw sockets)
            print(f"[+] SYN packet sent to {ip_input}:{port}")
        except PermissionError:
            print("[!] Permission denied. Run your script as administrator/root.")
            exit()
        except Exception as e:
            print(f"[!] Error sending packet to {ip_input}:{port} -> {e}")