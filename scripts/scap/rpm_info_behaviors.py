from dataclasses import dataclass, field

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class RpmInfoBehaviors:
    """The RpmInfoBehaviors complex type defines a set of behaviors for controlling
    what data, for installed rpms, is collected.

    This behavior aligns with the rpm command.

    :ivar filepaths: 'filepaths', when true, this behavior means collect
        all filepaths (directory and file information) from the rpm
        database for the package.
    """

    filepaths: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
