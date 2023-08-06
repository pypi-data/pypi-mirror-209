from platform import platform


def is_mac() -> bool:
    is_mac = False
    if not any(os_name in platform() for os_name in ["Windows", "Linux"]):
        is_mac = True
    return is_mac
