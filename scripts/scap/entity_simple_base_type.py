from dataclasses import dataclass, field
from typing import Optional

from scap.check_enumeration import CheckEnumeration
from scap.datatype_enumeration import DatatypeEnumeration
from scap.operation_enumeration import OperationEnumeration

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class EntitySimpleBaseType:
    """The EntitySimpleBaseType complex type is an abstract type that defines the
    default attributes associated with every simple entity.

    Entities can be found in both OVAL Objects and OVAL States and
    represent the individual properties associated with items found on a
    system. An example of a single entity would be the path of a file.
    Another example would be the version of the file.

    :ivar value:
    :ivar datatype: The optional datatype attribute specifies how the
        given operation should be applied to the data. Since we are
        dealing with XML everything is technically a string, but often
        the value is meant to represent some other datatype and this
        affects the way an operation is performed. For example, with the
        statement 'is 123 less than 98'. If the data is treated as
        integers the answer is no, but if the data is treated as
        strings, then the answer is yes. Specifying a datatype defines
        how the less than operation should be performed. Another way of
        thinking of things is that the datatype attribute specifies how
        the data should be cast before performing the operation (note
        that the default datatype is 'string'). In the previous example,
        if the datatype is set to int, then '123' and '98' should be
        cast as integers. Another example is applying the 'equals'
        operation to '1.0.0.0' and '1.0'. With datatype 'string' they
        are not equal, with datatype 'version' they are. Note that there
        are certain cases where a cast from one datatype to another is
        not possible. If a cast cannot be made, (trying to cast 'abc' to
        an integer) then an error should be reported. For example, if
        the datatype is set to 'integer' and the value is the empty
        string. There is no way to cast the empty string (or NULL) to an
        integer, and in cases like this an error should be reported.
    :ivar operation: The optional operation attribute determines how the
        individual entities should be evaluated (the default operation
        is 'equals').
    :ivar mask: The optional mask attribute is used to identify values
        that have been hidden for sensitivity concerns. This is used by
        the Result document which uses the System Characteristics schema
        to format the information found on a specific system. When the
        mask attribute is set to 'true' on an OVAL Entity or an OVAL
        Field, the corresponding collected value of that OVAL Entity or
        OVAL Field MUST NOT be present in the "results" section of the
        OVAL Results document; the "oval_definitions" section must not
        be altered and must be an exact copy of the definitions
        evaluated. Values MUST NOT be masked in OVAL System
        Characteristics documents that are not contained within an OVAL
        Results document. It is possible for masking conflicts to occur
        where one entity has mask set to true and another entity has
        mask set to false. A conflict will occur when the mask attribute
        is set differently on an OVAL Object and matching OVAL State or
        when more than one OVAL Objects identify the same OVAL Item(s).
        When such a conflict occurs the result is always to mask the
        entity.
    :ivar var_ref: The optional var_ref attribute refers the value of
        the element to a variable element. When supplied, the value(s)
        associated with the OVAL Variable should be used as the value(s)
        of the element. If there is an error computing the value of the
        variable, then that error should be passed up to the element
        referencing it. If the variable being referenced does not have a
        value (for example, if the variable pertains to the size of a
        file, but the file does not exist) then one of two results are
        possible. If the element is part of an object declaration, then
        the object element referencing it is considered to not exist. If
        the element is part of a state declaration, then the state
        element referencing it will evaluate to error.
    :ivar var_check: The optional var_check attribute specifies how data
        collection or state evaluation should proceed when an element
        uses a var_ref attribute, and the associated variable defines
        more than one value. For example, if an object entity 'filename'
        with an operation of 'not equal' references a variable that
        returns five different values, and the var_check attribute has a
        value of 'all', then an actual file on the system matches only
        if the actual filename does not equal any of the variable
        values. As another example, if a state entity 'size' with an
        operation of 'less than' references a variable that has five
        different integer values, and the var_check attribute has a
        value of 'all', then the 'size' state entity evaluates to true
        only if the corresponding 'size' item entity is less than each
        of the five integers defined by the variable. If a variable does
        not have any value value when referenced by an OVAL Object the
        object should be considered to not exist. If a variable does not
        have any value when referenced by an OVAL State an error should
        be reported during OVAL analysis. When an OVAL State uses a
        var_ref, if both the state entity and a corresponding item
        entity are collections of values, the var_check is applied to
        each value of the item entity individually, and all must
        evaluate to true for the state entity to evaluate to true. In
        this condition, there is no value of var_check which enables an
        element-wise comparison, and so there is no way to determine
        whether the two entities are truly 'equal' in that sense. If
        var_ref is present but var_check is not, the element should be
        processed as if var_check has the value "all".
    """

    value: Optional[object] = field(default=None)
    datatype: DatatypeEnumeration = field(
        default=DatatypeEnumeration.STRING,
        metadata={
            "type": "Attribute",
        },
    )
    operation: OperationEnumeration = field(
        default=OperationEnumeration.EQUALS,
        metadata={
            "type": "Attribute",
        },
    )
    mask: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:var:[1-9][0-9]*",
        },
    )
    var_check: Optional[CheckEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
