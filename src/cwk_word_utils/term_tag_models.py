"""Pydantic models for term tagging utilities."""

from pydantic import BaseModel, Field


class Tag(BaseModel):
    """Model representing a tag."""

    tag: str = Field(
        ...,
        pattern=r"^[a-z_]*$",
        description="The tag associated with a term list. Must be lowercase a-z or underscore.",
    )

    def __str__(self):
        return f"Tag: {self.tag}"

    def __repr__(self):
        return f"Tag(tag={self.tag!r})"


class Terms(BaseModel):
    """Model representing a list of terms."""

    terms: list[str] = Field(
        ...,
        description="The list of term:str matches that generate this tag.",
    )

    def __str__(self):
        return f"Terms: {self.terms}"

    def __repr__(self):
        return f"Terms(terms={self.terms!r})"


class TagTerms(BaseModel):
    """Model representing a tag and its associated term list."""

    tag: Tag
    terms: Terms

    def __str__(self):
        return f"TagTerms(tag={self.tag}, terms={self.terms})"

    def __repr__(self):
        return f"TagTerms(tag={self.tag!r}, terms={self.terms!r})"
