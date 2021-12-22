import subprocess
import sys


# Checking IP reachability
def ip_reach(ip_list):

    for ip in ip_list:
        ip = ip.rstrip("\n")

        ping_reply = subprocess.call(
            "ping %s -c 2" % (ip),
            stdout=subprocess.subprocess.DEVNULL,
            stderr=subprocess.subprocess.DEVNULL,
            shell=True
        )

        if ping_reply == 0:
            print("\n* {} is reachable :)\n".format(ip))
            continue
        else:
            print(
                "\n* {} is not reachable :( Check connectivity and try again.".format(
                    ip
                )
            )
            sys.exit()
