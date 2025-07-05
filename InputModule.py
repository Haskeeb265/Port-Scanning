import socket
import ipaddress


#Function to check if the input is a valid IP address or domain name
def is_ip_address(ip_input: str):
    
    try:
        ip_obj = ipaddress.ip_address(ip_input)
        return str(ip_obj)
    
    except ValueError:
        try:
            resolved_ip = socket.gethostbyname(ip_input)
            return resolved_ip
        except socket.gaierror:
            return None


def get_ports() -> list[int]:
    
    target_port_input = input("Enter target port(s). Use commans to separate multiple ports: ").strip()
    port_list = []

    for port_str in target_port_input.split(','):
        port_str = port_str.strip()
        if not port_str.isdigit():
            print(f"Invalid port: {port_str}. Ports must be numeric.")
            continue
        port = int(port_str)
        if 0<= port <=65535:
            port_list.append(port)
        else:
            print(f"Invalid port: {port}. Ports must be between 0 and 65535.")
            exit()

    print(f"Valid ports: {port_list}")
    return port_list        

# Taking input from the user for target IP address or domain and port(s)

if __name__ == "__main__":

    print("Enter target IP address or domain: ")
    ip_input = input().strip() # strip removes leading and trailing whitespace
    ip_input = is_ip_address(ip_input) # transforming domain into IP address if a domain is provided 
    
    print(f"Target IP address: {ip_input}")
    port_list = get_ports() # getting the list of ports from the user





 