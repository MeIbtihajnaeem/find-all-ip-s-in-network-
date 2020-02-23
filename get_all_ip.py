import netifaces
import subprocess 
import ipaddress

def get_machine_ips():
    """Get the machine's ip addresses

    :returns: list of Strings of ip addresses
    """
    addresses = []
    for interface in netifaces.interfaces():
        try:
            iface_data = netifaces.ifaddresses(interface)
            for family in iface_data:
                if family not in (netifaces.AF_INET, netifaces.AF_INET6):
                    continue
                for address in iface_data[family]:
                    addr = address['addr']

                    # If we have an ipv6 address remove the
                    # %ether_interface at the end
                    if family == netifaces.AF_INET6:
                        addr = addr.split('%')[0]
                    addresses.append(addr)
        except ValueError:
            pass
    return addresses 
def gateway():
    gws = netifaces.gateways()
    return (gws['default'][netifaces.AF_INET])
def netmask_value():
    addr = netifaces.ifaddresses('wlo1')
    return addr[netifaces.AF_INET][0]["netmask"]
def broadcast_value():
    addr = netifaces.ifaddresses('wlo1')
    return addr[netifaces.AF_INET][0]["broadcast"]
def all_possible_ips():
    net4 = ipaddress.ip_network('192.168.0.0/24')
    net4.num_addresses
    var = []
    all_ping_ip_address = []
    for address in net4.hosts():
        var.append(str(address))
    print(var)
    if(get_machine_ips()[2] in var):
        last_digits = str(get_machine_ips()[2]).split(".")
        mid_point = int(last_digits[-1])
        if(mid_point>=200):
            mid = var.index("192.168.0.200")
        elif(mid_point>=100):
            mid = var.index("192.168.0.100")
        elif(mid_point>=1 and mid_point<=99):
            mid = var.index("192.168.0.1")
        count = 10
        flag = True
        while(count<=10):
            flag = ping_ip(str(var[mid]))
            if(flag==True):
                all_ping_ip_address.append(var[mid])
                count = 0 
            else:
                count=count+1
            mid = mid+1
    return all_ping_ip_address
        

        
def ping_ip(address):
    if(str(address)!= str(gateway()[0])):
            res = subprocess.call(['ping', '-c', '1', str(address)])
            if res == 0:
                return True
            else :
                return False
    else:
        return False    
print(broadcast_value())
print(netmask_value())
print(gateway()[0])
print(get_machine_ips()[2])
print(all_possible_ips())

