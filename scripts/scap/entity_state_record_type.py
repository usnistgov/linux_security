from dataclasses import dataclass, field

from scap.entity_state_complex_base_type import EntityStateComplexBaseType
from scap.entity_state_field_type import EntityStateFieldType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class EntityStateRecordType(EntityStateComplexBaseType):
    """The EntityStateRecordType defines an entity that consists of a number of
    uniquely named fields.

    This structure is used for representing a record from a database
    query and other similar structures where multiple related fields
    must be collected at once. Note that for all entities of this type,
    the only allowed datatype is 'record' and the only allowed operation
    is 'equals'. During analysis of a system characteristics item, each
    field is analyzed and then the overall result for elements of this
    type is computed by logically anding the results for each field and
    then applying the entity_check attribute. Note the datatype
    attribute must be set to 'record'. Note the operation attribute must
    be set to 'equals'. Note the var_ref attribute is not permitted and
    the var_check attribute does not apply. Note that when the mask
    attribute is set to 'true', all child field elements must be masked
    regardless of the child field's mask attribute value.
    """

    field_value: list[EntityStateFieldType] = field(
        default_factory=list,
        metadata={
            "name": "field",
            "type": "Element",
            
        },
    )
