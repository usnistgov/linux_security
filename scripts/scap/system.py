from dataclasses import dataclass

from scap.system_target_type import SystemTargetType

__NAMESPACE__ = "http://scap.nist.gov/schema/ocil/2.0"


@dataclass
class System(SystemTargetType):
    """
    The system element contains information about the organization it belongs to, a
    set of ip addresses of computers/networks included in the system, description
    about it, and the roles it performs.
    """

    class Meta:
        name = "system"
        namespace = "http://scap.nist.gov/schema/ocil/2.0"
