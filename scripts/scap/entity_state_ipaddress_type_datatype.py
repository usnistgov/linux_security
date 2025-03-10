from enum import Enum

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5"


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
