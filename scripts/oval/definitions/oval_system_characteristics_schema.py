from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Union

from oval.definitions.oval_common_schema import (
    DatatypeEnumeration,
    GeneratorType,
    MessageType,
    SimpleDatatypeEnumeration,
)

from oval.definitions.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5"


class EntityItemIpaddressStringTypeDatatype(Enum):
    """
    :cvar IPV4_ADDRESS: The ipv4_address datatype represents IPv4
        addresses and IPv4 address prefixes. Its value space consists of
        the set of ordered pairs of integers where the first element of
        each pair is in the range [0,2^32) (the representable range of a
        32-bit unsigned int), and the second is in the range [0,32]. The
        first element is an address, and the second is a prefix length.
        The lexical space is dotted-quad CIDR-like notation ('a.b.c.d'
        where 'a', 'b', 'c', and 'd' are integers from 0-255),
        optionally followed by a slash ('/') and either a prefix length
        (an integer from 0-32) or a netmask represented in the dotted-
        quad notation described previously. Examples of legal values are
        '192.0.2.0', '192.0.2.0/32', and '192.0.2.0/255.255.255.255'.
        Additionally, leading zeros are permitted such that '192.0.2.0'
        is equal to '192.000.002.000'. If a prefix length is not
        specified, it is implicitly equal to 32. The expected operations
        within OVAL for ipv4_address values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'subset of', and 'superset of'. All operations are
        defined in terms of the value space. Let A and B be ipv4_address
        values (i.e. ordered pairs from the value space). The following
        definitions assume that bits outside the prefix have been zeroed
        out. By zeroing the low order bits, they are effectively ignored
        for all operations. Implementations of the following operations
        MUST behave as if this has been done. The following defines how
        to perform each operation for the ipv4_address datatype. Let
        P_addr mean the first element of ordered pair P and P_prefix
        mean the second element. equals: A equals B if and only if
        A_addr == B_addr and A_prefix == B_prefix. not equal: A is not
        equal to B if and only if they don't satisfy the criteria for
        operator "equals". greater than: A is greater than B if and only
        if A_prefix == B_prefix and A_addr &gt; B_addr. If A_prefix !=
        B_prefix, i.e. prefix lengths are not equal, an error MUST be
        reported. greater than or equal: A is greater than or equal to B
        if and only if A_prefix == B_prefix and they satisfy either the
        criteria for operators "equal" or "greater than". If A_prefix !=
        B_prefix, i.e. prefix lengths are not equal, an error MUST be
        reported. less than: A is less than B if and only if A_prefix ==
        B_prefix and they don't satisfy the criteria for operator
        "greater than or equal". If A_prefix != B_prefix, i.e. prefix
        lengths are not equal, an error MUST be reported. less than or
        equal: A is less than or equal to B if and only if A_prefix ==
        B_prefix and they don't satisfy the criteria for operator
        "greater than". If A_prefix != B_prefix, i.e. prefix lengths are
        not equal, an error MUST be reported. subset of: A is a subset
        of B if and only if every IPv4 address in subnet A is present in
        subnet B. In other words, A_prefix &gt;= B_prefix and the high
        B_prefix bits of A_addr and B_addr are equal. superset of: A is
        a superset of B if and only if B is a subset of A.
    :cvar IPV6_ADDRESS: The ipv6_address datatype represents IPv6
        addresses and IPv6 address prefixes. Its value space consists of
        the set of ordered pairs of integers where the first element of
        each pair is in the range [0,2^128) (the representable range of
        a 128-bit unsigned int), and the second is in the range [0,128].
        The first element is an address, and the second is a prefix
        length. The lexical space is CIDR notation given in IETF
        specification RFC 4291 for textual representations of IPv6
        addresses and IPv6 address prefixes (see sections 2.2 and 2.3).
        If a prefix-length is not specified, it is implicitly equal to
        128. The expected operations within OVAL for ipv6_address values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', 'less than or equal', 'subset of', and
        'superset of'. All operations are defined in terms of the value
        space. Let A and B be ipv6_address values (i.e. ordered pairs
        from the value space). The following definitions assume that
        bits outside the prefix have been zeroed out. By zeroing the low
        order bits, they are effectively ignored for all operations.
        Implementations of the following operations MUST behave as if
        this has been done. The following defines how to perform each
        operation for the ipv6_address datatype. Let P_addr mean the
        first element of ordered pair P and P_prefix mean the second
        element. equals: A equals B if and only if A_addr == B_addr and
        A_prefix == B_prefix. not equal: A is not equal to B if and only
        if they don't satisfy the criteria for operator "equals".
        greater than: A is greater than B if and only if A_prefix ==
        B_prefix and A_addr &gt; B_addr. If A_prefix != B_prefix, an
        error MUST be reported. greater than or equal: A is greater than
        or equal to B if and only if A_prefix == B_prefix and they
        satisfy either the criteria for operators "equal" or "greater
        than". If A_prefix != B_prefix, an error MUST be reported. less
        than: A is less than B if and only if A_prefix == B_prefix and
        they don't satisfy the criteria for operator "greater than or
        equal". If A_prefix != B_prefix, an error MUST be reported. less
        than or equal: A is less than or equal to B if and only if
        A_prefix == B_prefix and they don't satisfy the criteria for
        operator "greater than". If A_prefix != B_prefix, an error MUST
        be reported. subset of: A is a subset of B if and only if every
        IPv6 address in subnet A is present in subnet B. In other words,
        A_prefix &gt;= B_prefix and the high B_prefix bits of A_addr and
        B_addr are equal. superset of: A is a superset of B if and only
        if B is a subset of A.
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    """

    IPV4_ADDRESS = "ipv4_address"
    IPV6_ADDRESS = "ipv6_address"
    STRING = "string"


