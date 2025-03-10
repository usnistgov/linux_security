from dataclasses import dataclass, field
from typing import Optional

from scap.entity_state_int_type import EntityStateIntType
from scap.entity_state_string_type import EntityStateStringType
from scap.state_type import StateType

__NAMESPACE__ = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"


@dataclass
class PartitionState(StateType):
    """The partition_state element defines the different information associated
    with a partition.

    This includes the name, filesystem type, mount options, total space,
    space used, and space left. Please refer to the individual elements
    in the schema for more details about what each represents.

    :ivar mount_point: The mount_point element contains a string that
        represents the mount point of a partition on the local system.
    :ivar device: The device element contains a string that represents
        the name of the device.
    :ivar uuid: The uuid element contains a string that represents the
        universally unique identifier associated with a partition.
    :ivar fs_type: The fs_type element contains a string that represents
        the type of filesystem on a partition.
    :ivar mount_options: The mount_options element contains a string
        that represents the mount options associated with a partition.
        Implementation note: not all mount options are visible in
        /etc/mtab or /proc/mounts.  A complete source of additional
        mount options is the f_flag field of 'struct statvfs'.  See
        statvfs(2).  /etc/fstab may have additional mount options, but
        it need not contain all mounted filesystems, so it MUST NOT be
        relied upon.  Implementers MUST be sure to get all mount options
        in some way.
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
    :ivar block_size: The block_size element contains an integer that
        represents the actual byte size of each physical block on the
        partition's block device. This is the same block size used to
        compute the total_space, space_used, and space_left.
    """

    class Meta:
        name = "partition_state"
        namespace = "http://oval.mitre.org/XMLSchema/oval-definitions-5#linux"

    mount_point: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    device: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    uuid: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    fs_type: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    mount_options: Optional[EntityStateStringType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    total_space: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    space_used: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    space_left: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    space_left_for_unprivileged_users: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
    block_size: Optional[EntityStateIntType] = field(
        default=None,
        metadata={
            "type": "Element",
            
        },
    )
