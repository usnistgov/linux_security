from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_int_type import EntityStateIntType
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class SelinuxsecuritycontextState(StateType):
    """The selinuxsecuritycontext_state element defines the different information
    that can be used to evaluate the specified SELinux security context.

    This includes SELinux security context's user, type role, low
    sensitivity, low category, high sensitivity, high category, raw low
    sensitivity, raw low category, raw high sensitivity, and raw high
    category. This state follows the SELinux security context structure:
    user:role
    :type: low_sensitivity[:low_category]- high_sensitivity
    [:high_category]. Please refer to the individual elements in the
    schema for more details about what each represents.

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
        name = "selinuxsecuritycontext_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    filepath: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    path: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filename: Optional[EntityStateStringType] = field(
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
    user: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    role: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    type_value: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            
        },
    )
    low_sensitivity: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    low_category: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    high_sensitivity: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    high_category: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    rawlow_sensitivity: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    rawlow_category: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    rawhigh_sensitivity: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    rawhigh_category: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
