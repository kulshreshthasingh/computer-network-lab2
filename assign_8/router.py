def ip_to_binary(ip_address: str) -> str:
    return "".join(f"{int(octet):08b}" for octet in ip_address.split("."))


def get_network_prefix(ip_cidr: str) -> str:
    ip, prefix_length = ip_cidr.split("/")
    prefix_length = int(prefix_length)
    ip_binary = ip_to_binary(ip)
    return ip_binary[:prefix_length]


class Router:
    def __init__(self, routes):
        self.forwarding_table = self._build_forwarding_table(routes)

    def _build_forwarding_table(self, routes):
        table = []
        for cidr, link in routes:
            prefix = get_network_prefix(cidr)
            table.append((prefix, link))
        table.sort(key=lambda x: len(x[0]), reverse=True)
        return table

    def route_packet(self, dest_ip: str) -> str:
        dest_binary = ip_to_binary(dest_ip)
        for prefix, link in self.forwarding_table:
            if dest_binary.startswith(prefix):
                return link
        return "Default Gateway"


if __name__ == "__main__":
    routes = [
        ("223.1.1.0/24", "Link 0"),
        ("223.1.2.0/24", "Link 1"),
        ("223.1.3.0/24", "Link 2"),
        ("223.1.0.0/16", "Link 4 (ISP)")
    ]

    router = Router(routes)

    print("223.1.1.100 →", router.route_packet("223.1.1.100"))   # Link 0
    print("223.1.2.5 →", router.route_packet("223.1.2.5"))       # Link 1
    print("223.1.250.1 →", router.route_packet("223.1.250.1"))   # Link 4 (ISP)
    print("198.51.100.1 →", router.route_packet("198.51.100.1")) # Default Gateway
