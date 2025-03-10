from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = (
    "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"
)


@dataclass
class PartitionItem:
    """
    The partition_item stores information about a partition on the local system.

    :ivar mount_point: The mount_point element contains a string that
        represents the mount point of a partition on the local system.
    :ivar device: The device element contains a string that represents
        the name of the device.
    :ivar uuid: The uuid element contains a string that represents the
        universally unique identifier associated with a partition.
    :ivar fs_type: The fs_type element contains a string that represents
        the type of filesystem on a partition.
    :ivar mount_options: The mount_options element contains a string
        that represents a mount option associated with a partition on
        the local system. Implementation note: not all mount options are
        visible in /etc/mtab or /proc/mounts.  A complete source of
        additional mount options is the f_flag field of 'struct
        statvfs'.  See statvfs(2).  /etc/fstab may have additional mount
        options, but it need not contain all mounted filesystems, so it
        MUST NOT be relied upon.  Implementers MUST be sure to get all
        mount options in some way.
    :ivar total_space: The total_space element contains an integer that
        represents the total number of physical blocks on a partition.
    :ivar space_used: The space_used element contains an integer that
        represents the number of physical blocks used on a partition.
    :ivar space_left: The space_left element contains an integer that
        represents the number of physical blocks left on a partition
        available to be used by privileged users.
    :ivar space_left_for_unprivileged_users: The
        space_left_for_unprivileged_users element contains an integer
        that represents the number of physical blocks remaining on a
        partition that are available to be used by unprivileged users.
    :ivar block_size: The block_size element contains an integer
        representing the actual byte size of each physical block on the
        partition's block device. This is the same block size used to
        compute the total_space, space_used, and space_left.
    """

    class Meta:
        name = "partition_item"
        namespace = "http://oval.mitre.org/XMLSchema/oval-system-characteristics-5#linux"

    mount_point: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    device: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    fs_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    mount_options: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            
        },
    )
    total_space: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    space_used: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    space_left: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    space_left_for_unprivileged_users: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    block_size: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
