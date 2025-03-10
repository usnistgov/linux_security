from dataclasses import dataclass

from scap.user_type import UserType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class User(UserType):
    """
    A user element contains information about a target user such as name,
    organization, position, email, and role.
    """

    class Meta:
        name = "user"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
