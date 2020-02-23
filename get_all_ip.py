import netifaces

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
print(broadcast_value())
print(netmask_value())
print(gateway()[0])
print(get_machine_ips()[2])