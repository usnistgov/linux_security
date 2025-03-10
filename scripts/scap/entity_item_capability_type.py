from enum import Enum

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


class EntityItemCapabilityType(Enum):
    """The EntityItemCapabilityType complex type restricts a string value to a
    specific set of values that describe POSIX capability types associated with a
    process service.

    This list is based off the values defined in
    linux/include/linux/capability.h. Documentation on each allowed
    value can be found in capability.h.  The empty string is also
    allowed to support empty elements associated with error conditions.

    :cvar CAP_CHOWN:
    :cvar CAP_DAC_OVERRIDE:
    :cvar CAP_DAC_READ_SEARCH:
    :cvar CAP_FOWNER:
    :cvar CAP_FSETID:
    :cvar CAP_KILL:
    :cvar CAP_SETGID:
    :cvar CAP_SETUID:
    :cvar CAP_SETPCAP:
    :cvar CAP_LINUX_IMMUTABLE:
    :cvar CAP_NET_BIND_SERVICE:
    :cvar CAP_NET_BROADCAST:
    :cvar CAP_NET_ADMIN:
    :cvar CAP_NET_RAW:
    :cvar CAP_IPC_LOCK:
    :cvar CAP_IPC_OWNER:
    :cvar CAP_SYS_MODULE:
    :cvar CAP_SYS_RAWIO:
    :cvar CAP_SYS_CHROOT:
    :cvar CAP_SYS_PTRACE:
    :cvar CAP_SYS_ADMIN:
    :cvar CAP_SYS_BOOT:
    :cvar CAP_SYS_NICE:
    :cvar CAP_SYS_RESOURCE:
    :cvar CAP_SYS_TIME:
    :cvar CAP_SYS_TTY_CONFIG:
    :cvar CAP_MKNOD:
    :cvar CAP_LEASE:
    :cvar CAP_AUDIT_WRITE:
    :cvar CAP_AUDIT_CONTROL:
    :cvar CAP_SETFCAP:
    :cvar CAP_MAC_OVERRIDE:
    :cvar CAP_MAC_ADMIN:
    :cvar CAP_SYS_PACCT:
    :cvar CAP_SYSLOG:
    :cvar CAP_WAKE_ALARM:
    :cvar CAP_BLOCK_SUSPEND:
    :cvar CAP_AUDIT_READ:
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    CAP_CHOWN = "CAP_CHOWN"
    CAP_DAC_OVERRIDE = "CAP_DAC_OVERRIDE"
    CAP_DAC_READ_SEARCH = "CAP_DAC_READ_SEARCH"
    CAP_FOWNER = "CAP_FOWNER"
    CAP_FSETID = "CAP_FSETID"
    CAP_KILL = "CAP_KILL"
    CAP_SETGID = "CAP_SETGID"
    CAP_SETUID = "CAP_SETUID"
    CAP_SETPCAP = "CAP_SETPCAP"
    CAP_LINUX_IMMUTABLE = "CAP_LINUX_IMMUTABLE"
    CAP_NET_BIND_SERVICE = "CAP_NET_BIND_SERVICE"
    CAP_NET_BROADCAST = "CAP_NET_BROADCAST"
    CAP_NET_ADMIN = "CAP_NET_ADMIN"
    CAP_NET_RAW = "CAP_NET_RAW"
    CAP_IPC_LOCK = "CAP_IPC_LOCK"
    CAP_IPC_OWNER = "CAP_IPC_OWNER"
    CAP_SYS_MODULE = "CAP_SYS_MODULE"
    CAP_SYS_RAWIO = "CAP_SYS_RAWIO"
    CAP_SYS_CHROOT = "CAP_SYS_CHROOT"
    CAP_SYS_PTRACE = "CAP_SYS_PTRACE"
    CAP_SYS_ADMIN = "CAP_SYS_ADMIN"
    CAP_SYS_BOOT = "CAP_SYS_BOOT"
    CAP_SYS_NICE = "CAP_SYS_NICE"
    CAP_SYS_RESOURCE = "CAP_SYS_RESOURCE"
    CAP_SYS_TIME = "CAP_SYS_TIME"
    CAP_SYS_TTY_CONFIG = "CAP_SYS_TTY_CONFIG"
    CAP_MKNOD = "CAP_MKNOD"
    CAP_LEASE = "CAP_LEASE"
    CAP_AUDIT_WRITE = "CAP_AUDIT_WRITE"
    CAP_AUDIT_CONTROL = "CAP_AUDIT_CONTROL"
    CAP_SETFCAP = "CAP_SETFCAP"
    CAP_MAC_OVERRIDE = "CAP_MAC_OVERRIDE"
    CAP_MAC_ADMIN = "CAP_MAC_ADMIN"
    CAP_SYS_PACCT = "CAP_SYS_PACCT"
    CAP_SYSLOG = "CAP_SYSLOG"
    CAP_WAKE_ALARM = "CAP_WAKE_ALARM"
    CAP_BLOCK_SUSPEND = "CAP_BLOCK_SUSPEND"
    CAP_AUDIT_READ = "CAP_AUDIT_READ"
    VALUE = ""
