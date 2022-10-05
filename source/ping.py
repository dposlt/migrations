# Python3 code to display hostname and
# IP address

# Importing socket library
import socket
from source import colors


# Function to display hostname and
# IP address
def get_Host_name_IP(host):
    try:
        host_name = host
        host_ip = socket.gethostbyname(host_name)
        #print("Hostname :  ", host_name)
        #print("IP : ", host_ip)
        if host_ip:
            return True
    except:
        print(colors.red(f"Unable to get {host}"))
        quit()
    # Driver code


get_Host_name_IP('hostname')  # Function call