class EntityItemIpaddressTypeDatatype(Enum):
    """
    :cvar IPV4_ADDRESS: The ipv4_address datatype represents IPv4
        addresses and IPv4 address prefixes. Its value space consists of
        the set of ordered pairs of integers where the first element of
        each pair is in the range [0,2^32) (the representable range of a
        32-bit unsigned int), and the second is in the range [0,32]. The
        first element is an address, and the second is a prefix length.
        The lexical space is dotted-quad CIDR-like notation ('a.b.c.d'
        where 'a', 'b', 'c', and 'd' are integers from 0-255),
        optionally followed by a slash ('/') and either a prefix length
        (an integer from 0-32) or a netmask represented in the dotted-
        quad notation described previously. Examples of legal values are
        '192.0.2.0', '192.0.2.0/32', and '192.0.2.0/255.255.255.255'.
        Additionally, leading zeros are permitted such that '192.0.2.0'
        is equal to '192.000.002.000'. If a prefix length is not
        specified, it is implicitly equal to 32. The expected operations
        within OVAL for ipv4_address values are 'equals', 'not equal',
        'greater than', 'greater than or equal', 'less than', 'less than
        or equal', 'subset of', and 'superset of'. All operations are
        defined in terms of the value space. Let A and B be ipv4_address
        values (i.e. ordered pairs from the value space). The following
        definitions assume that bits outside the prefix have been zeroed
        out. By zeroing the low order bits, they are effectively ignored
        for all operations. Implementations of the following operations
        MUST behave as if this has been done. The following defines how
        to perform each operation for the ipv4_address datatype. Let
        P_addr mean the first element of ordered pair P and P_prefix
        mean the second element. equals: A equals B if and only if
        A_addr == B_addr and A_prefix == B_prefix. not equal: A is not
        equal to B if and only if they don't satisfy the criteria for
        operator "equals". greater than: A is greater than B if and only
        if A_prefix == B_prefix and A_addr &gt; B_addr. If A_prefix !=
        B_prefix, i.e. prefix lengths are not equal, an error MUST be
        reported. greater than or equal: A is greater than or equal to B
        if and only if A_prefix == B_prefix and they satisfy either the
        criteria for operators "equal" or "greater than". If A_prefix !=
        B_prefix, i.e. prefix lengths are not equal, an error MUST be
        reported. less than: A is less than B if and only if A_prefix ==
        B_prefix and they don't satisfy the criteria for operator
        "greater than or equal". If A_prefix != B_prefix, i.e. prefix
        lengths are not equal, an error MUST be reported. less than or
        equal: A is less than or equal to B if and only if A_prefix ==
        B_prefix and they don't satisfy the criteria for operator
        "greater than". If A_prefix != B_prefix, i.e. prefix lengths are
        not equal, an error MUST be reported. subset of: A is a subset
        of B if and only if every IPv4 address in subnet A is present in
        subnet B. In other words, A_prefix &gt;= B_prefix and the high
        B_prefix bits of A_addr and B_addr are equal. superset of: A is
        a superset of B if and only if B is a subset of A.
    :cvar IPV6_ADDRESS: The ipv6_address datatype represents IPv6
        addresses and IPv6 address prefixes. Its value space consists of
        the set of ordered pairs of integers where the first element of
        each pair is in the range [0,2^128) (the representable range of
        a 128-bit unsigned int), and the second is in the range [0,128].
        The first element is an address, and the second is a prefix
        length. The lexical space is CIDR notation given in IETF
        specification RFC 4291 for textual representations of IPv6
        addresses and IPv6 address prefixes (see sections 2.2 and 2.3).
        If a prefix-length is not specified, it is implicitly equal to
        128. The expected operations within OVAL for ipv6_address values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', 'less than or equal', 'subset of', and
        'superset of'. All operations are defined in terms of the value
        space. Let A and B be ipv6_address values (i.e. ordered pairs
        from the value space). The following definitions assume that
        bits outside the prefix have been zeroed out. By zeroing the low
        order bits, they are effectively ignored for all operations.
        Implementations of the following operations MUST behave as if
        this has been done. The following defines how to perform each
        operation for the ipv6_address datatype. Let P_addr mean the
        first element of ordered pair P and P_prefix mean the second
        element. equals: A equals B if and only if A_addr == B_addr and
        A_prefix == B_prefix. not equal: A is not equal to B if and only
        if they don't satisfy the criteria for operator "equals".
        greater than: A is greater than B if and only if A_prefix ==
        B_prefix and A_addr &gt; B_addr. If A_prefix != B_prefix, an
        error MUST be reported. greater than or equal: A is greater than
        or equal to B if and only if A_prefix == B_prefix and they
        satisfy either the criteria for operators "equal" or "greater
        than". If A_prefix != B_prefix, an error MUST be reported. less
        than: A is less than B if and only if A_prefix == B_prefix and
        they don't satisfy the criteria for operator "greater than or
        equal". If A_prefix != B_prefix, an error MUST be reported. less
        than or equal: A is less than or equal to B if and only if
        A_prefix == B_prefix and they don't satisfy the criteria for
        operator "greater than". If A_prefix != B_prefix, an error MUST
        be reported. subset of: A is a subset of B if and only if every
        IPv6 address in subnet A is present in subnet B. In other words,
        A_prefix &gt;= B_prefix and the high B_prefix bits of A_addr and
        B_addr are equal. superset of: A is a superset of B if and only
        if B is a subset of A.
    """

    IPV4_ADDRESS = "ipv4_address"
    IPV6_ADDRESS = "ipv6_address"


