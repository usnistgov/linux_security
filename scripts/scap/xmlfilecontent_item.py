from dataclasses import dataclass, field
from typing import Optional

from scap.entity_item_windows_view_type import EntityItemWindowsViewType

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"
)


@dataclass
class XmlfilecontentItem:
    """
    This item stores results from checking the contents of an xml file.

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
        node(s) or attribute(s) found. How this is used is entirely
        controlled by operator attributes.
    :ivar windows_view: The windows view value from which this OVAL Item
        was collected. This is used to indicate from which view (32-bit
        or 64-bit), the associated Item was collected. A value of
        '32_bit' indicates the Item was collected from the 32-bit view.
        A value of '64-bit' indicates the Item was collected from the
        64-bit view. Omitting this entity removes any assertion about
        which view the Item was collected from, and therefore it is
        strongly suggested that this entity be set. This entity only
        applies to 64-bit Microsoft Windows operating systems.
    """

    class Meta:
        name = "xmlfilecontent_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#independent"

    filepath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    filename: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    xpath: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    value_of: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    windows_view: Optional[EntityItemWindowsViewType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
