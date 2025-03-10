from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


@dataclass
class UnameItem:
    """Information about the hardware the machine is running on.

    This information is the parsed equivalent of uname -a.

    :ivar machine_class: This entity specifies the machine hardware
        name.  This corresponds to the command uname -m.
    :ivar node_name: This entity specifies the host name.  This
        corresponds to the command uname -n.
    :ivar os_name: This entity specifies the operating system name.
        This corresponds to the command uname -s.
    :ivar os_release: This entity specifies the build version.  This
        corresponds to the command uname -r.
    :ivar os_version: This entity specifies the operating system
        version.  This corresponds to the command uname -v.
    :ivar processor_type: This entity specifies the processor type.
        This corresponds to the command uname -p.
    """

    class Meta:
        name = "uname_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"

    machine_class: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    node_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    os_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    os_release: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    os_version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    processor_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
