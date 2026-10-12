## StarDict (.ifo)

<!--
This document is generated from source code. Do NOT edit.
To update, modify plugins/stardict/__init__.py file, then run ./scripts/gen
-->

### General Information

| Attribute | Value |
| --------- | ----- |
| Name | Stardict |
| snake_case_name | stardict |
| Description | StarDict (.ifo) |
| Extensions | `.ifo` |
| Read support | Yes |
| Write support | Yes |
| Single-file | No |
| Kind | 📁 directory |
| Sort-on-write | Always |
| Sort key | `stardict` |
| Wiki | [StarDict]() |
| Website | [huzheng.org/stardict]() |

### Read options

| Name | Default | Type | Comment |
| ---- | ------- | ---- | ------- |
| xdxf_to_html | `True` | bool | Convert XDXF entries to HTML |
| xsl | `False` | bool | Use XSL transformation |
| unicode_errors | `strict` | str | What to do with Unicode decoding errors |

### Write options

| Name | Default | Type | Comment |
| ---- | ------- | ---- | ------- |
| large_file | `False` | bool | Use idxoffsetbits=64 bits, for large files only |
| dictzip | `False` | bool | Compress .dict file to .dict.dz |
| dictzip_syn | `False` | bool | Compress .syn file to .syn.dz |
| sametypesequence |  | str | Definition format: h=html, m=plaintext, x=xdxf |
| stardict_client | `False` | bool | Modify html entries for StarDict 3.0 |
| audio_goldendict | `False` | bool | Convert audio links for GoldenDict (desktop) |
| audio_icon | `True` | bool | Add glossary's audio icon |
| autosqlite | `True` | bool | Auto-enable/disable SQLite option based on global SQLite mode. |
| sqlite | `False` | bool | Use SQLite to limit memory usage. |
| max_file_size | `0` | int | Max .dict file size before splitting into multiple glossaries;<br />0 means use default based on large_file (4 GiB or 64-bit limit).<br /> Examples: 100m, 1g |

### StarDict program HTML support

The StarDict application renders HTML definitions with a very limited engine
(its `stardict-html-parsedata-plugin`). It only understands these tags:

- inline formatting: `b`, `big`, `i`, `s`, `sub`, `sup`, `small`, `tt`, `u`,
  `font` (`face` and `color` attributes)
- line breaks: `br` (literal `<br>` only) and `hr`
- links and images: `a` (`href`), `img` (`src`)

All other tags - including `div`, `p`, `span`, `ol`, `li`, `blockquote`,
`table` and headings - are dropped and their content is rendered inline. As a
result:

- line breaks and block boundaries (keyword, sibling definitions, examples)
  are lost,
- ordered and unordered lists are not numbered or bulleted,
- `blockquote` indentation is not applied,
- the self-closing `<br/>` form is **not** recognized as a line break
  (PyGlossary writes `<br/>`), so explicit line breaks are dropped as well,
- inline formatting (bold, italic, underline, sub/superscript, `font` color)
  is preserved.

This matters for `sametypesequence=h` (HTML) and `sametypesequence=x` (XDXF)
entries, which PyGlossary converts to HTML on read (see the `xdxf_to_html`
option). That HTML relies on `div`, `ol`/`li` and `<br/>` for layout, so
entries will look degraded in the StarDict program. Viewers that render HTML
with a full web engine, such as GoldenDict or AyanDict, are recommended
instead.

See the
[StarDict HTML parsing plugin source]().

### Dictionary Applications/Tools

| Name & Website | Source code | License | Platforms | Language |
| -------------- | ----------- | ------- | --------- | -------- |
| [AyanDict]() | [@ilius/ayandict]() | GPL | Linux, Windows, Mac | Go |
| [GoldenDict-NG by @xiaoyifang]() | [@xiaoyifang/goldendict-ng]() | GPL | Linux, Windows, Mac | C++ |
| [GoldenDict]() | [@goldendict/goldendict]() | GPL | Linux, Windows, Mac | C++ |
| [SilverDict]() | [@Crissium/SilverDict]() | GPL | Web | Python |
| [StarDict]() | [@huzheng001/stardict-3]() | GPL | Linux, Windows, Mac | C++ |
| [QStarDict]() | [@a-rodin/qstardict]() | GPLv2 | Linux, Windows, Mac | C++ |
| [KOReader]() | [@koreader/koreader]() | AGPLv3 | Android, Amazon Kindle, Kobo eReader, PocketBook, Cervantes | Lua |
| [sdcv (command line)]() | [@Dushistov/sdcv]() | GPLv2 | Linux, Windows, Mac, Android | C++ |
| [QDict]() | [@namndev/QDict]() | Apache 2.0 | Android | Java |
| [GoldenDict Mobile (Free)]() | ― | Proprietary (Freemium) | Android |  |
| [GoldenDict Mobile (Full)]() | ― | Proprietary | Android |  |
| [WordMateX]() | ― | Proprietary | Android |  |
| [Fora Dictionary]() | ― | Proprietary (Freemium) | Android |  |
| [Fora Dictionary Pro]() | ― | Proprietary | Android |  |

### Related Formats

- [StarDict Textual File (.xml)](./stardict_textual.md)
- [StarDict (Merge Syns)](./stardict_merge_syns.md)
