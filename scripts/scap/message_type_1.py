from dataclasses import dataclass, field

from scap.message_level_enumeration import MessageLevelEnumeration

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-common-5"


@dataclass
class MessageType1:
    """The MessageType complex type defines the structure for which messages are
    relayed from the data collection engine.

    Each message is a text string that has an associated level attribute
    identifying the type of message being sent. These messages could be
    error messages, warning messages, debug messages, etc. How the
    messages are used by tools and whether or not they are displayed to
    the user is up to the specific implementation. Please refer to the
    description of the MessageLevelEnumeration for more information
    about each type of message.
    """

    class Meta:
        name = "MessageType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    level: MessageLevelEnumeration = field(
        default=MessageLevelEnumeration.INFO,
        metadata={
            "type": "Attribute",
        },
    )
