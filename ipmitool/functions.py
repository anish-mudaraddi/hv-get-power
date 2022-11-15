import re
from .utils import check_ipmi_conn, ipmi_query_power, to_csv


def get_current_power(csv=False):
    """ get current power info from ipmitool """
    if not check_ipmi_conn():
        return None
    res = ipmi_query_power()

    power_stats = {}
    for line in res.stdout.splitlines():
        line_str = line.split(b":")
        stat = line_str[0].decode().strip().lower().replace(" ", "_")
        if stat == "current_power":
            power_str = "".join([l.decode() for l in line_str[1:]]).strip()
            power_stats[stat] = re.search("[0-9]+", power_str).group(0)

    if csv:
        return to_csv(power_stats)
    return power_stats


def get_all_power_stats(csv=False):
    """ get all power info from ipmitool """
    if not check_ipmi_conn():
        return None
    res = ipmi_query_power()

    power_stats = {}
    for line in res.stdout.splitlines():
        line_str = line.split(b":")
        stat = line_str[0].decode().strip().lower().replace(" ", "_")
        val_str = ":".join([l.decode() for l in line_str[1:]]).strip()

        key, val = {
            "current_power": lambda a: ("current_power", re.search("[0-9]+", a).group(0)),
            "minimum_power_over_sampling_duration": lambda a: ("min", re.search("[0-9]+", a).group(0)),
            "maximum_power_over_sampling_duration": lambda a: ("max", re.search("[0-9]+", a).group(0)),
            "average_power_over_sampling_duration": lambda a: ("average", re.search("[0-9]+", a).group(0)),
            "statistics_reporting_time_period": lambda a: ("sampling_period", re.search("[0-9]+", a).group(0))
        }.get(stat, lambda a: (None, None))(val_str)
        if key:
            power_stats[key] = val

    if csv:
        return to_csv(power_stats)
    return power_stats



