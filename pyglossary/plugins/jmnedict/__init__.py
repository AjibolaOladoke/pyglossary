"""
PyGlossary JMnedict format plugin.

Japanese proper-name dictionary XML companion to JMdict. Read-only ``Reader``
maps name entries with readings and translations into glossary entries.
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
	"optionsProp",
	"singleFile",
	"website",
	"wiki",
]

enable = True
lname = "jmnedict"
name = "JMnedict"
description = "JMnedict"
extensions = ()
extensionCreate = ""
singleFile = True
kind = "text"
wiki = ""
website = (
	"",
	"EDRDG Wiki",
)
relatedFormats: list[str] = ["JMDict", "EDICT2"]
optionsProp: dict[str, Option] = {}
