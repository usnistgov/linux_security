from enum import Enum

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"
)


class EntityItemFamilyType(Enum):
    """The EntityItemFamilyType complex type defines a string entity value that is
    restricted to a set of enumerations.

    Each valid enumeration is a high-level family of system operating
    system.

    :cvar ANDROID: The android value describes the Android mobile
        operating system.
    :cvar APPLE_IOS: The apple_ios value describes the iOS mobile
        operating system.
    :cvar ASA: The asa value describes the Cisco ASA security devices.
    :cvar CATOS: The catos value describes the Cisco CatOS operating
        system.
    :cvar IOS: The ios value describes the Cisco IOS operating system.
    :cvar IOSXE: The iosxe value describes the Cisco IOS-XE operating
        system.
    :cvar JUNOS: The junos value describes the Juniper JunOS operating
        system.
    :cvar MACOS: The macos value describes the Mac operating system.
    :cvar PIXOS: The pixos value describes the Cisco PIX operating
        system.
    :cvar UNDEFINED: The undefined value is to be used when the desired
        family is not available.
    :cvar UNIX: The unix value describes the UNIX operating system.
    :cvar VMWARE_INFRASTRUCTURE: The vmware_infrastructure value
        describes VMWare Infrastructure.
    :cvar WINDOWS: The windows value describes the Microsoft Windows
        operating system.
    :cvar VALUE: The empty string value is permitted here to allow for
        detailed error reporting.
    """

    ANDROID = "android"
    APPLE_IOS = "apple_ios"
    ASA = "asa"
    CATOS = "catos"
    IOS = "ios"
    IOSXE = "iosxe"
    JUNOS = "junos"
    MACOS = "macos"
    PIXOS = "pixos"
    UNDEFINED = "undefined"
    UNIX = "unix"
    VMWARE_INFRASTRUCTURE = "vmware_infrastructure"
    WINDOWS = "windows"
    VALUE = ""
