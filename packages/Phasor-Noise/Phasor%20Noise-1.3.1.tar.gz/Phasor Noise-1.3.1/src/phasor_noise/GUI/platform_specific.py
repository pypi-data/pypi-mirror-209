from pathlib import Path
import os


def config_directory():
    """
    Set the default configuration directory for each platform
    """
    path = Path(os.path.expanduser("~/phasor-generator/config"))
    if not os.path.exists(path):
        path.mkdir(parents=True)
    return path


def images_directory():
    """
    Set the default images directory for each platform
    """
    path = Path(os.path.expanduser("~/phasor-generator/images"))
    if not os.path.exists(path):
        path.mkdir(parents=True)
    return path