class FlagEnumeration(Enum):
    """The FlagEnumeration simple type defines the valid flags associated with a
    collected object.

    These flags are meant to provide information about how the specified
    object was handled by the data collector. In order to evaluate an
    OVAL Definition, information about the defined objects needs to be
    available. The flags help detail the outcome of attempting to
    collect information related to these objects..

    :cvar ERROR: A flag of 'error' indicates that there was an error
        trying to identify items on the system that match the specified
        object declaration. This flag is not meant to be used when there
        was an error retrieving a specific entity, but rather when it
        could not be determined if an item exists or not. Any error in
        retrieving a specific entity should be represented by setting
        the status of that specific entity to 'error'.
    :cvar COMPLETE: A flag of 'complete' indicates that every matching
        item on the system has been identified and is represented in the
        system characteristics file. It can be assumed that no
        additional matching items exist on the system.
    :cvar INCOMPLETE: A flag of 'incomplete' indicates that a matching
        item exists on the system, but only some of the matching items
        have been identified and are represented in the system
        characteristics file. It is unknown if additional matching items
        also exist. Note that with a flag of 'incomplete', each item
        that has been identified  matches the object declaration, but
        additional items might also exist on the system.
    :cvar DOES_NOT_EXIST: A flag of 'does not exist' indicates that the
        underlying structure is installed on the system but no matching
        item was found. For example, the Windows metabase is installed
        but there were no items that matched the metabase_object. In
        this example, if the metabase itself was not installed, then the
        flag would have been 'not applicable'.
    :cvar NOT_COLLECTED: A flag of 'not collected' indicates that no
        attempt was made to collect items on the system. An object with
        this flag will produce an 'unknown' result during analysis since
        it is unknown if matching items exists on the system or not.
        This is different from an 'error' flag because an 'error' flag
        indicates that an attempt was made to collect items on system
        whereas a 'not collected' flag indicates that an attempt was not
        made to collect items on the system.
    :cvar NOT_APPLICABLE: A flag of 'not applicable' indicates that the
        specified object is not applicable to the system being
        characterized. This could be because the data repository is not
        installed or that the object structure is for a different flavor
        of systems. An example would be trying to collect objects
        related to a Red Hat system off of a Windows system. Another
        example would be trying to collect an rpminfo_object on a Linux
        system if the rpm packaging system is not installed. If the rpm
        packaging system is installed and the specified rpminfo_object
        could not be found, then the flag would be 'does not exist'.
    """

    ERROR = "error"
    COMPLETE = "complete"
    INCOMPLETE = "incomplete"
    DOES_NOT_EXIST = "does not exist"
    NOT_COLLECTED = "not collected"
    NOT_APPLICABLE = "not applicable"


