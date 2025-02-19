from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Union

from oval.definitions.oval_common_schema import (
    CheckEnumeration,
    ClassEnumeration,
    DatatypeEnumeration,
    ExistenceEnumeration,
    FamilyEnumeration,
    GeneratorType,
    NotesType,
    OperationEnumeration,
    OperatorEnumeration,
    SimpleDatatypeEnumeration,
)
from oval.definitions.oval_common_schema import (
    Notes as OvalCommonSchemaNotes,
)
from oval.definitions.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


class ArithmeticEnumeration(Enum):
    """The ArithmeticEnumeration simple type defines basic arithmetic operations.

    Currently add and multiply are defined.
    """

    ADD = "add"
    MULTIPLY = "multiply"


@dataclass
class CriterionType:
    """The CriterionType complex type identifies a specific test to be included in
    the definition's criteria.

    The required test_ref attribute is the actual id of the test being
    referenced. The optional negate attribute signifies that the result
    of an individual test should be negated during analysis. For
    example, consider a test that evaluates to TRUE if a specific patch
    is installed. By negating this test, it now evaluates to TRUE if the
    patch is NOT installed. The optional comment attribute provides a
    short description of the specified test and should mirror the
    comment attribute of the actual test. The optional
    applicability_check attribute provides a Boolean flag that when true
    indicates that the criterion is being used to determine whether the
    OVAL Definition applies to a given system.
    """

    applicability_check: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    test_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:tst:[1-9][0-9]*",
        },
    )
    negate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 1,
        },
    )


class DateTimeFormatEnumeration(Enum):
    """The DateTimeFormatEnumeration simple type defines the different date-time
    formats that are understood by OVAL.

    Note that in some cases there are a few different possibilities
    within a given format. Each of these possibilities is unique though
    and can be distinguished from each other. The different formats are
    used to clarify the higher level structure of the date-time string
    being used.

    :cvar YEAR_MONTH_DAY: The year_month_day value specifies date-time
        strings that follow the formats: 'yyyymmdd', 'yyyymmddThhmmss',
        'yyyy/mm/dd hh:mm:ss', 'yyyy/mm/dd', 'yyyy-mm-dd hh:mm:ss', or
        'yyyy-mm-dd'
    :cvar MONTH_DAY_YEAR: The month_day_year value specifies date-time
        strings that follow the formats: 'mm/dd/yyyy hh:mm:ss',
        'mm/dd/yyyy', 'mm-dd-yyyy hh:mm:ss', 'mm-dd-yyyy', 'NameOfMonth,
        dd yyyy hh:mm:ss' or 'NameOfMonth, dd yyyy',
        'AbreviatedNameOfMonth, dd yyyy hh:mm:ss', or
        'AbreviatedNameOfMonth, dd yyyy'
    :cvar DAY_MONTH_YEAR: The day_month_year value specifies date-time
        strings that follow the formats: 'dd/mm/yyyy hh:mm:ss',
        'dd/mm/yyyy', 'dd-mm-yyyy hh:mm:ss', or 'dd-mm-yyyy'
    :cvar WIN_FILETIME: The win_filetime value specifies date-time
        strings that follow the windows file time format.
    :cvar SECONDS_SINCE_EPOCH: The seconds_since_epoch value specifies
        date-time values that represent the time in seconds since the
        UNIX epoch.  The Unix epoch is the time 00:00:00 UTC on January
        1, 1970.
    :cvar CIM_DATETIME: The cim_datetime model is used by WMI and its
        value specifies date-time strings that follow the format:
        'yyyymmddHHMMSS.mmmmmmsUUU', and alternatively 'yyyy-mm-dd
        HH:MM:SS:mmm' only when used in WMI Query Language queries.
    """

    YEAR_MONTH_DAY = "year_month_day"
    MONTH_DAY_YEAR = "month_day_year"
    DAY_MONTH_YEAR = "day_month_year"
    WIN_FILETIME = "win_filetime"
    SECONDS_SINCE_EPOCH = "seconds_since_epoch"
    CIM_DATETIME = "cim_datetime"


class EntityObjectIpaddressStringTypeDatatype(Enum):
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


class EntityObjectIpaddressTypeDatatype(Enum):
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


class EntityStateIosversionTypeDatatype(Enum):
    """
    :cvar IOS_VERSION: The ios_version datatype describes Cisco IOS
        Train strings. These are in essence version strings for IOS.
        Please refer to Cisco's IOS Reference Guide for information on
        how to compare different Trains as they follow a very specific
        pattern. Expected operations within OVAL for ios_version values
        are 'equals', 'not equal', 'greater than', 'greater than or
        equal', 'less than', and 'less than or equal'.
    :cvar STRING: The string datatype describes standard string data.
        This datatype conforms to the W3C Recommendation for string
        data.  Expected operations within OVAL for string values are
        'equals', 'not equal', 'case insensitive equals', 'case
        insensitive not equal', 'pattern match'.
    """

    IOS_VERSION = "ios_version"
    STRING = "string"


class EntityStateIpaddressStringTypeDatatype(Enum):
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


class EntityStateIpaddressTypeDatatype(Enum):
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


@dataclass
class ExtendDefinitionType:
    """The ExtendDefinitionType complex type allows existing definitions to be
    extended by another definition.

    This works by evaluating the extended definition and then using the
    result within the logical context of the extending definition. The
    required definition_ref attribute is the actual id of the definition
    being extended. The optional negate attribute signifies that the
    result of an extended definition should be negated during analysis.
    For example, consider a definition that evaluates TRUE if
    certainsoftware is installed. By negating the definition, it now
    evaluates to TRUE if the software is NOT installed. The optional
    comment attribute provides a short description of the specified
    definition and should mirror the title metadata of the extended
    definition. The optional applicability_check attribute provides a
    Boolean flag that when true indicates that the extend_definition is
    being used to determine whether the OVAL Definition applies to a
    given system.
    """

    applicability_check: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    definition_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:def:[1-9][0-9]*",
        },
    )
    negate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 1,
        },
    )


class FilterActionEnumeration(Enum):
    """
    The FilterActionEnumeration simple type defines the different options for
    filtering sets of items.

    :cvar EXCLUDE: The exclude value specifies that all items that match
        the filter shall be excluded from set that the filter is applied
        to.
    :cvar INCLUDE: The include value specifies that only items that
        match the filter shall be included in the set that the filter is
        applied to.
    """

    EXCLUDE = "exclude"
    INCLUDE = "include"


@dataclass
class ObjectComponentType:
    """The ObjectComponentType complex type defines a specific value or set of
    values on the local system to obtain.

    The required object_ref attribute provides a reference to an
    existing OVAL Object declaration. The referenced OVAL Object
    specifies a set of OVAL Items to collect. Note that an OVAL Object
    might identify 0, 1, or many OVAL Items on a system. If no items are
    found on the system then an error should be reported when
    determining the value of an ObjectComponentType. If 1 or more OVAL
    Items are found then each OVAL Item will be considered and the
    ObjectComponentType may have one or more values. The required
    item_field attribute specifies the name of the entity whose value
    will be retrieved from each OVAL Item collected by the referenced
    OVAL Object. For example, if the object_ref references a win-
    def:file_object, the item_field may specify the 'version' entity as
    the field to use as the value of the ObjectComponentType. Note that
    an OVAL Item may have 0, 1, or many entities whose name matches the
    specified item_field value. If an entity is not found with a name
    that matches the value of the item_field an error should be reported
    when determining the value of an ObjectComponentType. If 1 or more
    matching entities are found in a single OVAL Item the value of the
    ObjectComponentType is the list of the values from each of the
    matching entities. The optional record_field attribute specifies the
    name of a field in a record entity in an OVAL Item. The record_field
    attribute allows the value of a specific field to be retrieved from
    an entity with a datatype of 'record'. If a field with a matching
    name attribute value is not found in the referenced OVAL Item entity
    an error should be reported when determining the value of the
    ObjectComponentType.
    """

    object_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:obj:[1-9][0-9]*",
        },
    )
    item_field: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 1,
        },
    )
    record_field: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 1,
        },
    )


@dataclass
class ObjectRefType:
    """The ObjectRefType complex type defines an object reference to be used by
    OVAL Tests that are defined in the component schemas.

    The required object_ref attribute specifies the id of the OVAL
    Object being referenced.
    """

    object_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:obj:[1-9][0-9]*",
        },
    )


class OrderEnumeration(Enum):
    """The OrderEnumeration simple type defines the direction in which data should
    be sorted, and works to support the SortEnumeration.

    The OrderEnumeration has no impact on the SortEnumeration of
    'document'.

    :cvar ASCENDING: Numbers: Arranged from smallest to largest, such as
        0, 1, 2, 3, 4, 5, 6. Letters: Arranged alphabetically from A to
        Z
    :cvar DESCENDING: Numbers: Arranged from largest to smallest, such
        as 9, 8, 7, 6. Letters: Arranged alphabetically from Z to A
    """

    ASCENDING = "ascending"
    DESCENDING = "descending"


