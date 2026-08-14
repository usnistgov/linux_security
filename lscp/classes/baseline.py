from typing import List

from pydantic import BaseModel, field_serializer, field_validator
from utils.mobile_validator import validate

from .platforms import SupportedPlatform


class Section(BaseModel):
    section: str
    rules: List[str]


class Author(BaseModel):
    name: str
    organization: str


class Baseline(BaseModel):
    title: str
    description: str
    authors: List[Author]
    platform: SupportedPlatform
    profile: List[Section]

    @field_validator("platform", mode="before")
    @classmethod
    def validate_platform(cls, platform):
        if isinstance(platform, SupportedPlatform):
            return platform.value
        else:
            return SupportedPlatform[platform]

    @field_serializer("platform")
    def serialize_platform(self, platform: SupportedPlatform):
        return platform.name


if __name__ == "__main__":
    validate(Baseline)
