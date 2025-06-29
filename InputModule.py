import socket
import ipaddress


#Function to check if the input is a valid IP address or domain name
def is_ip_address(target_input: str):
    try:
        ip_obj = ipaddress.ip_address(target_input)
        return str(ip_obj)
    
    except ValueError:
        try:
            resolved_ip = socket.gethostbyname(target_input)
            return resolved_ip
        except socket.gaierror:
            return None
        

#Taking input from the user for target IP address or domain and port(s)

if __name__ == "__main__":

    print("Enter target IP address or domain: ")
    target_input = input().strip() # strip removes leading and trailing whitespace
    
    #Taking input from the user for target port(s) and converting them to a list of integers
    print("Enter target port(s) use commas to seperate multiple ports: ") #Taking input from the user.
    target_port_input = input().strip() # Converts target_port_input to a string and removes leading and trailing whitespace 
    port_list = [int(port.strip()) for port in target_port_input.split(',') if port.strip().isdigit()] # Splitting the input string by commas and converting each part to an integer if it's a digit
    
    # Transforming domain into IP address if a domain is provided
    is_ip_address(target_input) 
    



 