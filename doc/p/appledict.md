## AppleDict Source

<!--
This document is generated from source code. Do NOT edit.
To update, modify plugins/appledict/__init__.py file, then run ./scripts/gen
-->

### General Information

| Attribute | Value |
| --------- | ----- |
| Name | AppleDict |
| snake_case_name | appledict |
| Description | AppleDict Source |
| Extensions | `.apple` |
| Read support | Yes |
| Write support | Yes |
| Single-file | No |
| Kind | 📁 directory |
| Sort-on-write | No (by default) |
| Sort key | (`headword_lower`) |
| Wiki | ― |
| Website | [Dictionary User Guide for Mac]() |

### Write options

| Name | Default | Type | Comment |
| ---- | ------- | ---- | ------- |
| clean_html | `True` | bool | use BeautifulSoup parser |
| css |  | str | custom .css file path |
| xsl |  | str | custom XSL transformations file path |
| default_prefs | `None` | dict | default prefs in python dict format |
| prefs_html |  | str | preferences XHTML file path |
| front_back_matter |  | str | XML file path with top-level tag |
| jing | `False` | bool | run Jing check on generated XML |
| indexes |  | str | Additional indexes to dictionary entries |

### Dependencies for reading

PyPI Links: [lxml]()

To install, run:

```sh
pip3 install lxml
```

### Dependencies for writing

PyPI Links: [lxml](), [beautifulsoup4](), [html5lib](), [colorize-pinyin](), [pymorphy3]()

To install, run

```sh
pip3 install lxml beautifulsoup4 html5lib colorize-pinyin pymorphy3
```

### Also see:

See [doc/apple.md](../apple.md) for additional AppleDict instructions.

### Dictionary Applications/Tools

| Name & Website | Source code | License | Platforms | Language |
| -------------- | ----------- | ------- | --------- | -------- |
| [Dictionary Development Kit]() | ― | Unknown | Mac |  |

### Related Formats

- [AppleDict Binary](./appledict_bin.md)
