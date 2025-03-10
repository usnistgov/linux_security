from dataclasses import dataclass, field

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class RpmVerifyBehaviors:
    """The RpmVerifyBehaviors complex type defines a set of behaviors that for
    controlling how installed rpms are verified.

    These behaviors align with the verify-options of the rpm command
    with the addition of two behaviors that will indicate that a file
    with a given attribute marker should not be collected.

    :ivar nodeps: 'nodeps' when true this behavior means, don't verify
        dependencies of packages.
    :ivar nodigest: 'nodigest' when true this behavior means, don't
        verify package or header digests when reading.
    :ivar nofiles: 'nofiles' when true this behavior means, don't verify
        any attributes of package files.
    :ivar noscripts: 'noscripts' when true this behavior means, don't
        execute the %verifyscript scriptlet (if any).
    :ivar nosignature: 'nosignature' when true this behavior means,
        don't verify package or header signatures when reading.
    :ivar nolinkto: 'nolinkto' when true this behavior means, don't
        verify symbolic links attribute.
    :ivar nomd5: 'nomd5' when true this behavior means, don't verify the
        file md5 attribute.
    :ivar nosize: 'nosize' when true this behavior means, don't verify
        the file size attribute.
    :ivar nouser: 'nouser' when true this behavior means, don't verify
        the file owner attribute.
    :ivar nogroup: 'nogroup' when true this behavior means, don't verify
        the file group owner attribute.
    :ivar nomtime: 'nomtime' when true this behavior means, don't verify
        the file mtime attribute.
    :ivar nomode: 'nomode' when true this behavior means, don't verify
        the file mode attribute.
    :ivar nordev: 'nordev' when true this behavior means, don't verify
        the file rdev attribute.
    :ivar noconfigfiles: 'noconfigfiles' when true this behavior means,
        skip files that are marked with the %config attribute marker.
    :ivar noghostfiles: 'noghostfiles' when true this behavior means,
        skip files that are maked with %ghost attribute marker.
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
    nofiles: bool = field(
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
    nolinkto: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nomd5: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nosize: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nouser: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nogroup: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nomtime: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nomode: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nordev: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    noconfigfiles: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    noghostfiles: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
