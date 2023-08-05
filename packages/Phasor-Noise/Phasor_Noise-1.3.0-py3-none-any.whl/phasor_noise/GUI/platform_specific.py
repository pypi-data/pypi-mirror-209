import platform
import os


def config_directory():
    """
    Set the default configuration directory for each platform
    """
    if platform.system() == "Linux":
        return "/etc/phasor-generator"
    return "C:/Program Files/phasor-generator/config"


def images_directory():
    """
    Set the default images directory for each platform
    """
    if platform.system() == "Linux":
        return f"/home/{os.environ['USER']}/phasor-generator"
    return f"{os.environ['UserProfile']}/phasor-generator"
