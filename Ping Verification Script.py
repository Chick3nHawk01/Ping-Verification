import os

ip_list = [] #state the ip addresses you want to ping
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        print(f"UP {ip} Ping Successful")
    else:
        print(f"DOWN {ip} Ping Unsuccessful")
