from enum import Enum

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


class LdapBehaviorsScope(Enum):
    BASE = "BASE"
    ONE = "ONE"
    SUBTREE = "SUBTREE"
