from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_int_type import EntityStateIntType
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"


@dataclass
class ProcessState(StateType):
    """The process_state element defines the different metadata associated with a
    UNIX process.

    This includes the command line, pid, ppid, priority, and user id.
    Please refer to the individual elements in the schema for more
    details about what each represents.

    :ivar command: The command element specifies the command/program
        name to check.
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
    """

    class Meta:
        name = "process_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#unix"

    command: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    exec_time: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    pid: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    ppid: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    priority: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    ruid: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    scheduling_class: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    start_time: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    tty: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    user_id: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
