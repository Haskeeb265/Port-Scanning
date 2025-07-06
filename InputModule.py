# InputModule.py

import socket
import ipaddress
from typing import List

# Function to get the IP address or domain from the user
def get_ip() -> str:
    ip_input = input("Enter target IP address or domain: ").strip()  # strip removes leading and trailing whitespace
    ip_resolved = is_ip_address(ip_input)  # transforming domain into IP address if a domain is provided
    if ip_resolved is None:
        print("[!] Invalid IP address or domain. Exiting.")
        exit()
    print(f"[+] Resolved IP: {ip_resolved}")
    return ip_resolved

# Function to check if the input is a valid IP address or domain name
def is_ip_address(ip_input: str):
    try:
        # Check if valid IP address
        ip_obj = ipaddress.ip_address(ip_input)
        return str(ip_obj)
    except ValueError:
        try:
            # Try resolving domain name to IP
            resolved_ip = socket.gethostbyname(ip_input)
            return resolved_ip
        except socket.gaierror:
            return None

# Function to get a list of valid target ports from the user
def get_ports() -> List[int]:
    target_port_input = input("Enter target port(s). Use commas to separate multiple ports: ").strip()
    port_list = []

    for port_str in target_port_input.split(','):
        port_str = port_str.strip()
        if not port_str.isdigit():
            print(f"Invalid port: {port_str}. Ports must be numeric.")
            continue
        port = int(port_str)
        if 0 <= port <= 65535:
            port_list.append(port)
        else:
            print(f"Invalid port: {port}. Ports must be between 0 and 65535.")
            exit()

    print(f"Valid ports: {port_list}")
    return port_list
