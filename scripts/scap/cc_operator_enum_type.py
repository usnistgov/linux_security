from enum import Enum

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


class CcOperatorEnumType(Enum):
    """The type for the allowed @operator names for the &lt;xccdf:complex-check&gt;
    operator attribute.

    Only AND and OR operators are supported. (The &lt;xccdf:complex-
    check&gt; has a separate mechanism for negation.)

    :cvar OR: The logical OR of the component terms
    :cvar AND: The logical AND of the component terms
    """

    OR = "OR"
    AND = "AND"
