from dataclasses import dataclass, field
from typing import Optional

from scap.param_type import ParamType

__NAMESPACE__ = "http://checklists.nist.gov/xccdf/1.2"


@dataclass
class Model:
    """A suggested scoring model for an &lt;xccdf:Benchmark&gt;, also encapsulating
    any parameters needed by the model.

    Every model is designated with a URI, which appears here as the
    system attribute. See the XCCDF specification for a list of standard
    scoring models and their associated URIs. Vendors may define their
    own scoring models and provide additional URIs to designate them.
    Some models may need additional parameters; to support such a model,
    zero or more &lt;xccdf:param&gt; elements may appear as children of
    the &lt;xccdf:model&gt; element.

    :ivar param: Parameters provided as input to the designated scoring
        model.
    :ivar system: A URI designating a scoring model.
    """

    class Meta:
        name = "model"
        namespace = "http://checklists.nist.gov/xccdf/1.2"

    param: list[ParamType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
