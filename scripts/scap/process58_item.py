from dataclasses import dataclass, field
from typing import Optional

from scap.entity_item_capability_type import EntityItemCapabilityType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


@dataclass
class Process58Item:
    """Output of /usr/bin/ps.

    See ps(1).

    :ivar command_line: This is the string used to start the process.
        This includes any parameters that are part of the command line.
    :ivar exec_time: This is the cumulative CPU time, formatted in
        [DD-]HH:MM:SS where DD is the number of days when execution time
        is 24 hours or more.
    :ivar pid: This is the process ID of the process.
    :ivar ppid: This is the process ID of the process's parent process.
    :ivar priority: This is the scheduling priority with which the
        process runs. This can be adjusted with the nice command or
        nice() system call.
    :ivar ruid: This is the real user id which represents the user who
        has created the process.
    :ivar scheduling_class: A platform specific characteristic
        maintained by the scheduler: RT (real-time), TS (timeshare), FF
        (fifo), SYS (system), etc.
    :ivar start_time: This is the time of day the process started
        formatted in HH:MM:SS if the same day the process started or
        formatted as MMM_DD (Ex.: Feb_5) if process started the previous
        day or further in the past.
    :ivar tty: This is the TTY on which the process was started, if
        applicable.
    :ivar user_id: This is the effective user id which represents the
        actual privileges of the process.
    :ivar exec_shield: A boolean that when true would indicates that
        ExecShield is enabled for the process.
    :ivar loginuid: The loginuid shows which account a user gained
        access to the system with. The /proc/XXXX/loginuid shows this
        value.
    :ivar posix_capability: An effective capability associated with the
        process. See linux/include/linux/capability.h for more
        information.
    :ivar selinux_domain_label: An selinux domain label associated with
        the process.
    :ivar session_id: The session ID of the process.
    """

    class Meta:
        name = "process58_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

    command_line: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    exec_time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    pid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    ppid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    priority: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    ruid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    scheduling_class: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    start_time: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    tty: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    user_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    exec_shield: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    loginuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    posix_capability: list[EntityItemCapabilityType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    selinux_domain_label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    session_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
