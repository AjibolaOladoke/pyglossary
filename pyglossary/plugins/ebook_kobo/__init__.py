"""
PyGlossary Kobo ebook format plugin.

Kobo e-reader dictionary packages (``.kobo`` / ``.kobo.zip``). Write-only
``Writer`` produces the Kobo-specific dictionary bundle layout from sorted
glossary entries.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyglossary.flags import NEVER

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
lname = "kobo"
name = "Kobo"
description = "Kobo E-Reader Dictionary"
extensions = (".kobo",)
extensionCreate = ".kobo.zip"
singleFile = False
kind = "package"
sortOnWrite = NEVER
wiki = ""
website = (
	"",
	"www.kobo.com",
)
relatedFormats: list[str] = ["Dictfile", "Epub2", "Mobi"]

# 


optionsProp: dict[str, Option] = {}


# Penelope option: marisa_index_size=1000000
