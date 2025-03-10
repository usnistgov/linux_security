from enum import Enum

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-common-5"


class FamilyEnumeration(Enum):
    """The FamilyEnumeration simple type is a listing of families that OVAL
    supports at this time.

    Since new family values can only be added with new version of the
    schema, the value of 'undefined' is to be used when the desired
    family is not available.  Note that use of the undefined family
    value does not target all families, rather it means that some family
    other than one of the defined values is targeted.

    :cvar ANDROID: The android value describes the Android mobile
        operating system.
    :cvar ASA: The asa value describes the Cisco ASA security devices.
    :cvar APPLE_IOS: The apple_ios value describes the iOS mobile
        operating system.
    :cvar CATOS: The catos value describes the Cisco CatOS operating
        system.
    :cvar IOS: The ios value describes the Cisco IOS operating system.
    :cvar IOSXE: The iosxe value describes the Cisco IOS XE operating
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
    """

    ANDROID = "android"
    ASA = "asa"
    APPLE_IOS = "apple_ios"
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
