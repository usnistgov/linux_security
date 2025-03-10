from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_any_simple_type import EntityStateAnySimpleType
from scap.entity_state_string_type import EntityStateStringType
from scap.entity_state_windows_view_type import EntityStateWindowsViewType
from scap.state_type import StateType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
)


@dataclass
class XmlfilecontentState(StateType):
    """
    The xmlfilecontent_state element contains entities that are used to check the
    file path and name, as well as the xpath used and the value of the this xpath.

    :ivar filepath: The filepath element specifies the absolute path for
        a file on the machine. A directory cannot be specified as a
        filepath.
    :ivar path: The path element specifies the directory component of
        the absolute path to a file on the machine.
    :ivar filename: The filename element specifies the name of the file.
    :ivar xpath: Specifies an XPath 1.0 expression to evaluate against
        the XML file specified by the filename entity.  This XPath 1.0
        expression must evaluate to a list of zero or more text values
        which will be accessible in OVAL via instances of the value_of
        entity.  Any results from evaluating the XPath 1.0 expression
        other than a list of text strings (e.g., a nodes set) is
        considered an error.  The intention is that the text values be
        drawn from instances of a single, uniquely named element or
        attribute.  However, an OVAL interpreter is not required to
        verify this, so the author should define the XPath expression
        carefully.  Note that "equals" is the only valid operator for
        the xpath entity.
    :ivar value_of: The value_of element checks the value(s) of the text
        node(s) or attribute(s) found.
    :ivar windows_view: The windows view value to which this was
        targeted. This is used to indicate which view (32-bit or
        64-bit), the associated State applies to.  This entity only
        applies to 64-bit Microsoft Windows operating systems.
    """

    class Meta:
        name = "xmlfilecontent_state"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-definitions-5#independent"
        )

    filepath: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    path: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filename: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    xpath: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    value_of: Optional[EntityStateAnySimpleType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    windows_view: Optional[EntityStateWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
