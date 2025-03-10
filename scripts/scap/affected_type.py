from dataclasses import dataclass, field
from typing import Optional

from scap.family_enumeration import FamilyEnumeration

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class AffectedType:
    """Each OVAL Definition is written to evaluate a certain type of system(s).

    The family, platform(s), and product(s) of this target are described
    by the AffectedType whose main purpose is to provide hints for tools
    using OVAL Definitions. For instance, to help a reporting tool only
    use Windows definitions, or to preselect only Red Hat definitions to
    be evaluated. Note, the inclusion of a particular platform or
    product does not mean the definition is physically checking for the
    existence of the platform or product. For the actual test to be
    performed, the correct test must still be included in the
    definition's criteria section. The AffectedType complex type details
    the specific system, application, subsystem, library, etc. for which
    a definition has been written. If a definition is not tied to a
    specific product, then this element should not be included. The
    absence of the platform or product element can be thought of as
    definition applying to all platforms or products. The inclusion of a
    particular platform or product does not mean the definition is
    physically checking for the existence of the platform or product.
    For the actual test to be performed, the correct test must still be
    included in the definition's criteria section. To increase the
    utility of this element, care should be taken when assigning and
    using strings for product names. The schema places no restrictions
    on the values that can be assigned, potentially leading to many
    different representations of the same value. For example, 'Internet
    Explorer' and 'IE' might be used to refer to the same product. The
    current convention is to fully spell out all terms, and avoid the
    use of abbreviations at all costs. Please note that the AffectedType
    will change in future versions of OVAL in order to support the
    Common Platform Enumeration (CPE).
    """

    platform: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    product: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    family: Optional[FamilyEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
