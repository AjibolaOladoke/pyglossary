"""
PyGlossary EDICT2 format plugin.

Extended EDICT/CEDICT line-oriented Japanese-English dictionary (``.u8`` and
related layouts). Read-only ``Reader`` parses kanji, readings, and glosses with
optional pinyin and summarization helpers for long entries.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyglossary.option import (
	BoolOption,
	EncodingOption,
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
lname = "edict2"
name = "EDICT2"
description = "EDICT2 (CEDICT) (.u8)"
extensions = (".u8",)
extensionCreate = ""
singleFile = True
kind = "text"
wiki = ""
website = None

# Websites / info for different uses of format:

# CC-CEDICT: Chinese-English (122k entries)
# "", "CC-CEDICT Editor"

# HanDeDict: Chinese-German (144k entries)
# "",
# "Herunterladen - HanDeDict @ Zydeo Wörterbuch Chinesisch-Deutsch"

# CFDICT: Chinese-French (56k entries)
# "",
# "Dictionnaire chinois français _ 汉法词典 - Chine Informations"

# CC-Canto is Pleco Software's addition of Cantonese language readings
# in Jyutping transcription to CC-CEDICT
# "",

relatedFormats: list[str] = ["JMDict", "JMnedict", "cc-kedict"]

optionsProp: dict[str, Option] = {
	"encoding": EncodingOption(),
	"traditional_title": BoolOption(
		comment="Use traditional Chinese for entry titles/keys",
	),
	"colorize_tones": BoolOption(
		comment="Set to false to disable tones coloring",
	),
	"link_references": BoolOption(
		comment="Create links to references to other entries",
	),
	"summary_alternatives": BoolOption(
		comment=(
			"Include English definition summaries as alternative terms (old behavior)"
		),
	),
}
