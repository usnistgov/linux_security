from dataclasses import dataclass, field

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class RpmVerifyFileBehaviors:
    """The RpmVerifyFileBehaviors complex type defines a set of behaviors that for
    controlling how the individual files in installed rpms are verified.

    These behaviors align with the verify-options of the rpm command
    with the addition of two behaviors that will indicate that a file
    with a given attribute marker should not be collected.

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
    :ivar nofiledigest: 'nofiledigest' when true this behavior means,
        don't verify the file digest attribute.
    :ivar nocaps: 'nocaps' when true this behavior means, don't verify
        the presence of file capabilities.
    """

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
    nofiledigest: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    nocaps: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
