import os, re
full_results = [re.findall('^[\w\?\.]+|(?<=\s)\([\d\.]+\)|(?<=at\s)[\w\:]+', i) for i in os.popen('arp -a')]
final_results = [dict(zip(['IP', 'LAN_IP', 'MAC_ADDRESS'], i)) for i in full_results]
final_results = [{**i, **{'LAN_IP':i['LAN_IP'][1:-1]}} for i in final_results]
print(final_results)
'''
import subprocess 
  
for ping in range(1,10): 
    address = "192.168.0." + str(ping) 
    res = subprocess.call(['ping', '-c', '3', address]) 
    if res == 0: 
        print( "ping to", address, "OK") 
    elif res == 2: 
        print("no response from", address) 
    else: 
        print("ping to", address, "failed!") 
'''