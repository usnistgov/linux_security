from dataclasses import dataclass

from scap.item_type_abstract import ItemTypeAbstract

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class Item(ItemTypeAbstract):
    """An item is a named constituent of an &lt;xccdf:Benchmark&gt;.

    There are three types of items: &lt;xccdf:Group&gt;,
    &lt;xccdf:Rule&gt; and &lt;xccdf:Value&gt;. The &lt;xccdf:Item&gt; element type
    imposes constraints shared by all &lt;xccdf:Group&gt;, &lt;xccdf:Rule&gt; and
    &lt;xccdf:Value&gt; elements. The itemType is abstract, so the element
    &lt;xccdf:Item&gt; can never appear in a valid XCCDF document.
    """

    class Meta:
        namespace = "http://checklists.nist.gov/xccdf/1.2"
