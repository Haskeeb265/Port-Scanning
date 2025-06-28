This is a port scanner coded for educational purposes.

Here's what's going under the hood:

FLOW OF LOGIC:
1. Input: 
    Accept target IP from the user

2. SYN Packet Crafting:
    For each target port create:
        - TCP SYN Packet with: 
            . Source IP and ephemeral source port
            . Destination IP & target port
            . TCP flags = SYN

3. Send Packets:
    Send crafted SYN packets using raw sockets or scapy.

4. Sniff Response:
    Listen for incoming packets:
     - If SYN + ACK recieved = port is open
     - If RST received = port is closed
     - If no response = host is down

5. Send RST:
    If SYN + ACK is recieved, immediately send RST packet to avoid a full handshake.

6. Log Results:
    Store port status for later reference

7. Exit:
    Clean up sockets/sniffers
    Present final report of open/closed/filtered ports


MODULES:

1. Input:
    Parse Input and validate IP addresses/domains

2. Packet Crafter:
    I will be using socket + struct instead of scapy since this project is for my own learning purposes and I intend on learning what goes under the hood.

3. Packet Sender:
    Sends crafted SYN packets to each port. We can use multithreading to scan faster.

4. Packet Sniffer:
    Capture response using raw sockets
    Filter packets

5. Reponse Analyzer:
    Analyze packets (recieved) and handle timeouts for each port scan.

6. RST Sender:
    Send RST is SYN + ACK was detected to terminate handshake quickly

7. Logger and Reporter
    Print live scanning results.
    Generate Summary of scan duration, open and closed ports.
