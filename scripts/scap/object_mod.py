from dataclasses import dataclass

from scap.object_type_1 import ObjectType1

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Object(ObjectType1):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"
