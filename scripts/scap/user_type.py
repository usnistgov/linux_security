from dataclasses import dataclass, field

from scap.named_item_base_type import NamedItemBaseType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class UserType(NamedItemBaseType):
    """
    The UserType type defines structures containing information about a user such
    as name, organization, position, email, and role.

    :ivar organization: The organization element specifies the company
        or institution that the user belongs to.
    :ivar position: The position element holds the job title or the
        position of the user within his/her organization.
    :ivar email: The email element holds the email address where the
        user can be contacted. TODO: define an email pattern
    """

    organization: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    position: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
    email: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://scap.nist.gov/schema/ocil/2.0",
        },
    )
