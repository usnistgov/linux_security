from enum import Enum

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"
)


class EntityItemProtocolType(Enum):
    """The EntityStateProtocolType complex type restricts a string value to the set
    of physical layer protocols used by AF_PACKET sockets.

    The empty string is also allowed to support the empty element
    associated with variable references.  Note that when using pattern
    matches and variables care must be taken to ensure that the regular
    expression and variable values align with the enumerated values.

    :cvar ETH_P_LOOP: Ethernet loopback packet.
    :cvar ETH_P_PUP: Xerox PUP packet.
    :cvar ETH_P_PUPAT: Xerox PUP Address Transport packet.
    :cvar ETH_P_IP: Internet protocol packet.
    :cvar ETH_P_X25: CCITT X.25 packet.
    :cvar ETH_P_ARP: Address resolution packet.
    :cvar ETH_P_BPQ: G8BPQ AX.25 ethernet packet.
    :cvar ETH_P_IEEEPUP: Xerox IEEE802.3 PUP packet.
    :cvar ETH_P_IEEEPUPAT: Xerox IEEE802.3 PUP address transport packet.
    :cvar ETH_P_DEC: DEC assigned protocol.
    :cvar ETH_P_DNA_DL: DEC DNA Dump/Load.
    :cvar ETH_P_DNA_RC: DEC DNA Remote Console.
    :cvar ETH_P_DNA_RT: DEC DNA Routing.
    :cvar ETH_P_LAT: DEC LAT.
    :cvar ETH_P_DIAG: DEC Diagnostics.
    :cvar ETH_P_CUST: DEC Customer use.
    :cvar ETH_P_SCA: DEC Systems Comms Arch.
    :cvar ETH_P_RARP: Reverse address resolution packet.
    :cvar ETH_P_ATALK: Appletalk DDP.
    :cvar ETH_P_AARP: Appletalk AARP.
    :cvar ETH_P_8021_Q: 802.1Q VLAN Extended Header.
    :cvar ETH_P_IPX: IPX over DIX.
    :cvar ETH_P_IPV6: IPv6 over bluebook.
    :cvar ETH_P_SLOW: Slow Protocol. See 802.3ad 43B.
    :cvar ETH_P_WCCP: Web-cache coordination protocol.
    :cvar ETH_P_PPP_DISC: PPPoE discovery messages.
    :cvar ETH_P_PPP_SES: PPPoE session messages.
    :cvar ETH_P_MPLS_UC: MPLS Unicast traffic.
    :cvar ETH_P_MPLS_MC: MPLS Multicast traffic.
    :cvar ETH_P_ATMMPOA: MultiProtocol Over ATM.
    :cvar ETH_P_ATMFATE: Frame-based ATM Transport over Ethernet.
    :cvar ETH_P_AOE: ATA over Ethernet.
    :cvar ETH_P_TIPC: TIPC.
    :cvar ETH_P_802_3: Dummy type for 802.3 frames.
    :cvar ETH_P_AX25: Dummy protocol id for AX.25.
    :cvar ETH_P_ALL: Every packet.
    :cvar ETH_P_802_2: 802.2 frames.
    :cvar ETH_P_SNAP: Internal only.
    :cvar ETH_P_DDCMP: DEC DDCMP: Internal only
    :cvar ETH_P_WAN_PPP: Dummy type for WAN PPP frames.
    :cvar ETH_P_PPP_MP: Dummy type for PPP MP frames.
    :cvar ETH_P_PPPTALK: Dummy type for Atalk over PPP.
    :cvar ETH_P_LOCALTALK: Localtalk pseudo type.
    :cvar ETH_P_TR_802_2: 802.2 frames.
    :cvar ETH_P_MOBITEX: Mobitex.
    :cvar ETH_P_CONTROL: Card specific control frames.
    :cvar ETH_P_IRDA: Linux-IrDA.
    :cvar ETH_P_ECONET: Acorn Econet.
    :cvar ETH_P_HDLC: HDLC frames.
    :cvar ETH_P_ARCNET: 1A for ArcNet.
    :cvar VALUE: The empty string value is permitted here to allow for
        detailed error reporting.
    """

    ETH_P_LOOP = "ETH_P_LOOP"
    ETH_P_PUP = "ETH_P_PUP"
    ETH_P_PUPAT = "ETH_P_PUPAT"
    ETH_P_IP = "ETH_P_IP"
    ETH_P_X25 = "ETH_P_X25"
    ETH_P_ARP = "ETH_P_ARP"
    ETH_P_BPQ = "ETH_P_BPQ"
    ETH_P_IEEEPUP = "ETH_P_IEEEPUP"
    ETH_P_IEEEPUPAT = "ETH_P_IEEEPUPAT"
    ETH_P_DEC = "ETH_P_DEC"
    ETH_P_DNA_DL = "ETH_P_DNA_DL"
    ETH_P_DNA_RC = "ETH_P_DNA_RC"
    ETH_P_DNA_RT = "ETH_P_DNA_RT"
    ETH_P_LAT = "ETH_P_LAT"
    ETH_P_DIAG = "ETH_P_DIAG"
    ETH_P_CUST = "ETH_P_CUST"
    ETH_P_SCA = "ETH_P_SCA"
    ETH_P_RARP = "ETH_P_RARP"
    ETH_P_ATALK = "ETH_P_ATALK"
    ETH_P_AARP = "ETH_P_AARP"
    ETH_P_8021_Q = "ETH_P_8021Q"
    ETH_P_IPX = "ETH_P_IPX"
    ETH_P_IPV6 = "ETH_P_IPV6"
    ETH_P_SLOW = "ETH_P_SLOW"
    ETH_P_WCCP = "ETH_P_WCCP"
    ETH_P_PPP_DISC = "ETH_P_PPP_DISC"
    ETH_P_PPP_SES = "ETH_P_PPP_SES"
    ETH_P_MPLS_UC = "ETH_P_MPLS_UC"
    ETH_P_MPLS_MC = "ETH_P_MPLS_MC"
    ETH_P_ATMMPOA = "ETH_P_ATMMPOA"
    ETH_P_ATMFATE = "ETH_P_ATMFATE"
    ETH_P_AOE = "ETH_P_AOE"
    ETH_P_TIPC = "ETH_P_TIPC"
    ETH_P_802_3 = "ETH_P_802_3"
    ETH_P_AX25 = "ETH_P_AX25"
    ETH_P_ALL = "ETH_P_ALL"
    ETH_P_802_2 = "ETH_P_802_2"
    ETH_P_SNAP = "ETH_P_SNAP"
    ETH_P_DDCMP = "ETH_P_DDCMP"
    ETH_P_WAN_PPP = "ETH_P_WAN_PPP"
    ETH_P_PPP_MP = "ETH_P_PPP_MP"
    ETH_P_PPPTALK = "ETH_P_PPPTALK"
    ETH_P_LOCALTALK = "ETH_P_LOCALTALK"
    ETH_P_TR_802_2 = "ETH_P_TR_802_2"
    ETH_P_MOBITEX = "ETH_P_MOBITEX"
    ETH_P_CONTROL = "ETH_P_CONTROL"
    ETH_P_IRDA = "ETH_P_IRDA"
    ETH_P_ECONET = "ETH_P_ECONET"
    ETH_P_HDLC = "ETH_P_HDLC"
    ETH_P_ARCNET = "ETH_P_ARCNET"
    VALUE = ""
