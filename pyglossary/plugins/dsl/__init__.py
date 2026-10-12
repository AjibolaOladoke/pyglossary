"""
PyGlossary ABBYY Lingvo DSL format plugin.

Textual ``.dsl`` dictionaries from ABBYY Lingvo with markup for abbreviations,
examples, and audio references. Read-only plugin: imports ``Reader`` only and
exposes encoding and styling options for DSL source files.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyglossary.option import (
	BoolOption,
	EncodingOption,
	StrOption,
)

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
lname = "dsl"
name = "ABBYYLingvoDSL"
description = "ABBYY Lingvo DSL (.dsl)"
extensions = (".dsl",)
extensionCreate = ".dsl"
singleFile = True
kind = "text"
wiki = ""
website = (
	"",
	"www.lingvo.ru",
)
relatedFormats: list[str] = ["LingoesLDF"]
optionsProp: dict[str, Option] = {
	"encoding": EncodingOption(),
	"audio": BoolOption(
		comment="Enable audio objects",
	),
	"example_color": StrOption(
		comment="Examples color",
	),
	"abbrev": StrOption(
		customValue=False,
		values=["", "hover"],
		comment="Load and apply abbreviation file (`_abrv.dsl`)",
	),
}

# ABBYY is a Russian company
# 
# 
# 


# {{{
# modified to work around codepoints that are not supported by `unichr`.
# 
# January 15, 2003 | Fredrik Lundh


# Removes HTML or XML character references and entities from a text string.
#
# @param text The HTML (or XML) source text.
# @return The plain text, as a Unicode string, if necessary.
