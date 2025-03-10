from dataclasses import dataclass

from scap.named_item_base_type import NamedItemBaseType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class Target(NamedItemBaseType):
    """A target element describes the user, system, or role that applies to all
    questionnaires in scope.

    For instance, specifying that user Joe Smith should complete this
    document; applies to system with ip address of 123.45.67.89; applies
    to all systems functioning as (role) web servers; or all (role)
    administrators should complete this document.
    """

    class Meta:
        name = "target"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