@dataclass
class InterfaceType:
    """The InterfaceType complex type is used to describe an existing network
    interface on the system.

    This information can help identify a specific system on a given
    network.

    :ivar interface_name: The required interface_name element is the
        name of the interface
    :ivar ip_address: The ipv4_address element holds the IPV4 address
        for the interface.
    :ivar ipv6_address: The ipv6_address element holds the IPV6 address
        for the interface.
    :ivar mac_address: The required mac_address element holds the MAC
        address for the interface. MAC addresses should be formatted
        according to the IEEE 802-2001 standard which states that a MAC
        address is a sequence of six octet values, separated by hyphens,
        where each octet is represented by two hexadecimal digits.
        Uppercase letters should also be used to represent the
        hexadecimal digits A through F.
    """

    interface_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    ip_address: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    ipv6_address: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    mac_address: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ReferenceType:
    """The ReferenceType complex type specifies an item in the system
    characteristics file.

    This reference is used to link global OVAL Objects to specific
    items.
    """

    item_ref: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


class StatusEnumeration(Enum):
    """
    The StatusEnumeration simple type defines the valid status messages associated
    with collection of specific information associated with an item.

    :cvar ERROR: A status of 'error' says that there was an error
        collecting information associated with an item as a whole or any
        specific entity. An item would have a status of 'error' if a
        problem occurred that prevented the item from being collected.
        For example, a file_item would have a status of 'error' if a
        handle to the file could not be opened because the handle was
        already in use by another program. See the documentation for
        ItemType for information about when an item entity status of
        'error' should propagate up to the item status level.
    :cvar EXISTS: A status of 'exists' says that the item or specific
        piece of information exists on the system and has been
        collected.
    :cvar DOES_NOT_EXIST: A status of 'does not exist' says that the
        item or specific piece of information does not exist and
        therefore has not been collected. This status assumes that an
        attempt was made to collect the information, but the information
        just does not exist. This can happen when a certain entity is
        only pertinent to particular instances or if the information for
        that entity is not set.
    :cvar NOT_COLLECTED: A status of 'not collected' says that no
        attempt was made to collect the item or specific piece of
        information so it is unknown what the value is and if it even
        exists.
    """

    ERROR = "error"
    EXISTS = "exists"
    DOES_NOT_EXIST = "does not exist"
    NOT_COLLECTED = "not collected"


@dataclass
class VariableValueType:
    """The VariableValueType complex type holds the value to a variable used during
    the collection of an object.

    The required variable_id attribute is the unique id of the variable
    being identified.
    """

    value: Optional[object] = field(default=None)
    variable_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:var:[1-9][0-9]*",
        },
    )


