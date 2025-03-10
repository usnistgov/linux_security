from enum import Enum

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#unix"
)


class EntityItemEncryptMethodType(Enum):
    """The EntityItemEncryptMethodType complex type restricts a string value to a
    set that corresponds to the allowed encrypt methods used for protected
    passwords in a shadow file.

    The empty string is also allowed to support empty elements
    associated with error conditions.

    :cvar DES: The DES method corresponds to the (none) prefix.
    :cvar BSDI: The BSDi method corresponds to BSDi modified DES or the
        '_' prefix.
    :cvar MD5: The MD5 method corresponds to MD5 for Linux/BSD or the
        $1$ prefix.
    :cvar BLOWFISH: The Blowfish method corresponds to Blowfish
        (OpenBSD) or the $2$ or $2a$ prefixes.
    :cvar SUN_MD5: The Sun MD5 method corresponds to the $md5$ prefix.
    :cvar SHA_256: The SHA-256 method corresponds to the $5$ prefix.
    :cvar SHA_512: The SHA-512 method corresponds to the $6$ prefix.
    :cvar VALUE: The empty string value is permitted here to allow for
        empty elements associated with variable references.
    """

    DES = "DES"
    BSDI = "BSDi"
    MD5 = "MD5"
    BLOWFISH = "Blowfish"
    SUN_MD5 = "Sun MD5"
    SHA_256 = "SHA-256"
    SHA_512 = "SHA-512"
    VALUE = ""
