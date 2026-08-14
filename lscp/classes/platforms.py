from enum import Enum


class SupportedPlatform(str, Enum):
    ubuntu_2004 = "Ubuntu 20.04 LTS"  # Not supported; referenced in files for testing purposes
    ubuntu_2204 = "Ubuntu 22.04 LTS"
    ubuntu_2404 = "Ubuntu 24.04 LTS"