@dataclass
class PossibleValueType:
    """The PossibleValueType complex type is used to outline a single expected
    value of an external variable.

    The required hint attribute gives a short description of what the
    value means or represents.
    """

    value: Optional[object] = field(default=None)
    hint: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ReferenceType:
    """The ReferenceType complex type links the OVAL Definition to a definitive
    external reference.

    For example, CVE Identifiers are used for referencing
    vulnerabilities. The intended purpose for this reference is to link
    the definition to a variety of other sources that address the same
    issue being specified by the OVAL Definition. The required source
    attribute specifies where the reference is coming from. In other
    words, it identifies the reference repository being used. The
    required ref_id attribute is the external id of the reference. The
    optional ref_url attribute is the URL to the reference.
    """

    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ref_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    ref_url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class SetOperatorEnumeration(Enum):
    """The SetOperatorEnumeration simple type defines acceptable set operations.

    Set operations are used to take multiple different sets of objects
    within OVAL and merge them into a single unique set. The different
    operators that guide this merge are defined below. For each
    operator, if only a single object has been supplied, then the
    resulting set is simply that complete object.

    :cvar COMPLEMENT: The complement operator is defined in OVAL as a
        relative complement. The resulting unique set contains
        everything that belongs to the first declared set that is not
        part of the second declared set. If A and B are sets (with A
        being the first declared set), then the relative complement is
        the set of elements in A, but not in B, with the duplicates
        removed.
    :cvar INTERSECTION: The intersection of two sets in OVAL results in
        a unique set that contains everything that belongs to both sets
        in the collection, but nothing else. If A and B are sets, then
        the intersection of A and B contains all the elements of A that
        also belong to B, but no other elements, with the duplicates
        removed.
    :cvar UNION: The union of two sets in OVAL results in a unique set
        that contains everything that belongs to either of the original
        sets. If A and B are sets, then the union of A and B contains
        all the elements of A and all elements of B, with the duplicates
        removed.
    """

    COMPLEMENT = "COMPLEMENT"
    INTERSECTION = "INTERSECTION"
    UNION = "UNION"


class SortEnumeration(Enum):
    """The SortEnumeration simple type defines basic sorting operations.

    Currently 'document', 'lexical', 'numeric' and 'natural' are
    defined.

    :cvar DOCUMENT: No sorting is performed, the values will remain in
        the order they came in as, and match the order in which the
        referenced system characterics will appear in the OVAL results
        XML document.
    :cvar LEXICAL: Sort alphabetically, useful for pure string lists.
    :cvar NUMERIC: Sort numerically, useful for lists of numbers or
        lists of integers or floats, but will cause errors if string
        data is present.
    :cvar NATURAL: Perform a 'natural' sort, refer to
        https://en.wikipedia.org/wiki/Natural_sort_order
    """

    DOCUMENT = "document"
    LEXICAL = "lexical"
    NUMERIC = "numeric"
    NATURAL = "natural"


@dataclass
class StateRefType:
    """The StateRefType complex type defines a state reference to be used by OVAL
    Tests that are defined in the component schemas.

    The required state_ref attribute specifies the id of the OVAL State
    being referenced.
    """

    state_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:ste:[1-9][0-9]*",
        },
    )


@dataclass
class ValueType:
    """The ValueType complex type holds the actual value of the variable when
    dealing with a constant variable.

    This value should be used by all tests that reference this variable.
    The value cannot be over-ridden by an external source.
    """

    value: Optional[object] = field(default=None)


@dataclass
class VariableComponentType:
    """The VariableComponentType complex type defines a specific value obtained by
    looking at the value of another OVAL Variable.

    The required var_ref attribute provides a reference to the variable.
    One must make sure that the variable reference does not point to the
    parent variable that uses this component to avoid a race condition.
    """

    var_ref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:var:[1-9][0-9]*",
        },
    )


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
            "namespace": "",
        },
    )
    product: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    family: Optional[FamilyEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class CriteriaType:
    """The CriteriaType complex type describes a container for a set of sub
    criteria, criteria, criterion, or extend_definition elements allowing complex
    logical trees to be constructed.

    Each referenced test is represented by a criterion element. Please
    refer to the description of the CriterionType for more information
    about and individual criterion element. The optional
    extend_definition element allows existing definitions to be included
    in the criteria. Refer to the description of the
    ExtendDefinitionType for more information. The required operator
    attribute provides the logical operator that binds the different
    statements inside a criteria together. The optional negate attribute
    signifies that the result of the criteria as a whole should be
    negated during analysis. For example, consider a criteria that
    evaluates to TRUE if certain software is installed. By negating this
    test, it now evaluates to TRUE if the software is NOT installed. The
    optional comment attribute provides a short description of the
    criteria. The optional applicability_check attribute provides a
    Boolean flag that when true indicates that the criteria is being
    used to determine whether the OVAL Definition applies to a given
    system.
    """

    criteria: list["CriteriaType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    criterion: list[CriterionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    extend_definition: list[ExtendDefinitionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    applicability_check: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    operator: OperatorEnumeration = field(
        default=OperatorEnumeration.AND,
        metadata={
            "type": "Attribute",
        },
    )
    negate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 1,
        },
    )


@dataclass
class EntityComplexBaseType:
    """The EntityComplexBaseType complex type is an abstract type that defines the
    default attributes associated with every complex entity.

    Entities can be found in both OVAL Objects and OVAL States and
    represent the individual properties associated with items found on a
    system. An example of a single entity would be the path of a file.
    Another example would be the version of the file.

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


@dataclass
class EntityObjectFieldType:
    """The EntityObjectFieldType defines an element with simple content that
    represents a named field in a record that may contain any number of named
    fields.

    The EntityObjectFieldType is much like all other entities with one
    significant difference, the EntityObjectFieldType has a name
    attribute The required name attribute specifies a unique name for
    the field. Field names are lowercase and must be unique within a
    given parent record element. When analyzing system characteristics
    an error should be reported for the result of a field that is
    present in the OVAL State, but not found in the system
    characteristics Item. The optional entity_check attribute specifies
    how to handle multiple record fields with the same name in the OVAL
    Systems Characteristics file. For example, while collecting group
    information where one field is the represents the users that are
    members of the group.  It is very likely that there will be multiple
    fields with a name of 'user' associated with the group.  If the OVAL
    State defines the value of the field with name equal 'user' to equal
    'Fred', then the entity_check attribute determines if all values for
    field entities must be equal to 'Fred', or at least one value must
    be equal to 'Fred', etc. Note that when the mask attribute is set to
    'true' on a field's parent element the field must be masked
    regardless of the field's mask attribute value.

    :ivar value:
    :ivar name: A string restricted to disallow upper case characters.
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
    :ivar entity_check:
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
    entity_check: CheckEnumeration = field(
        default=CheckEnumeration.ALL,
        metadata={
            "type": "Attribute",
        },
    )


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


