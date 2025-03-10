from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"
)


@dataclass
class SelinuxsecuritycontextItem:
    """This item describes the SELinux security context of a file or process on the
    local system.

    This item follows the SELinux security context structure: user:role:type:low_sensitivity[:low_category]- high_sensitivity [:high_category]. It extends the standard ItemType as defined in the oval-system-characteristics schema and one should refer to the ItemType description for more information.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The name of the file. If the xsi:nil attribute is
        set to true, then the item being represented is the higher
        directory represented by the path entity.
    :ivar pid: This is the process ID of the process.
    :ivar user: The user element specifies the SELinux user that either
        created the file or started the process.
    :ivar role: The role element specifies the types that a process may
        transition to (domain transitions). Note that this entity is not
        relevant for files and will always have a value of object_r.
    :ivar type_value: The type element specifies the domain in which the
        file is accessible or the domain in which a process executes.
    :ivar low_sensitivity: The low_sensitivity element specifies the
        current sensitivity of a file or process.
    :ivar low_category: The low_category element specifies the set of
        categories associated with the low sensitivity.
    :ivar high_sensitivity: The high_sensitivity element specifies the
        maximum range for a file or the clearance for a process.
    :ivar high_category: The high_category element specifies the set of
        categories associated with the high sensitivity.
    :ivar rawlow_sensitivity: The rawlow_sensitivity element specifies
        the current sensitivity of a file or process but in its raw
        context.
    :ivar rawlow_category: The rawlow_category element specifies the set
        of categories associated with the low sensitivity but in its raw
        context.
    :ivar rawhigh_sensitivity: The rawhigh_sensitivity element specifies
        the maximum range for a file or the clearance for a process but
        in its raw context.
    :ivar rawhigh_category: The rawhigh_category element specifies the
        set of categories associated with the high sensitivity but in
        its raw context.
    """

    class Meta:
        name = "selinuxsecuritycontext_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
            "nillable": True,
        },
    )
    pid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    user: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            
        },
    )
    low_sensitivity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    low_category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    high_sensitivity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    high_category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    rawlow_sensitivity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    rawlow_category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    rawhigh_sensitivity: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    rawhigh_category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
