import subprocess
import time
import os


def run_cmd(cmd_args, max_retries=3):
    """Run command with given arguments and return output"""
    for retry in range(max_retries):
        res = subprocess.run(cmd_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if res.returncode:
            # We encountered a failure - likely due to the node being busy
            # Wait for longer time after each consecutive fail
            time.sleep(retry + 1)
            continue
        return res


def check_ipmi_conn():
    # check if ipmi exists
    if not any(
        [os.path.exists(f) for f in ["/dev/ipmi0", "/dev/ipmi/0", "/dev/ipmidev/0"]]
    ):
        print("No IPMI found on this node, Exiting")
        return False

    # check if ipmitool exists
    res = run_cmd(["/usr/bin/ipmitool", "sel", "info"])
    if res.returncode:
        print("Failed to run ipmitool sel! (%s). Exiting" % res.stderr)
        return False
    return True


def ipmi_query_power():
    # Get Power Info
    res = run_cmd(["/usr/sbin/ipmi-dcmi", "--get-system-power-statistics"])
    if res.returncode:
        print("Failed to run ipmi-dcmi tool! (%s). Exiting" % res.stderr)
        return None
    return res

def to_csv(stats, include_header=True):
    res = ",".join([str(s) for s in stats.values()])
    if include_header:
        return "%s\n%s" % (",".join(stats.keys()), res)
    return res