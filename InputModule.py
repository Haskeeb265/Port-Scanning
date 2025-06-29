print("Enter target IP address or domain: ")
target_input = input().strip() # strip removes leading and trailing whitespace

print("Enter target port(s): ")
target_port_input = input().strip()
port_list = [int(port.strip()) for port in target_port_input.plsit(',') if port.strip().isdigit()]
 