from enum import Enum

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"
)


class EntityItemHashTypeType(Enum):
    """The EntityItemHashTypeType complex type restricts a string value to a
    specific set of values that specify the different hash algorithms that are
    supported.

    The empty string is also allowed to support empty elements
    associated with variable references.

    :cvar MD5: The MD5 hash algorithm.
    :cvar SHA_1: The SHA-1 hash algorithm.
    :cvar SHA_224: The SHA-224 hash algorithm.
    :cvar SHA_256: The SHA-256 hash algorithm.
    :cvar SHA_384: The SHA-384 hash algorithm.
    :cvar SHA_512: The SHA-512 hash algorithm.
    :cvar VALUE: The empty string value is permitted here to allow for
        detailed error reporting.
    """

    MD5 = "MD5"
    SHA_1 = "SHA-1"
    SHA_224 = "SHA-224"
    SHA_256 = "SHA-256"
    SHA_384 = "SHA-384"
    SHA_512 = "SHA-512"
    VALUE = ""
