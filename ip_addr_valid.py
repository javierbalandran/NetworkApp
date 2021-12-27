import sys


# Checking octets
def ip_addr_valid(addr_list):

    for ip in addr_list:
        ip = ip.rstrip("\n")
        octet_list = ip.split(".")

        # Valid length = 4 octets
        is_valid_length = len(octet_list) == 4
        # Loopback 127.0.0.0. - 127.255.255.255
        is_loopback = int(octet_list[0]) == 127
        # Multicast: 224.0.0.0 - 239.255.255.255
        is_multicast = 224 <= int(octet_list[0]) <= 239
        # Broadcast: 255.255.255.255
        is_broadcast = (
            int(octet_list[0]) == 255
            and int(octet_list[1]) == 255
            and int(octet_list[2]) == 255
            and int(octet_list[3]) == 255
        )
        # Link-Local: 169.254.0.0 - 169.254.255.255
        is_link_local = int(octet_list[0]) == 169 and int(octet_list[1]) == 254
        # Reserved for future use: 240.0.0.0 - 255.255.255.254
        is_future_reserved = 240 <= int(octet_list[0]) <= 255

        if is_valid_length and not (
            is_loopback
            or is_multicast
            or is_broadcast
            or is_link_local
            or is_future_reserved
        ):
            continue
        else:
            print(
                "\n* There was an invalid IP address in the file: {} : (\n".format(ip)
            )
            sys.exit()
