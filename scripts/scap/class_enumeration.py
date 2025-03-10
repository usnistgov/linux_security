from enum import Enum

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-common-5"


class ClassEnumeration(Enum):
    """The ClassEnumeration simple type defines the different classes of
    definitions.

    Each class defines a certain intent regarding how an OVAL Definition
    is written and what that definition is describing. The specified
    class gives a hint about the definition so a user can know what the
    definition writer is trying to say. Note that the class does not
    make a statement about whether a true result is good or bad as this
    depends on the use of an OVAL Definition. These classes are also
    used to group definitions by the type of system state they are
    describing. For example, this allows users to find all the
    vulnerability (or patch, or inventory, etc) definitions.

    :cvar COMPLIANCE: A compliance definition describes the state of a
        machine as it complies with a specific policy. A definition of
        this class will evaluate to true when the system is found to be
        compliant with the stated policy. Another way of thinking about
        this is that a compliance definition is stating "the system is
        compliant if ...".
    :cvar INVENTORY: An inventory definition describes whether a
        specific piece of software is installed on the system. A
        definition of this class will evaluate to true when the
        specified software is found on the system. Another way of
        thinking about this is that an inventory definition is stating
        "the software is installed if ...".
    :cvar MISCELLANEOUS: The 'miscellaneous' class is used to identify
        definitions that do not fall into any of the other defined
        classes.
    :cvar PATCH: A patch definition details the machine state of whether
        a patch executable should be installed. A definition of this
        class will evaluate to true when the specified patch is missing
        from the system. Another way of thinking about this is that a
        patch definition is stating "the patch should be installed if
        ...". Note that word SHOULD is intended to mean more than just
        CAN the patch executable be installed. In other words, if a more
        recent patch is already installed then the specified patch might
        not need to be installed.
    :cvar VULNERABILITY: A vulnerability definition describes the
        conditions under which a machine is vulnerable. A definition of
        this class will evaluate to true when the system is found to be
        vulnerable with the stated issue. Another way of thinking about
        this is that a vulnerability definition is stating "the system
        is vulnerable if ...".
    """

    COMPLIANCE = "compliance"
    INVENTORY = "inventory"
    MISCELLANEOUS = "miscellaneous"
    PATCH = "patch"
    VULNERABILITY = "vulnerability"
