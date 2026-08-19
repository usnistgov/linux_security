from classes.baseline import BaselinePlatform
from classes.rule import EnforcementInfo, Rule


def get_enforcement_block(
    rule: Rule, platform: BaselinePlatform
) -> EnforcementInfo | None:
    if platform.os not in rule.platforms.keys():
        raise ValueError(
            f"Rule {rule.rule_id} does not support the supplied platform, {platform.os}"
        )
    if str(platform.version) not in rule.platforms[platform.os].versions.keys():
        raise ValueError(
            f"Rule {rule.rule_id} does not support the supplied platform, {platform.os}"
        )

    rule_platform = rule.platforms[platform.os]
    rule_platform_version = rule_platform.versions[str(platform.version)]

    enforcement_block = rule_platform.enforcement_info
    if rule_platform_version.enforcement_info:
        enforcement_block = rule_platform_version.enforcement_info

    return enforcement_block
