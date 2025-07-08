from InputModule import get_ip, get_ports
from PacketTransmission import packet_transmission
from PacketSniffer import packet_sniffer
from RSTSender import send_rst
from LoggerReporter import log_results
import time

def main():
    print("\n[+] Advanced SYN Scanner Starting...")
    ip_input = get_ip()
    port_list = get_ports()

    start_time = time.time()

    packet_transmission(ip_input, port_list)
    open_ports = packet_sniffer(ip_input, port_list, timeout=7)

    send_rst(ip_input, open_ports, source_ip='192.168.0.104')  # replace with your attacker IP

    end_time = time.time()
    scan_duration = round(end_time - start_time, 2)
    print(f"\n[+] Scan completed in {scan_duration} seconds.")

    log_results(open_ports, ip_input, scan_duration)

if __name__ == "__main__":
    main()