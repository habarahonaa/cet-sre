from netmiko import ConnectHandler

def connection_handler(device_type, ip, username, password, secret):
    """
    Establishes a connection to the device and returns the SSH connection object.

    Args:
        device_type (string): device type (i.e. cisco_ios) full list on netmiko's docs
        ip (string): IP address of the device to connect to
        username (string): username to use when connecting to the device
        password (string): password to use when connecting to the device
        secret (string): enable password for devices that require it
    Returns:
        net_connect: netmiko SSH connection object
    """
    device = {
        'device_type': device_type,
        'ip': ip,
        'username': username,
        'password': password,
        'secret': secret
    }
    net_connect = ConnectHandler(**device)
    return net_connect