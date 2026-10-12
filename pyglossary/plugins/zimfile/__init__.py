"""
PyGlossary Zim format plugin.

OpenZIM archives (``.zim``) as used by Kiwix offline Wikipedia and dictionaries.
Read-only ``Reader`` indexes ZIM entries and extracts article HTML as glossary
definitions keyed by title.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyglossary.option import UnicodeErrorsOption

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
	"optionsProp",
	"singleFile",
	"website",
	"wiki",
]

enable = True
lname = "zim"
name = "Zim"
description = "Zim (.zim, for Kiwix)"
extensions = (".zim",)
extensionCreate = ".zim"
singleFile = True
kind = "binary"
wiki = ")"
website = (
	"",
	"OpenZIM",
)
relatedFormats: list[str] = ["Aard2Slob"]
optionsProp: dict[str, Option] = {
	"text_unicode_errors": UnicodeErrorsOption(
		comment="Unicode Errors for plaintext, values: `strict`, `ignore`, `replace`",
	),
	"html_unicode_errors": UnicodeErrorsOption(
		comment="Unicode Errors for HTML, values: `strict`, `ignore`, `replace`",
	),
}

# 

# to download zim files:
# 
# 

# I can't find any way to download zim files from 
# which wiki.openzim.org points at for downloading zim files
