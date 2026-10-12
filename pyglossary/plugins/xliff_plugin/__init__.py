"""
PyGlossary XLIFF format plugin.

XML Localization Interchange File Format glossaries (``.xlf``, ``.xliff``).
Read-only ``Reader`` extracts ``<trans-unit>`` source/target pairs as entries.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from .reader import Reader

if TYPE_CHECKING:
	from pyglossary.option import Option

__all__ = [
	"Reader",
	"description",
	"enable",
	"extensionCreate",
	"extensions",
	"kind",
	"lname",
	"name",
	"singleFile",
	"wiki",
]

enable = True
lname = "xliff"
name = "XLIFF"
description = "XLIFF (.xlf, .xliff)"
extensions = (".xlf", ".xliff")
extensionCreate = ".xlf"
singleFile = True
kind = "text"
wiki = ""
website = (
	"",
	"XLIFF Version 1.2",
)
optionsProp: dict[str, Option] = {}
relatedFormats: list[str] = ["TMX"]

# XLIFF Version 2.2: 