@dataclass
class EntityItemComplexBaseType:
    """
    The EntityItemComplexBaseType complex type is an abstract type that serves as
    the base type for all complex item entities.

    :ivar datatype: The optional datatype attribute determines the type
        of data expected (the default datatype is 'string'). Note that
        the datatype attribute simply defines the type of data as found
        on the system, it is not used during evaluation. An OVAL
        Definition defines how the data should be interpreted during
        analysis. If the definition states a datatype that is different
        than what the system characteristics presents, then a type cast
        must be made.
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
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """

    datatype: DatatypeEnumeration = field(
        default=DatatypeEnumeration.STRING,
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
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EntityItemFieldType:
    """The EntityItemFieldType defines an element with simple content that
    represents a named field in a record that may contain any number of named
    fields.

    The EntityItemFieldType is much like all other entities with one
    significant difference, the EntityItemFieldType has a name
    attribute. The required name attribute specifies a name for the
    field. Field names are lowercase and may occur more than once to
    allow for a field to have multiple values. Note that when the mask
    attribute is set to 'true' on a field's parent element the field
    must be masked regardless of the field's mask attribute value.

    :ivar value:
    :ivar name: A string restricted to disallow upper case characters.
    :ivar datatype: The optional datatype attribute determines the type
        of data expected (the default datatype is 'string'). Note that
        the datatype attribute simply defines the type of data as found
        on the system, it is not used during evaluation. An OVAL
        Definition defines how the data should be interpreted during
        analysis. If the definition states a datatype that is different
        than what the system characteristics presents, then a type cast
        must be made.
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
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """

    value: Optional[object] = field(default=None)
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^A-Z]+",
        },
    )
    datatype: DatatypeEnumeration = field(
        default=DatatypeEnumeration.STRING,
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
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EntityItemSimpleBaseType:
    """
    The EntityItemSimpleBaseType complex type is an abstract type that serves as
    the base type for all simple item entities.

    :ivar value:
    :ivar datatype: The optional datatype attribute determines the type
        of data expected (the default datatype is 'string'). Note that
        the datatype attribute simply defines the type of data as found
        on the system, it is not used during evaluation. An OVAL
        Definition defines how the data should be interpreted during
        analysis. If the definition states a datatype that is different
        than what the system characteristics presents, then a type cast
        must be made.
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
    :ivar status: The optional status attribute holds information
        regarding the success of the data collection. For example, if
        there was an error collecting a particular piece of data, then
        the status would be 'error'.
    """

    value: Optional[object] = field(default=None)
    datatype: DatatypeEnumeration = field(
        default=DatatypeEnumeration.STRING,
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
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class InterfacesType:
    """The InterfacesType complex type is a container for zero or more interface
    elements.

    Each interface element is used to describe an existing network
    interface on the system.

    :ivar interface: Please refer to the description of the
        InterfaceType for more information.
    """

    interface: list[InterfaceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class ItemType:
    """The ItemType complex type specifies an optional message element that is used
    to pass things like error messages during data collection to a tool that will
    utilize the information.

    The required id attribute is a unique (to the file) identifier that
    allows the specific item to be referenced. The required status
    attribute holds information regarding the success of the data
    collection. For example, if an item exists on the system then the
    status would reflect this with a value of 'exists'. If an error
    occurs which is not associated with any item entities, or if an
    error occurs that is associated with an item entity matching an
    associated object entity, then the status would be 'error'. An error
    specific to any particular entity should be addressed at the entity
    level and, for item entities not associated with an object entity,
    not the item level. When creating items, any entities that can
    successfully be collected should be reported. In some cases, when an
    item for a specified object does not exist, it may be beneficial to
    report a partial match of an item showing what entities did exist
    and what entities did not exist for debugging purposes. This is
    especially true when considering items that are collected by objects
    with hierarchical object entities. An example of such a case is when
    a file_object has a path entity equal to 'C:\\' and a filename
    entity equal to 'test.txt' where 'test.txt' does not exist in the
    'C:\\' directory. This would result in the creation of a partially
    matching file_item with a status of 'does not exist' where the path
    entity equals 'C:\\' and the filename entity equals 'test.txt' with
    a status of 'does not exist'. By showing the partial match, someone
    reading a system-characteristics document can quickly see that a
    matching file_item did not exist because the specified filename did
    not exist and not that the specified path did not exist. Again,
    please note that the implementation of partial matches, when an item
    for a specified object does not exist,  is completely optional.
    """

    message: list[MessageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 50,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.EXISTS,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ObjectType:
    """The ObjectType complex type provides a reference between items collected and
    a related global OVAL Object.

    If an OVAL Object does not exist on the system, then an object
    element is still provided but with the flag attribute set to 'does
    not exist'. For details on how to handle items, when an OVAL Object
    does not exist on the system, please see the ItemType documentation.
    This shows that the object was looked for but not found on the
    system. If no object element is written in this case, users of the
    system characteristics file will not know whether the object was not
    found or no attempt was made to collect it. The required id
    attribute is the id of the global OVAL Object. The required version
    attribute is the specific version of the global OVAL Object that was
    used by the data collection engine. The version is necessary so that
    analysis using a system characteristics file knows exactly what was
    collected. The optional variable_instance identifier is a unique id
    that differentiates each unique instance of an object. Capabilities
    that use OVAL may reference the same definition multiple times and
    provide different variable values each time the definition is
    referenced. This will result in multiple instances of an object
    being included in the OVAL System Characteristics file (definitions
    that do not use variables can only have one unique instance). The
    inclusion of this unique instance identifier allows the OVAL Results
    document to associate the correct objects and items for each
    combination of supplied values. The optional comment attribute
    provides a short description of the object. The required flag
    attribute holds information regarding the outcome of the data
    collection. For example, if there was an error looking for items
    that match the object specification, then the flag would be 'error'.
    Please refer to the description of FlagEnumeration for details about
    the different flag values.

    :ivar message: The optional message element holds an error message
        or some other string that the data collection engine wishes to
        pass along.
    :ivar variable_value: The optional variable_value elements define
        the actual value(s) used during data collection of any variable
        referenced by the object (as well as any object referenced via a
        set element). An OVAL Object that includes a variable maybe have
        a different unique set of matching items depending on the value
        assigned to the variable. A tool that is given an OVAL System
        Characteristics file in order to analyze an OVAL Definition
        needs to be able to determine the exact instance of an object to
        use based on the variable values supplied. If a variable
        represents a collection of values, then multiple variable_value
        elements would exist with the same variable_id attribute.
    :ivar reference: The optional reference element links the collected
        item found by the data collection engine and the global OVAL
        Object. A global OVAL Object my have multiple matching items on
        a system. For example a global file object that is a pattern
        match might match 10 different files on a specific system. In
        this case, there would be 10 reference elements, one for each of
        the files found on the system.
    :ivar id:
    :ivar version:
    :ivar variable_instance:
    :ivar comment:
    :ivar flag:
    """

    message: list[MessageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    variable_value: list[VariableValueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    reference: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:obj:[1-9][0-9]*",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    variable_instance: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    flag: Optional[FlagEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )



@dataclass
class CollectedObjectsType:
    """The CollectedObjectsType complex type states all the objects that have been
    collected by the system characteristics file.

    The details of each object are defined by the global OVAL object
    that is identified by the id.
    """

    object_value: list[ObjectType] = field(
        default_factory=list,
        metadata={
            "name": "object",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )


@dataclass
class EntityItemAnySimpleType(EntityItemSimpleBaseType):
    """The EntityItemAnySimpleType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes any simple data.
    """

    value: str = field(default="")
    datatype: SimpleDatatypeEnumeration = field(
        default=SimpleDatatypeEnumeration.STRING,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EntityItemBinaryType(EntityItemSimpleBaseType):
    """The EntityItemBinaryType type is extended by the entities of an individual
    item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes simple binary data. The empty string is also allowed for
    cases where there was an error in the data collection of an entity
    and a status needs to be reported.
    """

    value: Union[bytes, str] = field(
        default=b"",
        metadata={
            "max_length": 0,
            "format": "base16",
        },
    )
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.BINARY,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EntityItemBoolType(EntityItemSimpleBaseType):
    """The EntityItemBoolType type is extended by the entities of an individual
    item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes simple boolean data. The empty string is also allowed for
    cases where there was an error in the data collection of an entity
    and a status needs to be reported.
    """

    value: Union[bool, str] = field(
        default="",
        metadata={
            "max_length": 0,
        },
    )
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.BOOLEAN,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EntityItemDebianEvrstringType(EntityItemSimpleBaseType):
    """The EntityItemDebianEVRStringType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the attributes found in the EntityItemSimpleBaseType. This type represents the epoch, upstream_version, and debian_revision fields, for a Debian package, as a single version string. It has the form "EPOCH:UPSTREAM_VERSION-DEBIAN_REVISION". Note that a null epoch (or '(none)' as returned by dpkg) is equivalent to '0' and would hence have the form 0:UPSTREAM_VERSION-DEBIAN_REVISION. Comparisons involving this datatype should follow the algorithm outlined in Chapter 5 of the "Debian Policy Manual" (https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-Version). An implementation of this is the cmpversions() function in dpkg's enquiry.c.
    """

    class Meta:
        name = "EntityItemDebianEVRStringType"

    value: str = field(default="")
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.DEBIAN_EVR_STRING,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EntityItemEvrstringType(EntityItemSimpleBaseType):
    """The EntityItemEVRStringType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This type
    represents the epoch, version, and release fields, for an RPM
    package, as a single version string. It has the form "EPOCH:VERSION-
    RELEASE". Note that a null epoch (or '(none)' as returned by rpm) is
    equivalent to '0' and would hence have the form 0:VERSION-RELEASE.
    Comparisons involving this datatype should follow the algorithm of
    librpm's rpmvercmp() function.
    """

    class Meta:
        name = "EntityItemEVRStringType"

    value: str = field(default="")
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.EVR_STRING,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EntityItemFilesetRevisionType(EntityItemSimpleBaseType):
    """The EntityItemFilesetRevisionType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    represents the version string related to filesets in HP-UX.
    """

    value: str = field(default="")
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.FILESET_REVISION,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EntityItemFloatType(EntityItemSimpleBaseType):
    """The EntityItemFloatType type is extended by the entities of an individual
    item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes simple float data. The empty string is also allowed for
    cases where there was an error in the data collection of an entity
    and a status needs to be reported.
    """

    value: Union[float, str] = field(
        default="",
        metadata={
            "max_length": 0,
        },
    )
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.FLOAT,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EntityItemIosversionType(EntityItemSimpleBaseType):
    """The EntityItemIOSVersionType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    represents the version string for IOS.
    """

    class Meta:
        name = "EntityItemIOSVersionType"

    value: str = field(default="")
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.IOS_VERSION,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EntityItemIpaddressStringType(EntityItemSimpleBaseType):
    """The EntityItemIPAddressStringType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes any IPv4/IPv6 address, address prefix, or its string
    representation.
    """

    class Meta:
        name = "EntityItemIPAddressStringType"

    value: str = field(default="")
    datatype: EntityItemIpaddressStringTypeDatatype = field(
        default=EntityItemIpaddressStringTypeDatatype.STRING,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EntityItemIpaddressType(EntityItemSimpleBaseType):
    """The EntityItemIPAddressType type is extended by the entities of an
    individual item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes any IPv4/IPv6 address or address prefix.
    """

    class Meta:
        name = "EntityItemIPAddressType"

    value: str = field(default="")
    datatype: Optional[EntityItemIpaddressTypeDatatype] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EntityItemIntType(EntityItemSimpleBaseType):
    """The EntityItemIntType type is extended by the entities of an individual
    item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes simple integer data. The empty string is also allowed for
    cases where there was an error in the data collection of an entity
    and a status needs to be reported.
    """

    value: Union[int, str] = field(
        default="",
        metadata={
            "max_length": 0,
        },
    )
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.INT,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EntityItemRecordType(EntityItemComplexBaseType):
    """The EntityItemRecordType defines an entity that consists of a number of
    named fields.

    This structure is used for representing a record from a database
    query and other similar structures where multiple related fields
    must be collected at once. Note that for all entities of this type,
    the only allowed datatype is 'record'. Note the datatype attribute
    must be set to 'record'. Note that when the mask attribute is set to
    'true', all child field elements must be masked regardless of the
    child field's mask attribute value.
    """

    field_value: list[EntityItemFieldType] = field(
        default_factory=list,
        metadata={
            "name": "field",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class EntityItemStringType(EntityItemSimpleBaseType):
    """The EntityItemStringType type is extended by the entities of an individual
    item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes simple string data.
    """

    value: str = field(default="")
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.STRING,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EntityItemVersionType(EntityItemSimpleBaseType):
    """The EntityItemVersionType type is extended by the entities of an individual
    item.

    This type provides uniformity to each entity by including the
    attributes found in the EntityItemSimpleBaseType. This specific type
    describes version data.
    """

    value: str = field(default="")
    datatype: SimpleDatatypeEnumeration = field(
        init=False,
        default=SimpleDatatypeEnumeration.VERSION,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SystemInfoType:
    """The SystemInfoType complex type specifies general information about the
    system that data was collected from, including information that can be used to
    identify the system.

    See the description of the InterfacesType complex type for more
    information. Note that the high level interfaces is required due to
    the inclusion of the xsd:any tag that follows it. The interfaces tag
    can be empty if no single interface is present. Additional system
    information is also allowed although it is not part of the official
    OVAL Schema. Individual organizations can place system information
    that they feel is important and these will be skipped during the
    validation. All OVAL really cares about is that the required system
    information items are there.

    :ivar os_name: The required os_name elements describes the operating
        system of the machine the data was collected on.
    :ivar os_version: The required os_version elements describe the
        operating system version of the machine the data was collected
        on.
    :ivar architecture: The required architecture element describes the
        hardware architecture type of the system data was collected on.
    :ivar primary_host_name: The required primary_host_name element is
        the primary host name of the machine the data was collected on.
    :ivar interfaces: The required interfaces element outlines the
        network interfaces that exist on the system.
    :ivar any_element: The Asset Identification specification
        (http://scap.nist.gov/specifications/ai/) provides a
        standardized way of reporting asset information across different
        organizations. The information contained within an AI computing-
        device element is similar to the information collected by OVAL's
        SystemInfoType. To support greater interoperability, an
        ai:computing-device element describing the system that data was
        collected from may appear at this point in an OVAL System
        Characteristics document.
    """

    os_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    os_version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    architecture: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    primary_host_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    interfaces: Optional[InterfacesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Item(ItemType):
    """The abstract item element holds information about a specific item on a
    system.

    An item might be a file, a rpm, a process, etc. This element is
    extended by the different component schemas through substitution
    groups. Each item represents a unique instance of an object as
    specified by an OVAL Object. For example, a single file or a single
    user. Each item may be referenced by more than one object in the
    collected object section. Please refer to the description of
    ItemType for more details about the information stored in items.
    """

    class Meta:
        name = "item"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5"
        )


@dataclass
class OvalSystemCharacteristics:
    """The system_characteristics element is the root of an OVAL System
    Characteristics Document, and must occur exactly once.

    Its purpose is to bind together the four major sections of a system characteristics file - generator, system_info, collected_objects, and system_data - which are the children of the oval_system_characteristics element.

    :ivar generator: The generator section must be present and provides
        information about when the system characteristics file was
        compiled and under what version.
    :ivar system_info: The required system_info element is used to
        record information about the system being described.
    :ivar collected_objects: The optional collected_objects section is
        used to associated the ids of the OVAL Objects collected with
        the system characteristics items that have been defined. The
        collected_objects section provides a listing of all the objects
        used to generate this system characteristics file.
    :ivar system_data: The optional system_data section defines the
        specific characteristics that have been collected from the
        system.
    :ivar signature: The optional Signature element allows an XML
        Signature as defined by the W3C to be attached to the document.
        This allows authentication and data integrity to be provided to
        the user. Enveloped signatures are supported. More information
        about the official W3C Recommendation regarding XML digital
        signatures can be found at http://www.w3.org/TR/xmldsig-core/.
    """

    class Meta:
        name = "oval_system_characteristics"
        namespace = (
            "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5"
        )

    generator: Optional[GeneratorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    system_info: Optional[SystemInfoType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    collected_objects: Optional[CollectedObjectsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    system_data: Optional[ItemType] = field(
        default=None,
        metadata={
            "type": "Elements",
            "namespace": "",
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
