# mypy: ignore-errors
# from 

"""
PyGlossary DIKT JSON format plugin.

JSON export format used by the DIKT dictionary tool chain. Write-only ``Writer``
serializes glossary entries into DIKT-compatible JSON records.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyglossary.option import (
	BoolOption,
	EncodingOption,
)

from .writer import Writer

if TYPE_CHECKING:
	from pyglossary.option import Option

__all__ = [
	"Writer",
	"description",
	"enable",
	"extensionCreate",
	"extensions",
	"kind",
	"lname",
	"name",
	"optionsProp",
	"singleFile",
	"website",
	"wiki",
]

enable = True
lname = "dikt_json"
name = "DiktJson"
description = "DIKT JSON (.json)"
extensions = ()
extensionCreate = ".json"
singleFile = True
kind = "text"
wiki = ""
website = ""
relatedFormats: list[str] = ["Json"]
optionsProp: dict[str, Option] = {
	"encoding": EncodingOption(),
	"enable_info": BoolOption(comment="Enable glossary info / metedata"),
	"resources": BoolOption(comment="Enable resources / data files"),
	"word_title": BoolOption(
		comment="add headwords title to beginning of definition",
	),
}
