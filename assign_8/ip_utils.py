
def ip_to_binary(ip_address: str) -> str:
    octets = ip_address.split(".")
    binary_str = "".join(f"{int(octet):08b}" for octet in octets)
    return binary_str


def get_network_prefix(ip_cidr: str) -> str:
    ip, prefix_length = ip_cidr.split("/")
    prefix_length = int(prefix_length)
    ip_binary = ip_to_binary(ip)
    return ip_binary[:prefix_length]


if __name__ == "__main__":
    print("Binary →", ip_to_binary("192.168.1.1"))
    print("Network prefix ", get_network_prefix("200.23.16.0/23"))