@dataclass
class EntityStateFieldType:
    """The EntityStateFieldType defines an element with simple content that
    represents a named field in a record that may contain any number of named
    fields.

    The EntityStateFieldType is much like all other entities with one
    significant difference, the EntityStateFieldType has a name
    attribute The required name attribute specifies a unique name for
    the field. Field names are lowercase and must be unique within a
    given parent record element. When analyzing system characteristics
    an error should be reported for the result of a field that is
    present in the OVAL State, but not found in the system
    characteristics Item. The optional entity_check attribute specifies
    how to handle multiple record fields with the same name in the OVAL
    Systems Characteristics file. For example, while collecting group
    information where one field is the represents the users that are
    members of the group.  It is very likely that there will be multiple
    fields with a name of 'user' associated with the group.  If the OVAL
    State defines the value of the field with name equal 'user' to equal
    'Fred', then the entity_check attribute determines if all values for
    field entities must be equal to 'Fred', or at least one value must
    be equal to 'Fred', etc. Note that when the mask attribute is set to
    'true' on a field's parent element the field must be masked
    regardless of the field's mask attribute value.

    :ivar value:
    :ivar name: A string restricted to disallow upper case characters.
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
    :ivar entity_check:
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
    entity_check: CheckEnumeration = field(
        default=CheckEnumeration.ALL,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LiteralComponentType:
    """The LiteralComponentType complex type defines a literal value to be used as
    a component.

    The optional datatype attribute defines the type of data expected.
    The default datatype is 'string'.
    """

    value: Optional[object] = field(default=None)
    datatype: SimpleDatatypeEnumeration = field(
        default=SimpleDatatypeEnumeration.STRING,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RestrictionType:
    """The RestrictionType complex type outlines a restriction that is placed on
    expected values for an external variable.

    For example, a possible value may be restricted to a integer less
    than 10. Please refer to the operationEnumeration simple type for a
    description of the valid operations.
    """

    value: Optional[object] = field(default=None)
    operation: Optional[OperationEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Filter:
    """The filter element provides a reference to an existing OVAL State and
    includes an optional action attribute.

    The action attribute is used to specify whether items that match the
    referenced OVAL State will be included in the resulting set or
    excluded from the resulting set.
    """

    class Meta:
        name = "filter"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:ste:[1-9][0-9]*",
        },
    )
    action: FilterActionEnumeration = field(
        default=FilterActionEnumeration.EXCLUDE,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Notes(NotesType):
    """The notes element is a container for one or more note child elements.

    It exists for backwards-compatibility purposes, for the pre-5.11.0
    oval-def:NotesType, which has been replaced by the oval:notes
    element in 5.11.1.
    """

    class Meta:
        name = "notes"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class ArithmeticFunctionType:
    """The arithmetic function takes two or more integer or float components and
    performs a basic mathematical function on them.

    The result of this function is a single integer or float unless one
    of the components returns a collection of values. In this case the
    specified arithmetic function would be performed multiple times and
    the end result would also be a collection of values for the local
    variable. For example assume a local_variable specifies the
    arithmetic function with an arithmetic_operation of "add" and has
    two sub-components under this function: the first component returns
    "1" and "2", and the second component returns "3" and "4" and "5".
    The local_variable element would be evaluated to be a collection of
    six values: 1+3, 1+4, 1+5, 2+3, 2+4, and 2+5. Note that if both an
    integer and float components are used then the result is a float.
    """

    object_component: list[ObjectComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    variable_component: list[VariableComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    literal_component: list[LiteralComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    arithmetic: list["ArithmeticFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    begin: list["BeginFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    concat: list["ConcatFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    end: list["EndFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    escape_regex: list["EscapeRegexFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    split: list["SplitFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    substring: list["SubstringFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    time_difference: list["TimeDifferenceFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    regex_capture: list["RegexCaptureFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    unique: list["UniqueFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    count: list["CountFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    glob_to_regex: list["GlobToRegexFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    merge: list["MergeFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    arithmetic_operation: Optional[ArithmeticEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EntityObjectAnySimpleType(EntitySimpleBaseType):
    """The EntityObjectAnySimpleType type is extended by the entities of an
    individual OVAL Object.

    This type provides uniformity to each object entity by including the
    attributes found in the EntitySimpleBaseType. This specific type
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
class EntityObjectBinaryType(EntitySimpleBaseType):
    """The EntityBinaryType type is extended by the entities of an individual OVAL
    Object.

    This type provides uniformity to each object entity by including the
    attributes found in the EntitySimpleBaseType. This specific type
    describes simple binary data. The empty string is also allowed when
    using a variable reference with an element.
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
class EntityObjectBoolType(EntitySimpleBaseType):
    """The EntityBoolType type is extended by the entities of an individual OVAL
    Object.

    This type provides uniformity to each object entity by including the
    attributes found in the EntitySimpleBaseType. This specific type
    describes simple boolean data. The empty string is also allowed when
    using a variable reference with an element.
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
class EntityObjectFloatType(EntitySimpleBaseType):
    """The EntityObjectFloatType type is extended by the entities of an individual
    OVAL Object.

    This type provides uniformity to each object entity by including the
    attributes found in the EntitySimpleBaseType. This specific type
    describes simple float data. The empty string is also allowed when
    using a variable reference with an element.
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
class EntityObjectIpaddressStringType(EntitySimpleBaseType):
    """The EntityObjectIPAddressStringType type is extended by the entities of an
    individual OVAL Object.

    This type provides uniformity to each object entity by including the
    attributes found in the EntitySimpleBaseType. This specific type
    describes any IPv4/IPv6 address, address prefix, or its string
    representation.
    """

    class Meta:
        name = "EntityObjectIPAddressStringType"

    value: str = field(default="")
    datatype: EntityObjectIpaddressStringTypeDatatype = field(
        default=EntityObjectIpaddressStringTypeDatatype.STRING,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EntityObjectIpaddressType(EntitySimpleBaseType):
    """The EntityObjectIPAddressType type is extended by the entities of an
    individual OVAL Object.

    This type provides uniformity to each object entity by including the
    attributes found in the EntitySimpleBaseType. This specific type
    describes any IPv4/IPv6 address or address prefix.
    """

    class Meta:
        name = "EntityObjectIPAddressType"

    value: str = field(default="")
    datatype: Optional[EntityObjectIpaddressTypeDatatype] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EntityObjectIntType(EntitySimpleBaseType):
    """The EntityIntType type is extended by the entities of an individual OVAL
    Object.

    This type provides uniformity to each object entity by including the
    attributes found in the EntitySimpleBaseType. This specific type
    describes simple integer data. The empty string is also allowed when
    using a variable reference with an element.
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
class EntityObjectRecordType(EntityComplexBaseType):
    """The EntityObjectRecordType defines an entity that consists of a number of
    uniquely named fields.

    This structure is used for representing a record from a database
    query and other similar structures where multiple related fields
    must be represented at once. Note that for all entities of this
    type, the only allowed datatype is 'record' and the only allowed
    operation is 'equals'. During analysis of a system characteristics
    item, each field is analyzed and then the overall result for
    elements of this type is computed by logically anding the results
    for each field and then applying the entity_check attribute. Note
    the datatype attribute must be set to 'record'. Note the operation
    attribute must be set to 'equals'. Note the var_ref attribute is not
    permitted and the var_check attribute does not apply. Note that when
    the mask attribute is set to 'true', all child field elements must
    be masked regardless of the child field's mask attribute value.
    """

    field_value: list[EntityObjectFieldType] = field(
        default_factory=list,
        metadata={
            "name": "field",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class EntityObjectStringType(EntitySimpleBaseType):
    """The EntityStringType type is extended by the entities of an individual OVAL
    Object.

    This type provides uniformity to each object entity by including the
    attributes found in the EntitySimpleBaseType. This specific type
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
class EntityObjectVersionType(EntitySimpleBaseType):
    """The EntityObjectVersionType type is extended by the entities of an
    individual OVAL State.

    This type provides uniformity to each state entity by including the
    attributes found in the EntityStateSimpleBaseType. This specific
    type describes simple version data.
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
class EntityStateComplexBaseType(EntityComplexBaseType):
    """The EntityStateComplexBaseType complex type is an abstract type that extends
    the EntityComplexBaseType and is used by some entities within an OVAL State.

    The optional check_existence attribute specifies how to interpret
    the status of corresponding item entities when performing an item-
    state comparison. The default value for this attribute is
    'at_least_one_exists' indicating that by default an item comparison
    may evaluate to true only if at least one corresponding item entity
    has a status of 'exists'. For example, if a value of 'none_exist' is
    given, then the comparison can evaluate to true only if there are
    one or more corresponding item entities, each with a status of 'does
    not exist'. The optional entity_check attribute specifies how to
    handle multiple item entities with the same name in the OVAL Systems
    Characteristics file. For example, suppose we are dealing with a
    Group Test and an entity in the state is related to the user.  It is
    very likely that when the information about the group is collected
    off of the system (and represented in the OVAL System
    Characteristics file) that there will be multiple users associated
    with the group (i.e. multiple 'user' item entities associated with
    the same 'user' state entity).  If the OVAL State defines the value
    of the user entity to equal 'Fred', then the entity_check attribute
    determines if all values for 'user' item entities must be equal to
    'Fred', or at least one value must be equal to 'Fred', etc.  Note
    that with the exception of the 'none_satisfy' check value, the
    entity_check attribute can only affect the result of the test if the
    corresponding OVAL Item allows more than one occurrence of the
    entity (e.g. 'maxOccurs' is some value greater than one). The
    entity_check and var_check attributes are considered together when
    evaluating a single state entity. When a variable identifies more
    than one value and multiple item entities with the same name exist,
    for a single state entity, a many-to-many comparison must be
    conducted.  In this situation, there are many values for the state
    entity that must be compared to many item entities.  Each item
    entity is compared to the state entity. For each item entity, an
    interim result is calculated by using the var_check attribute to
    combine the result of comparing each variable value with a single
    system value. Then these interim results are combined for each
    system value using the entity_check attribute.
    """

    entity_check: CheckEnumeration = field(
        default=CheckEnumeration.ALL,
        metadata={
            "type": "Attribute",
        },
    )
    check_existence: ExistenceEnumeration = field(
        default=ExistenceEnumeration.AT_LEAST_ONE_EXISTS,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EntityStateSimpleBaseType(EntitySimpleBaseType):
    """The EntityStateSimpleBaseType complex type is an abstract type that extends
    the EntitySimpleBaseType and is used by some entities within an OVAL State.

    The optional check_existence attribute specifies how to interpret
    the status of corresponding item entities when performing an item-
    state comparison. The default value for this attribute is
    'at_least_one_exists' indicating that by default an item comparison
    may evaluate to true only if at least one corresponding item entity
    has a status of 'exists'. For example, if a value of 'none_exist' is
    given, then the comparison can evaluate to true only if there are
    one or more corresponding item entities, each with a status of 'does
    not exist'. The optional entity_check attribute specifies how to
    handle multiple item entities with the same name in the OVAL Systems
    Characteristics file. For example, suppose we are dealing with a
    Group Test and an entity in the state is related to the user.  It is
    very likely that when the information about the group is collected
    off of the system (and represented in the OVAL System
    Characteristics file) that there will be multiple users associated
    with the group (i.e. multiple 'user' item entities associated with
    the same 'user' state entity).  If the OVAL State defines the value
    of the user entity to equal 'Fred', then the entity_check attribute
    determines if all values for 'user' item entities must be equal to
    'Fred', or at least one value must be equal to 'Fred', etc.  Note
    that with the exception of the 'none_satisfy' check value, the
    entity_check attribute can only affect the result of the test if the
    corresponding OVAL Item allows more than one occurrence of the
    entity (e.g. 'maxOccurs' is some value greater than one). The
    entity_check and var_check attributes are considered together when
    evaluating a single state entity. When a variable identifies more
    than one value and multiple item entities with the same name exist,
    for a single state entity, a many-to-many comparison must be
    conducted.  In this situation, there are many values for the state
    entity that must be compared to many item entities.  Each item
    entity is compared to the state entity. For each item entity, an
    interim result is calculated by using the var_check attribute to
    combine the result of comparing each variable value with a single
    system value. Then these interim results are combined for each
    system value using the entity_check attribute.
    """

    entity_check: CheckEnumeration = field(
        default=CheckEnumeration.ALL,
        metadata={
            "type": "Attribute",
        },
    )
    check_existence: ExistenceEnumeration = field(
        default=ExistenceEnumeration.AT_LEAST_ONE_EXISTS,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MetadataType:
    """The MetadataType complex type contains all the metadata available to an OVAL
    Definition.

    This metadata is for informational purposes only and is not part of
    the criteria used to evaluate machine state. The required title
    child element holds a short string that is used to quickly identify
    the definition to a human user. The affected metadata item contains
    information about the system(s) for which the definition has been
    written. Remember that this is just metadata and not part of the
    criteria. Please refer to the AffectedType description for more
    information. The required description element contains a textual
    description of the configuration state being addressed by the OVAL
    Definition. In the case of a definition from the vulnerability
    class, the reference is usually the Common Vulnerability and
    Exposures (CVE) Identifier, and this description field corresponds
    with the CVE description. Additional metadata is also allowed
    although it is not part of the official OVAL Schema. Individual
    organizations can place metadata items that they feel are important
    and these will be skipped during the validation. All OVAL really
    cares about is that the stated metadata items are there.
    """

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    affected: list[AffectedType] = field(
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
    description: Optional[str] = field(
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
class ObjectType:
    """The base type of every object includes an optional notes element.

    The notes element of an object should be used to hold information
    that might be helpful to someone examining the technical aspects of
    the object. For example, why certain values have been used, or maybe
    a link to where further information can be found. Please refer to
    the description of the NotesType complex type for more information
    about the notes element. The required id attribute uniquely
    identifies each object, and must conform to the format specified by
    the ObjectIdPattern simple type. The required version attribute
    holds the current version of the object element. Versions are
    integers, starting at 1 and incrementing every time an object is
    modified. The optional comment attribute provides a short
    description of the object. The optional deprecated attribute
    signifies that an id is no longer to be used or referenced but the
    information has been kept around for historic purposes.
    """

    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    notes: Optional[Notes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    oval_mitre_org_xmlschema_oval_common_5_notes: Optional[
        OvalCommonSchemaNotes
    ] = field(
        default=None,
        metadata={
            "name": "notes",
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-common-5",
        },
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "id",
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:obj:[1-9][0-9]*",
        },
    )
    version_attribute: Optional[int] = field(
        default=None,
        metadata={
            "name": "version",
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 1,
        },
    )
    deprecated: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class PossibleRestrictionType:
    """The PossibleRestrictionType complex type outlines a range of possible
    expected value of an external variable.

    Each possible_restriction element contains an unbounded list of
    child restriction elements that each specify a range that an actual
    value may fall in. For example, a restriction element may specify
    that a value must be less than 10. When multiple restriction
    elements are present, a valid possible value's evaluation is based
    on the operator attribute. The operator attribute is set to AND by
    default. Other valid operation values are explained in the
    description of the OperatorEnumeration simple type. One can think of
    the possible_value and possible_restriction elements as an OR'd list
    of possible values, with the restriction elements as using the
    selected operation to evaluate its own list of value descriptions.
    Please refer to the description of the RestrictionType complex type
    for more information. The required hint attribute gives a short
    description of what the value means or represents.
    """

    restriction: list[RestrictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    operator: OperatorEnumeration = field(
        default=OperatorEnumeration.AND,
        metadata={
            "type": "Attribute",
        },
    )
    hint: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class StateType:
    """The base type of every state includes an optional notes element and two
    attributes.

    The notes section of a state should be used to hold information that
    might be helpful to someone examining the technical aspects of the
    state. For example, why certain values have been used by the state,
    or maybe a link to where further information can be found. Please
    refer to the description of the NotesType complex type for more
    information about the notes element. The required id attribute
    uniquely identifies each state, and must conform to the format
    specified by the StateIdPattern simple type. The required version
    attribute holds the current version of the state. Versions are
    integers, starting at 1 and incrementing every time a state is
    modified. The required operator attribute provides the logical
    operator that binds the different characteristics inside a state
    together. The optional comment attribute provides a short
    description of the state. The optional deprecated attribute
    signifies that an id is no longer to be used or referenced but the
    information has been kept around for historic purposes. When
    evaluating a particular state against an object, one should evaluate
    each individual entity separately. The individual results are then
    combined by the operator to produce an overall result. This process
    holds true even when there are multiple instances of the same
    entity. Evaluate each instance separately, taking the entity check
    attribute into account, and then combine everything using the
    operator.
    """

    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    notes: Optional[Notes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    oval_mitre_org_xmlschema_oval_common_5_notes: Optional[
        OvalCommonSchemaNotes
    ] = field(
        default=None,
        metadata={
            "name": "notes",
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-common-5",
        },
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "id",
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:ste:[1-9][0-9]*",
        },
    )
    version_attribute: Optional[int] = field(
        default=None,
        metadata={
            "name": "version",
            "type": "Attribute",
            "required": True,
        },
    )
    operator: OperatorEnumeration = field(
        default=OperatorEnumeration.AND,
        metadata={
            "type": "Attribute",
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 1,
        },
    )
    deprecated: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TestType:
    """The base type of every test includes an optional notes element and several
    attributes.

    The notes section of a test should be used to hold information that
    might be helpful to someone examining the technical aspects of the
    test. For example, why certain values have been used by the test, or
    maybe a link to where further information can be found. Please refer
    to the description of the NotesType complex type for more
    information about the notes element. The required comment attribute
    provides a short description of the test. The optional deprecated
    attribute signifies that an id is no longer to be used or referenced
    but the information has been kept around for historic purposes. The
    required id attribute uniquely identifies each test, and must
    conform to the format specified by the TestIdPattern simple type.
    The required version attribute holds the current version of the
    test. Versions are integers, starting at 1 and incrementing every
    time a test is modified. The optional check_existence attribute
    specifies how many items in the set defined by the OVAL Object must
    exist for the test to evaluate to true. The default value for this
    attribute is 'at_least_one_exists' indicating that by default the
    test may evaluate to true if at least one item defined by the OVAL
    Object exists on the system. For example, if a value of 'all_exist'
    is given, every item defined by the OVAL Object must exist on the
    system for the test to evaluate to true. If the OVAL Object uses a
    variable reference, then every value of that variable must exist.
    Note that a pattern match defines a unique set of matching items
    found on a system. So when check_existence = 'all_exist' and a regex
    matches anything on a system the test will evaluate to true (since
    all matching objects on the system were found on the system). When
    check_existence = 'all_exist' and a regex does not match anything on
    a system the test will evaluate to false. The required check
    attribute specifies how many items in the set defined by the OVAL
    Object (ignoring items with a status of Does Not Exist) must satisfy
    the state requirements.  For example, should the test check that all
    matching files have a specified version or that at least one file
    has the specified version?  The valid check values are explained in
    the description of the CheckEnumeration simple type. Note that if
    the test does not contain any references to OVAL States, then the
    check attribute has no meaning and can be ignored during evaluation.
    An OVAL Test evaluates to true if both the check_existence  and
    check attributes are satisfied during evaluation. The evaluation
    result for a test is determined by first evaluating the
    check_existence attribute. If the result of evaluating the
    check_existence attribute is true then the check attribute is
    evaluated. An interpreter may choose to always evaluate both the
    check_existence and the check attributes, but once the
    check_existence attribute evaluation has resulted in false the
    overall test result after evaluating the check attribute will not be
    affected. The optional state_operator attribute provides the logical
    operator that combines the evaluation results from each referenced
    state on a per item basis.  Each matching item is compared to each
    referenced state. The result of comparing each state to a single
    item is combined based on the specified state_operator value to
    determine one result for each item. Finally, the results for each
    item are combined based on the specified check value.  Note that if
    the test does not contain any references to OVAL States, then the
    state_operator attribute has no meaning and can be ignored during
    evaluation. Referencing multiple states in one test allows ranges of
    possible values to be expressed. For example, one state can check
    that a value greater than 8 is found and another state can check
    that a value of less than 16 is found.  In this example the
    referenced states are combined with a state_operator = 'AND'
    indicating that the conditions of all referenced states must be
    satisfied and that the value must be between 8 AND 16.  The valid
    state_operation values are explained in the description of the
    OperatorEnumeration simple type.
    """

    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    notes: Optional[Notes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    oval_mitre_org_xmlschema_oval_common_5_notes: Optional[
        OvalCommonSchemaNotes
    ] = field(
        default=None,
        metadata={
            "name": "notes",
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-common-5",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:tst:[1-9][0-9]*",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    check_existence: ExistenceEnumeration = field(
        default=ExistenceEnumeration.AT_LEAST_ONE_EXISTS,
        metadata={
            "type": "Attribute",
        },
    )
    check: Optional[CheckEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    state_operator: OperatorEnumeration = field(
        default=OperatorEnumeration.AND,
        metadata={
            "type": "Attribute",
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 1,
        },
    )
    deprecated: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class VariableType:
    """The VariableType complex type defines attributes associated with each OVAL
    Variable.

    The required id attribute uniquely identifies each variable, and
    must conform to the format specified by the VariableIDPattern simple
    type. The required version attribute holds the current version of
    the variable. Versions are integers, starting at 1 and incrementing
    every time a variable is modified. The required comment attribute
    provides a short description of the variable. The optional
    deprecated attribute signifies that an id is no longer to be used or
    referenced but the information has been kept around for historic
    purposes. The required datatype attribute specifies the type of
    value being defined.  The set of values identified by a variable
    must comply with the specified datatype, otherwise an error should
    be reported. Please see the DatatypeEnumeration for details about
    each valid datatype.  For example, if the datatype of the variable
    is specified as boolean then the value(s) returned by the component
    / function should be "true", "false", "1", or "0". Note that the
    'record' datatype is not permitted on variables. The notes section
    of a variable should be used to hold information that might be
    helpful to someone examining the technical aspects of the variable.
    Please refer to the description of the NotesType complex type for
    more information about the notes element.

    :ivar signature:
    :ivar notes:
    :ivar oval_mitre_org_xmlschema_oval_common_5_notes:
    :ivar id:
    :ivar version:
    :ivar datatype: Note that the 'record' datatype is not permitted on
        variables.
    :ivar comment:
    :ivar deprecated:
    """

    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    notes: Optional[Notes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    oval_mitre_org_xmlschema_oval_common_5_notes: Optional[
        OvalCommonSchemaNotes
    ] = field(
        default=None,
        metadata={
            "name": "notes",
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-common-5",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:var:[1-9][0-9]*",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    datatype: Optional[SimpleDatatypeEnumeration] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 1,
        },
    )
    deprecated: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Set:
    """The set element enables complex objects to be described.

    It is a recursive element in that each set element can contain
    additional set elements as children. Each set element defines
    characteristics that produce a matching unique set of items. This
    set of items is defined by one or two references to OVAL Objects
    that provide the criteria needed to collect a set of system items.
    These items can have one or more filters applied to allow a subset
    of those items to be specifically included or excluded from the
    overall set of items. The set element's object_reference refers to
    an existing OVAL Object. The set element's filter element provides a
    reference to an existing OVAL State and includes an optional action
    attribute. The filter's action attribute allows the author to
    specify whether matching items should be included or excluded from
    the overall set. The default filter action is to exclude all
    matching items. In other words, the filter can be thought of
    filtering items out by default. Each filter is applied to the items
    identified by each OVAL Object before the set_operator is applied.
    For example, if an object_reference points to an OVAL Object that
    identifies every file in a certain directory, a filter might be set
    up to limit the object set to only those files with a size less than
    10 KB. If multiple filters are provided, then each filter is applied
    to the set of items identified by the OVAL Object. Care must be
    taken to ensure that conflicting filters are not applied. It is
    possible to exclude all items with a size of 10 KB and then include
    only items with a size of 10 KB. This example would result in the
    empty set. The optional set_operator attribute defines how different
    child sets are combined to form the overall unique set of objects.
    For example, does one take the union of different sets or the
    intersection? For a description of the valid values please refer to
    the SetOperatorEnumeration simple type.
    """

    class Meta:
        name = "set"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    set: list["Set"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
        },
    )
    object_reference: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:obj:[1-9][0-9]*",
        },
    )
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    set_operator: SetOperatorEnumeration = field(
        default=SetOperatorEnumeration.UNION,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class BeginFunctionType:
    """The begin function takes a single string component and defines a character
    (or string) that the component string should start with.

    The character attribute defines the specific character (or string).
    The character (or string) is only added to the component string if
    the component string does not already start with the specified
    character (or string). If the component string does not start with
    the specified character (or string) the entire character (or string)
    will be prepended to the component string..
    """

    object_component: Optional[ObjectComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    variable_component: Optional[VariableComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    literal_component: Optional[LiteralComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    arithmetic: Optional[ArithmeticFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    begin: Optional["BeginFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    concat: Optional["ConcatFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    end: Optional["EndFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    escape_regex: Optional["EscapeRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    split: Optional["SplitFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    substring: Optional["SubstringFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    time_difference: Optional["TimeDifferenceFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    regex_capture: Optional["RegexCaptureFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    unique: Optional["UniqueFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    count: Optional["CountFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    glob_to_regex: Optional["GlobToRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    merge: Optional["MergeFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    character: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class DefinitionType:
    """The DefinitionType defines a single OVAL Definition.

    A definition is the key structure in OVAL. It is analogous to the
    logical sentence or proposition: if a computer's state matches the
    configuration parameters laid out in the criteria, then that
    computer exhibits the state described. The DefinitionType contains a
    section for various metadata related elements that describe the
    definition. This includes a description, version, affected system
    types, and reference information. The notes section of a definition
    should be used to hold information that might be helpful to someone
    examining the technical aspects of the definition. For example, why
    certain tests have been included in the criteria, or maybe a link to
    where further information can be found. The DefinitionType also
    (unless the definition is deprecated) contains a criteria child
    element that joins individual tests together with a logical operator
    to specify the specific computer state being described. The required
    id attribute is the OVAL-ID of the Definition. The form of an OVAL-
    ID must follow the specific format described by the
    oval:DefinitionIDPattern. The required version attribute holds the
    current version of the definition. Versions are integers, starting
    at 1 and incrementing every time a definition is modified. The
    required class attribute indicates the specific class to which the
    definition belongs. The class gives a hint to a user so they can
    know what the definition writer is trying to say. See the definition
    of oval-def:ClassEnumeration for more information about the
    different valid classes. The optional deprecated attribute signifies
    that an id is no longer to be used or referenced but the information
    has been kept around for historic purposes. When the deprecated
    attribute is set to true, the definition is considered to be
    deprecated. The criteria child element of a deprecated definition is
    optional. If a deprecated definition does not contain a criteria
    child element, the definition must evaluate to "not evaluated". If a
    deprecated definition contains a criteria child element, an
    interpreter should evaluate the definition as if it were not
    deprecated, but an interpreter may evaluate the definition to "not
    evaluated".
    """

    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    metadata: Optional[MetadataType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    notes: Optional[Notes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    oval_mitre_org_xmlschema_oval_common_5_notes: Optional[
        OvalCommonSchemaNotes
    ] = field(
        default=None,
        metadata={
            "name": "notes",
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-common-5",
        },
    )
    criteria: Optional[CriteriaType] = field(
        default=None,
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
            "pattern": r"oval:[A-Za-z0-9_\-\.]+:def:[1-9][0-9]*",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    class_value: Optional[ClassEnumeration] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
            "required": True,
        },
    )
    deprecated: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EntityStateAnySimpleType(EntityStateSimpleBaseType):
    """The EntityStateAnySimpleType type is extended by the entities of an
    individual OVAL State.

    This type provides uniformity to each state entity by including the
    attributes found in the EntityStateSimpleBaseType. This specific
    type describes any simple data.
    """

    value: str = field(default="")
    datatype: SimpleDatatypeEnumeration = field(
        default=SimpleDatatypeEnumeration.STRING,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EntityStateBinaryType(EntityStateSimpleBaseType):
    """The EntityStateBinaryType type is extended by the entities of an individual
    OVAL State.

    This type provides uniformity to each state entity by including the
    attributes found in the EntityStateSimpleBaseType. This specific
    type describes simple binary data. The empty string is also allowed
    when using a variable reference with an element.
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
class EntityStateBoolType(EntityStateSimpleBaseType):
    """The EntityStateBoolType type is extended by the entities of an individual
    OVAL State.

    This type provides uniformity to each state entity by including the
    attributes found in the EntityStateSimpleBaseType. This specific
    type describes simple boolean data. The empty string is also allowed
    when using a variable reference with an element.
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
class EntityStateDebianEvrstringType(EntityStateSimpleBaseType):
    """The EntityStateDebianEVRStringType type is extended by the entities of an
    individual OVAL State.

    This type provides uniformity to each state entity by including the attributes found in the EntityStateSimpleBaseType. This type represents the epoch, upstream_version, and debian_revision fields, for a Debian package, as a single version string. It has the form "EPOCH:UPSTREAM_VERSION-DEBIAN_REVISION". Note that a null epoch (or '(none)' as returned by dpkg) is equivalent to '0' and would hence have the form 0:UPSTREAM_VERSION-DEBIAN_REVISION. Comparisons involving this datatype should follow the algorithm outlined in Chapter 5 of the "Debian Policy Manual" (https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-Version). An implementation of this is the cmpversions() function in dpkg's enquiry.c.
    """

    class Meta:
        name = "EntityStateDebianEVRStringType"

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
class EntityStateEvrstringType(EntityStateSimpleBaseType):
    """The EntityStateEVRStringType type is extended by the entities of an
    individual OVAL State.

    This type provides uniformity to each state entity by including the
    attributes found in the EntityStateSimpleBaseType. This type
    represents the epoch, version, and release fields, for an RPM
    package, as a single version string. It has the form "EPOCH:VERSION-
    RELEASE". Note that a null epoch (or '(none)' as returned by rpm) is
    equivalent to '0' and would hence have the form 0:VERSION-RELEASE.
    Comparisons involving this datatype should follow the algorithm of
    librpm's rpmvercmp() function.
    """

    class Meta:
        name = "EntityStateEVRStringType"

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
class EntityStateFileSetRevisionType(EntityStateSimpleBaseType):
    """The EntityStateFileSetRevisionType type is extended by the entities of an
    individual OVAL State.

    This type provides uniformity to each state entity by including the
    attributes found in the EntityStateSimpleBaseType. This specific
    type represents the version string related to filesets in HP-UX.
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
class EntityStateFloatType(EntityStateSimpleBaseType):
    """The EntityStateFloatType type is extended by the entities of an individual
    OVAL State.

    This type provides uniformity to each state entity by including the
    attributes found in the EntityStateSimpleBaseType. This specific
    type describes simple float data. The empty string is also allowed
    when using a variable reference with an element.
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
class EntityStateIosversionType(EntityStateSimpleBaseType):
    """The EntityStateIOSVersionType type is extended by the entities of an
    individual OVAL State.

    This type provides uniformity to each state entity by including the
    attributes found in the EntityStateSimpleBaseType. This specific
    type represents the version string related to CISCO IOS.
    """

    class Meta:
        name = "EntityStateIOSVersionType"

    value: str = field(default="")
    datatype: EntityStateIosversionTypeDatatype = field(
        default=EntityStateIosversionTypeDatatype.STRING,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EntityStateIpaddressStringType(EntityStateSimpleBaseType):
    """The EntityStateIPAddressStringType type is extended by the entities of an
    individual OVAL State.

    This type provides uniformity to each object entity by including the
    attributes found in the EntityStateSimpleBaseType. This specific
    type describes any IPv4/IPv6 address, address prefix, or its string
    representation.
    """

    class Meta:
        name = "EntityStateIPAddressStringType"

    value: str = field(default="")
    datatype: EntityStateIpaddressStringTypeDatatype = field(
        default=EntityStateIpaddressStringTypeDatatype.STRING,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EntityStateIpaddressType(EntityStateSimpleBaseType):
    """The EntityStateIPAddressType type is extended by the entities of an
    individual OVAL State.

    This type provides uniformity to each object entity by including the
    attributes found in the EntityStateSimpleBaseType. This specific
    type describes any IPv4/IPv6 address or address prefix.
    """

    class Meta:
        name = "EntityStateIPAddressType"

    value: str = field(default="")
    datatype: Optional[EntityStateIpaddressTypeDatatype] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EntityStateIntType(EntityStateSimpleBaseType):
    """The EntityStateIntType type is extended by the entities of an individual
    OVAL State.

    This type provides uniformity to each state entity by including the
    attributes found in the EntityStateSimpleBaseType. This specific
    type describes simple integer data. The empty string is also allowed
    when using a variable reference with an element.
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
            "namespace": "",
        },
    )


@dataclass
class EntityStateStringType(EntityStateSimpleBaseType):
    """The EntityStateStringType type is extended by the entities of an individual
    OVAL State.

    This type provides uniformity to each state entity by including the
    attributes found in the EntityStateSimpleBaseType. This specific
    type describes simple string data.
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
class EntityStateVersionType(EntityStateSimpleBaseType):
    """The EntityStateVersionType type is extended by the entities of an individual
    OVAL State.

    This type provides uniformity to each state entity by including the
    attributes found in the EntityStateSimpleBaseType. This specific
    type describes simple version data.
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
class ConstantVariable(VariableType):
    """The constant_variable element extends the VariableType and defines a
    variable with a constant value(s).

    Each constant_variable defines either a single value or a collection
    of values to be used throughout the evaluation of the OVAL
    Definition File in which it has been defined. Constant variables
    cannot be over-ridden by an external source. The actual value of a
    constant variable is defined by the required value child element. A
    collection of values can be specified by including multiple
    instances of the value element. Please refer to the description of
    the ValueType complex type for more information.
    """

    class Meta:
        name = "constant_variable"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    value: list[ValueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )


@dataclass
class ExternalVariable(VariableType):
    """The external_variable element extends the VariableType and defines a
    variable with some external source.

    The actual value(s) for the variable is not provided within the OVAL
    file, but rather it is retrieved during the evaluation of the OVAL
    Definition from an external source. An unbounded set of possible-
    value and possible_restriction child elements can be specified that
    together specify the list of all possible values that an external
    source is allowed to supply for the external variable. In other
    words, the value assigned by an external source must match one of
    the possible_value or possible_restriction elements specified. Each
    possible_value element contains a single value that could be
    assigned to the given external_variable while each
    possible_restriction element outlines a range of possible values.
    Note that it is not necessary to declare a variable's possible
    values, but the option is available if desired. If no possible child
    elements are specified, then the valid values are only bound to the
    specified datatype of the external variable. Please refer to the
    description of the PossibleValueType and PossibleRestrictionType
    complex types for more information.
    """

    class Meta:
        name = "external_variable"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    possible_value: list[PossibleValueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    possible_restriction: list[PossibleRestrictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Object(ObjectType):
    """The object element is an abstract element that is meant to be extended (via
    substitution groups) by the objects found in the component schemas.

    An actual object element is not valid. The use of this abstract
    element simplifies the OVAL schema by allowing individual objects to
    inherit any common elements and attributes from the base ObjectType.
    Please refer to the description of the ObjectType complex type for
    more information. An object is used to identify a set of items to
    collect.  The author of a schema object must define sufficient
    object entities to allow a user to identify a unique item to be
    collected. A simple object typically results in a single file,
    process, etc being identified.  But through the use of pattern
    matches, sets, and variables, multiple matching items can be
    identified.  The set of items matching the object can then be used
    by an OVAL test and compared against an OVAL state.
    """

    class Meta:
        name = "object"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class State(StateType):
    """The state element is an abstract element that is meant to be extended (via
    substitution groups) by the states found in the component schemas.

    An actual state element is not valid. The use of this abstract class
    simplifies the OVAL schema by allowing individual states to inherit
    the optional notes child element, and the id and operator attributes
    from the base StateType. Please refer to the description of the
    StateType complex type for more information. An OVAL State is a
    collection of one or more characteristics pertaining to a specific
    object type. The OVAL State is used by an OVAL Test to determine if
    a unique set of items identified on a system meet certain
    characteristics.
    """

    class Meta:
        name = "state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class Test(TestType):
    """The test element is an abstract element that is meant to be extended (via
    substitution groups) by the individual tests found in the component schemas.

    An OVAL Test is used to compare an object(s) against a defined
    state. An actual test element is not valid. The use of this abstract
    class simplifies the OVAL schema by allowing individual tests to
    inherit the optional notes child element, and the id and comment
    attributes from the base TestType. Please refer to the description
    of the TestType complex type for more information.
    """

    class Meta:
        name = "test"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class Variable(VariableType):
    """The variable element is an abstract element that is meant to be extended
    (via substitution groups) by the different types of variables.

    An actual variable element is not valid. The different variable
    types describe different sources for obtaining a value(s) for the
    variable. There are currently three types of variables; local,
    external, and constant. Please refer to the description of each one
    for more specific information. The value(s) of a variable is treated
    as if it were inserted where referenced. One of the main benefits of
    variables is that they allow tests to evaluate user-defined policy.
    For example, an OVAL Test might check to see if a password is at
    least a certain number of characters long, but this number depends
    upon the individual policy of the user. To solve this, the test for
    password length can be written to refer to a variable element that
    defines the length. If a variable defines a collection of values,
    any entity that references the variable will evaluate to true
    depending on the value of the var_check attribute. For example, if
    an entity 'size' with an operation of 'less than' references a
    variable that returns five different integers, and the var_check
    attribute has a value of 'all', then the 'size' entity returns true
    only if the actual size is less than each of the five integers
    defined by the variable. If a variable does not return any value,
    then an error should be reported during OVAL analysis.
    """

    class Meta:
        name = "variable"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class ConcatFunctionType:
    """The concat function takes two or more components and concatenates them
    together to form a single string.

    The first component makes up the beginning of the resulting string
    and any following components are added to the end it. If one of the
    components returns multiple values then the concat function would be
    performed multiple times and the end result would be a collection of
    values for the local variable. For example assume a local variable
    has two sub-components: a basic component element returns the values
    "abc" and "def", and a literal component element that has a value of
    "xyz". The local_variable element would evaluate to a collection of
    two values, "abcxyz" and "defxyz". If one of the components does not
    exist, then the result of the concat operation should be does not
    exist.
    """

    object_component: list[ObjectComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    variable_component: list[VariableComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    literal_component: list[LiteralComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    arithmetic: list[ArithmeticFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    begin: list[BeginFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    concat: list["ConcatFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    end: list["EndFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    escape_regex: list["EscapeRegexFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    split: list["SplitFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    substring: list["SubstringFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    time_difference: list["TimeDifferenceFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    regex_capture: list["RegexCaptureFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    unique: list["UniqueFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    count: list["CountFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    glob_to_regex: list["GlobToRegexFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    merge: list["MergeFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )


@dataclass
class Definition(DefinitionType):
    """The definition element represents the globally defined element of type
    DefinitionType.

    For more information please see the documentation on the
    DefinitionType.
    """

    class Meta:
        name = "definition"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


@dataclass
class DefinitionsType:
    """The DefinitionsType complex type is a container for one or more definition
    elements.

    Each definition element describes a single OVAL Definition. Please
    refer to the description of the DefinitionType for more information
    about an individual definition.
    """

    definition: list[Definition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
            "min_occurs": 1,
        },
    )


@dataclass
class EndFunctionType:
    """The end function takes a single string component and defines a character (or
    string) that the component string should end with.

    The character attribute defines the specific character (or string).
    The character (or string) is only added to the component string if
    the component string does not already end with the specified
    character (or string). If the desired end character is a string,
    then the entire end string must exist at the end if the component
    string. If the entire end string is not present then the entire end
    string is appended to the component string.
    """

    object_component: Optional[ObjectComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    variable_component: Optional[VariableComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    literal_component: Optional[LiteralComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    arithmetic: Optional[ArithmeticFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    begin: Optional[BeginFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    concat: Optional[ConcatFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    end: Optional["EndFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    escape_regex: Optional["EscapeRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    split: Optional["SplitFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    substring: Optional["SubstringFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    time_difference: Optional["TimeDifferenceFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    regex_capture: Optional["RegexCaptureFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    unique: Optional["UniqueFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    count: Optional["CountFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    glob_to_regex: Optional["GlobToRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    merge: Optional["MergeFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    character: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class EscapeRegexFunctionType:
    """The escape_regex function takes a single string component and escapes all of
    the regular expression characters.

    If the string sub-component contains multiple values, then the
    escape_regex function will be applied to each individual value and
    return a multiple-valued result. For example, the string
    '(\\.test_string*)?' will evaluate to
    '\\(\\\\\\.test_string\\*\\)\\?'. The purpose for this is that many
    times, a component used in pattern match needs to be treated as a
    literal string and not a regular expression. For example, assume a
    basic component element that identifies a file path that is held in
    the Windows registry. This path is a string that might contain
    regular expression characters. These characters are likely not
    intended to be treated as regular expression characters and need to
    be escaped. This function allows a definition writer to mark convert
    the values of components to regular expression format. Note that
    when using regular expressions, OVAL supports a common subset of the
    regular expression character classes, operations, expressions and
    other lexical tokens defined within Perl 5's regular expression
    specification. The set of Perl metacharacters which must be escaped
    by this function is as follows, enclosed by single quotes:
    '^$\\.[](){}*+?|'. For more information on the supported regular
    expression syntax in OVAL see:
    http://oval.mitre.org/language/about/re_support_5.6.html.
    """

    object_component: Optional[ObjectComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    variable_component: Optional[VariableComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    literal_component: Optional[LiteralComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    arithmetic: Optional[ArithmeticFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    begin: Optional[BeginFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    concat: Optional[ConcatFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    end: Optional[EndFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    escape_regex: Optional["EscapeRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    split: Optional["SplitFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    substring: Optional["SubstringFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    time_difference: Optional["TimeDifferenceFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    regex_capture: Optional["RegexCaptureFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    unique: Optional["UniqueFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    count: Optional["CountFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    glob_to_regex: Optional["GlobToRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    merge: Optional["MergeFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class SplitFunctionType:
    """The split function takes a single string component and turns it into a
    collection of values based on a delimiter string.

    For example, assume that a basic component element returns the value
    "a-b-c-d" to the split function with the delimiter set to "-". The
    local_variable element would be evaluated to have four values "a",
    "b", "c", and "d". If the basic component returns a value that
    begins, or ends, with a delimiter, the local_variable element would
    contain empty string values at the beginning, or end, of the
    collection of values returned for that string component. For
    example, if the delimiter is "-", and the basic component element
    returns the value "-a-a-", the local_variable element would evaluate
    to a collection of four values "", "a", "a", and "". Likewise, if
    the basic component element returns a value that contains adjacent
    delimiters such as "---", the local_variable element would evaluate
    to a collection of four values "", "", "", and "". Lastly, if the
    basic component element used by the split function returnsa
    collection of values, then the split function is performed multiple
    times, and all of the results, from each of the split functions, are
    returned.
    """

    object_component: Optional[ObjectComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    variable_component: Optional[VariableComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    literal_component: Optional[LiteralComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    arithmetic: Optional[ArithmeticFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    begin: Optional[BeginFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    concat: Optional[ConcatFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    end: Optional[EndFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    escape_regex: Optional[EscapeRegexFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    split: Optional["SplitFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    substring: Optional["SubstringFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    time_difference: Optional["TimeDifferenceFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    regex_capture: Optional["RegexCaptureFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    unique: Optional["UniqueFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    count: Optional["CountFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    glob_to_regex: Optional["GlobToRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    merge: Optional["MergeFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    delimiter: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class SubstringFunctionType:
    """The substring function takes a single string component and produces a single
    value that contains a portion of the original string.

    The substring_start attribute defines the starting position in the
    original string. To include the first character of the string, the
    start position would be 1. A value less than 1 also means that the
    start position would be 1. If the substring_start attribute has
    value greater than the length of the original string an error should
    be reported. The substring_length attribute defines how many
    characters after, and including, the starting character to include.
    A substring_length value greater than the actual length of the
    string, or a negative value, means to include all of the characters
    after the starting character. For example, assume a basic component
    element that returns the value "abcdefg" with a substring_start
    value of 3 and a substring_length value of 2. The local_variable
    element would evaluate to have a single value of "cd". If the string
    component used by the substring function returns a collection of
    values, then the substring operation is performed multiple times and
    results in a collection of values for the component.
    """

    object_component: Optional[ObjectComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    variable_component: Optional[VariableComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    literal_component: Optional[LiteralComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    arithmetic: Optional[ArithmeticFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    begin: Optional[BeginFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    concat: Optional[ConcatFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    end: Optional[EndFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    escape_regex: Optional[EscapeRegexFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    split: Optional[SplitFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    substring: Optional["SubstringFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    time_difference: Optional["TimeDifferenceFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    regex_capture: Optional["RegexCaptureFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    unique: Optional["UniqueFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    count: Optional["CountFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    glob_to_regex: Optional["GlobToRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    merge: Optional["MergeFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    substring_start: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    substring_length: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class TimeDifferenceFunctionType:
    """The time_difference function calculates the difference in seconds between
    date-time values.

    If one component is specified, the values of that component are subtracted from the current time (UTC). The current time is the time at which the function is evaluated. If two components are specified, the value of the second component is subtracted from the value of the first component. If the component(s) contain a collection of values, the operation is performed multiple times on the Cartesian product of the component(s) and the result is also a collection of time difference values. For example, assume a local_variable specifies the time_difference function and has two sub-components under this function: the first component returns "04/02/2009" and "04/03/2009", and the second component returns "02/02/2005" and "02/03/2005" and "02/04/2005". The local_variable element would evaluate to a collection of six values: (ToSeconds("04/02/2009") - ToSeconds("02/02/2005")), (ToSeconds("04/02/2009") - ToSeconds("02/03/2005")),
    (ToSeconds("04/02/2009") - ToSeconds("02/04/2005")), (ToSeconds("04/03/2009") - ToSeconds("02/02/2005")), (ToSeconds("04/03/2009") - ToSeconds("02/03/2005")), and (ToSeconds("04/03/2009") - ToSeconds("02/04/2005")).
    The date-time format of each component is determined by the two format attributes. The format1 attribute applies to the first component, and the format2 attribute applies to the second component. Valid values for the attributes are 'win_filetime', 'seconds_since_epoch', 'day_month_year', 'year_month_day', and 'month_day_year'. Please see the DateTimeFormatEnumeration for more information about each of these values. If an input value is not understood, the result is an error. If only one input is specified, specify the format with the format2 attribute, as the first input is considered to be the implied 'current time' input.
    Note that the datatype associated with the components should be 'string' or 'int' depending on which date time format is specified.  The result of this function though is always an integer.
    """

    object_component: list[ObjectComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    variable_component: list[VariableComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    literal_component: list[LiteralComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    arithmetic: list[ArithmeticFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    begin: list[BeginFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    concat: list[ConcatFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    end: list[EndFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    escape_regex: list[EscapeRegexFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    split: list[SplitFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    substring: list[SubstringFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    time_difference: list["TimeDifferenceFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    regex_capture: list["RegexCaptureFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    unique: list["UniqueFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    count: list["CountFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    glob_to_regex: list["GlobToRegexFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    merge: list["MergeFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    format_1: DateTimeFormatEnumeration = field(
        default=DateTimeFormatEnumeration.YEAR_MONTH_DAY,
        metadata={
            "type": "Attribute",
        },
    )
    format_2: DateTimeFormatEnumeration = field(
        default=DateTimeFormatEnumeration.YEAR_MONTH_DAY,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RegexCaptureFunctionType:
    """The regex_capture function captures a single substring from a single string
    component.

    If the string sub-component contains multiple values, then the
    regex_capture function will extract a substring from each value. The
    'pattern' attribute provides a regular expression that should
    contain a single subexpression (using parentheses). For example, the
    pattern ^abc(.*)xyz$ would capture a substring from each of the
    string component's values if the value starts with abc and ends with
    xyz. In this case the subexpression would be all the characters that
    exist in between the abc and the xyz. Note that subexpressions match
    the longest possible substrings. If the regular expression contains
    multiple capturing sub-patterns, only the first capture is used. If
    there are no capturing sub-patterns, the result for each target
    string must be the empty string. Otherwise, if the regular
    expression could match the target string in more than one place,
    only the first match (and its first capture) is used. If no matches
    are found in a target string, the result for that target must be the
    empty string. Note that a quantified capturing sub-pattern does not
    produce multiple substrings. Standard regular expression semantics
    are such that if a capturing sub-pattern is required to match
    multiple times in order for the overall regular expression to match,
    the capture produced is the last substring to have matched the sub-
    pattern. Note that when using regular expressions, OVAL supports a
    common subset of the regular expression character classes,
    operations, expressions and other lexical tokens defined within Perl
    5's regular expression specification. If any of the Perl
    metacharacters are to be used literally, then they must be escaped.
    The set of metacharacters which must be escaped for this purpose is
    as follows, enclosed by single quotes: '^$\\.[](){}*+?|'. For more
    information on the supported regular expression syntax in OVAL see:
    http://oval.mitre.org/language/about/re_support_5.6.html.
    """

    object_component: Optional[ObjectComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    variable_component: Optional[VariableComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    literal_component: Optional[LiteralComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    arithmetic: Optional[ArithmeticFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    begin: Optional[BeginFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    concat: Optional[ConcatFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    end: Optional[EndFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    escape_regex: Optional[EscapeRegexFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    split: Optional[SplitFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    substring: Optional[SubstringFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    time_difference: Optional[TimeDifferenceFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    regex_capture: Optional["RegexCaptureFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    unique: Optional["UniqueFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    count: Optional["CountFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    glob_to_regex: Optional["GlobToRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    merge: Optional["MergeFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    pattern: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class UniqueFunctionType:
    """The unique function takes one or more components and removes any duplicate
    value from the set of components.

    All components used in the unique function will be treated as
    strings. For example, assume that three components exist, one that
    contains a string value of 'foo', and two of which both resolve to
    the string value 'bar'. Applying the unique function to these three
    components resolves to a local_variable with two string values,
    'foo' and 'bar'. Additionally, if any of the components referenced
    by the unique function evaluate to a collection of values, then
    those values are used in the unique calculation. For example, assume
    that there are two components, one of which resolves to a single
    string value, 'foo', the other of which resolves to two string
    values, 'foo' and 'bar'. If the unique function is used to remove
    duplicates from these two components, the function will resolve to a
    local_variable that is a collection of two string values, 'foo' and
    'bar'.
    """

    object_component: list[ObjectComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    variable_component: list[VariableComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    literal_component: list[LiteralComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    arithmetic: list[ArithmeticFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    begin: list[BeginFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    concat: list[ConcatFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    end: list[EndFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    escape_regex: list[EscapeRegexFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    split: list[SplitFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    substring: list[SubstringFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    time_difference: list[TimeDifferenceFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    regex_capture: list[RegexCaptureFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    unique: list["UniqueFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    count: list["CountFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    glob_to_regex: list["GlobToRegexFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    merge: list["MergeFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )


@dataclass
class MergeFunctionType:
    """The merge function takes one or more components and merges them together
    into a single string value, optionally including a delimiter string.

    For example, if data from one registry reg_multi_sz value contains
    values of "abc" and "def", the merge function operated on those
    values would resolve to a string with the value of 'abcdef'. If an
    optional delimiter of ',' was used, the merge function would resolve
    to a value of 'abc,'def'.
    """

    object_component: list[ObjectComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    variable_component: list[VariableComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    literal_component: list[LiteralComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    arithmetic: list[ArithmeticFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    begin: list[BeginFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    concat: list[ConcatFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    end: list[EndFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    escape_regex: list[EscapeRegexFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    split: list[SplitFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    substring: list[SubstringFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    time_difference: list[TimeDifferenceFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    regex_capture: list[RegexCaptureFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    unique: list[UniqueFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    count: list["CountFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    glob_to_regex: list["GlobToRegexFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    merge: list["MergeFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    delimiter: str = field(
        default="",
        metadata={
            "type": "Attribute",
        },
    )
    sort: SortEnumeration = field(
        default=SortEnumeration.DOCUMENT,
        metadata={
            "type": "Attribute",
        },
    )
    order: OrderEnumeration = field(
        default=OrderEnumeration.ASCENDING,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CountFunctionType:
    """The count function takes one or more components and returns the count of all
    of the values represented by the components.

    For example, assume that two variables exist, each with a single
    value. By applying the count function against two variable
    components that resolve to the two variables, the resulting
    local_variable would have a value of '2'. Additionally, if any of
    the components referenced by the count function evaluate to a
    collection of values, then those values are used in the count
    calculation. For example, assume that there are two components, one
    of which resolves to a single value, the other of which resolves to
    two values. If the count function is used to provide a count of
    these two components, the function will resolve to a local_variable
    with the values '3'.
    """

    object_component: list[ObjectComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    variable_component: list[VariableComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    literal_component: list[LiteralComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    arithmetic: list[ArithmeticFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    begin: list[BeginFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    concat: list[ConcatFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    end: list[EndFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    escape_regex: list[EscapeRegexFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    split: list[SplitFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    substring: list[SubstringFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    time_difference: list[TimeDifferenceFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    regex_capture: list[RegexCaptureFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    unique: list[UniqueFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    count: list["CountFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    glob_to_regex: list["GlobToRegexFunctionType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )
    merge: list[MergeFunctionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "sequence": 1,
        },
    )


@dataclass
class GlobToRegexFunctionType:
    """The glob_to_regex function takes a single string component representing
    shell glob pattern and produces a single value that corresponds to result of a
    conversion of the original glob pattern into Perl 5's regular expression
    pattern. The glob_noescape attribute defines the way how the backslash ('\\')
    character should be interpreted. It defaults to 'false' meaning backslash
    should be interpreted as an escape character (backslash is allowed to be used
    as an escape character). If the glob_noescape attribute would be set to 'true'
    it instructs the glob_to_regex function to interpret the backslash ('\\')
    character as a literal, rather than as an escape character (backslash is *not*
    allowed to be used as an escape character). Refer to table with examples below
    to see the difference how a different boolean value of the 'glob_noescape'
    attribute will impact the output form of the resulting Perl 5's regular
    expression produced by glob_to_regex function. Please note the glob_to_regex
    function will fail to perform the conversion and return an error when the
    provided string argument (to represent glob pattern) does not represent a
    syntactically correct glob pattern. For example given the 'a*b?[' as the
    argument to be converted, glob_to_regex would return an error since there's
    missing the corresponding closing bracket in the provided glob pattern
    argument.

    Also, it is necessary to mention that the glob_to_regex function respects the default behaviour for the input glob pattern and output Perl 5's regular expression spaces. Namely this means that:
    - glob_to_regex will respect the UNIX glob behavior when processing forward slashes, forward slash should be treated as a path separator and * or ? shall not match it,
    - glob_to_regex will rule out matches having special meaning (for example '.' as a representation of the current working directory or '..' as a representation of the parent directory of the current working directory,
    - glob_to_regex will rule out files or folders starting with '.' character (e.g. dotfiles) unless the respective glob pattern part itself starts with the '.' character,
    - glob_to_regex will not perform case-sensitivity transformation (alphabetical characters will be copied from input glob pattern space to output Perl 5's regular expression pattern space intact). It is kept as a responsibility of the OVAL content author to provide input glob pattern argument in such case so the resulting Perl 5's regular expression pattern will match the expected pathname entries according to the case of preference,
    - glob_to_regex will not perform any possible brace expansion. Therefore glob patterns like '{pat,pat,pat}' would be converted into Perl 5's regular expression syntax in the original un-expanded form (kept for any potential subsequent expansion to be performed by Perl 5's regular expression engine in the moment of the use of that resulting regular expression),
    - glob_to_regex will not perform tilde ('~') character substitution to user name home directory pathname. The ('~') character will be passed to Perl 5's regular expression engine intact. If user name home directory pathname glob pattern behaviour is expected, the pathname of the user name home directory needs to be specified in the original input glob pattern already,
    - glob_to_regex function will not perform any custom changes wrt to the ordering of items (perform any additional sorting of set of pathnames represented by the provided glob pattern argument).
    """

    object_component: Optional[ObjectComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    variable_component: Optional[VariableComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    literal_component: Optional[LiteralComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    arithmetic: Optional[ArithmeticFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    begin: Optional[BeginFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    concat: Optional[ConcatFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    end: Optional[EndFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    escape_regex: Optional[EscapeRegexFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    split: Optional[SplitFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    substring: Optional[SubstringFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    time_difference: Optional[TimeDifferenceFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    regex_capture: Optional[RegexCaptureFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    unique: Optional[UniqueFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    count: Optional[CountFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    glob_to_regex: Optional["GlobToRegexFunctionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    merge: Optional[MergeFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    glob_noescape: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LocalVariable(VariableType):
    """The local_variable element extends the VariableType and defines a variable
    with some local source.

    The actual value(s) for the variable is not provided in the OVAL
    Definition document but rather it is retrieved during the evaluation
    of the OVAL Definition. Each local variable is defined by either a
    single component or a complex function, meaning that a value can be
    as simple as a literal string or as complex as multiple registry
    keys concatenated together. Note that if an individual component is
    used and it returns a collection of values, then there will be
    multiple values associated with the local_variable. For example, if
    an object_component is used and it references a file object that
    identifies a set of 5 files, then the local variable would evaluate
    to a collection of those 5 values. Please refer to the description
    of the ComponentGroup for more information.
    """

    class Meta:
        name = "local_variable"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    object_component: Optional[ObjectComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    variable_component: Optional[VariableComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    literal_component: Optional[LiteralComponentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    arithmetic: Optional[ArithmeticFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    begin: Optional[BeginFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    concat: Optional[ConcatFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    end: Optional[EndFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    escape_regex: Optional[EscapeRegexFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    split: Optional[SplitFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    substring: Optional[SubstringFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    time_difference: Optional[TimeDifferenceFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    regex_capture: Optional[RegexCaptureFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    unique: Optional[UniqueFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    count: Optional[CountFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    glob_to_regex: Optional[GlobToRegexFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    merge: Optional[MergeFunctionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class VariablesType:
    """The VariablesType complex type is a container for one or more variable child
    elements.

    Each variable element is a way to define one or more values to be
    obtained at the time a definition is evaluated.
    """

    local_variable: list[LocalVariable] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    constant_variable: list[ConstantVariable] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )
    external_variable: list[ExternalVariable] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://oval.mitre.org/XMLSchema/oval-definitions-5",
        },
    )


@dataclass
class OvalDefinitions:
    """The oval_definitions element is the root of an OVAL Definition Document.

    Its purpose is to bind together the major sections of a document - generator, definitions, tests, objects, states, and variables - which are the children of the root element.

    :ivar generator: The required generator section provides information
        about when the definition file was compiled and under what
        version.
    :ivar definitions: The optional definitions section contains 1 or
        more definitions.
    :ivar tests: The optional tests section contains 1 or more tests.
    :ivar objects: The optional objects section contains 1 or more
        objects.
    :ivar states: The optional states section contains 1 or more states.
    :ivar variables: The optional variables section contains 1 or more
        variables.
    :ivar signature: The optional Signature element allows an XML
        Signature as defined by the W3C to be attached to the document.
        This allows authentication and data integrity to be provided to
        the user. Enveloped signatures are supported. More information
        about the official W3C Recommendation regarding XML digital
        signatures can be found at http://www.w3.org/TR/xmldsig-core/.
    """

    class Meta:
        name = "oval_definitions"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5"

    generator: Optional[GeneratorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    definitions: Optional[DefinitionType] = field(
        default=None,
        metadata={
            "type": "Elements",
            "namespace": "",
        },
    )
    tests: Optional[TestType] = field(
        default=None,
        metadata={
            "type": "Elements",
            "namespace": "",
        },
    )
    objects: Optional[ObjectType] = field(
        default=None,
        metadata={
            "type": "Elements",
            "namespace": "",
        },
    )
    states: Optional[StateType] = field(
        default=None,
        metadata={
            "type": "Elements",
            "namespace": "",
        },
    )
    variables: Optional[VariableType] = field(
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
