from PacketCrafting import s, packet_crafting
from InputModule import ip_input, port_list

def packet_transmission():
    print("Transmitting packets...")

    for port in port_list:
        pkt = packet_crafting(ip_input, port)  # Dynamically craft the packet for this port
        s.sendto(pkt, (ip_input, 0))
