from dataclasses import dataclass, field

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class RpmVerifyPackageBehaviors:
    """The RpmVerifyPackageBehaviors complex type defines a set of behaviors that
    for controlling how installed rpms are verified.

    These behaviors align with the verify-options of the rpm command.

    :ivar nodeps: 'nodeps' when true this behavior means, don't verify
        dependencies of packages.
    :ivar nodigest: 'nodigest' when true this behavior means, don't
        verify package or header digests when reading.
    :ivar noscripts: 'noscripts' when true this behavior means, don't
        execute the %verifyscript scriptlet (if any).
    :ivar nosignature: 'nosignature' when true this behavior means,
        don't verify package or header signatures when reading.
    """

    nodeps: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nodigest: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    noscripts: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nosignature: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
