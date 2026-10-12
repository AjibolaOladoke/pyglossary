## Octopus MDict (.mdx)

<!--
This document is generated from source code. Do NOT edit.
To update, modify plugins/octopus_mdict/__init__.py file, then run ./scripts/gen
-->

### General Information

| Attribute | Value |
| --------- | ----- |
| Name | OctopusMdict |
| snake_case_name | octopus_mdict |
| Description | Octopus MDict (.mdx) |
| Extensions | `.mdx` |
| Read support | Yes |
| Write support | No |
| Single-file | No |
| Kind | 🔢 binary |
| Wiki | ― |
| Website | [Download - MDict.cn]() |

### Read options

| Name | Default | Type | Comment |
| ---- | ------- | ---- | ------- |
| encoding |  | str | Encoding/charset |
| substyle | `True` | bool | Enable substyle |
| same_dir_data_files | `False` | bool | Read data files from same directory |
| audio | `False` | bool | Enable audio objects |

### Dependencies for reading

PyPI Links: [xxhash]()

To install, run:

```sh
pip3 install xxhash
```

### `python-lzo` is required for **some** MDX glossaries.

First try converting your MDX file, if failed (`AssertionError` probably),
then try to install [LZO library and Python binding](../lzo.md).

### Dictionary Applications/Tools

| Name & Website | Source code | License | Platforms | Language |
| -------------- | ----------- | ------- | --------- | -------- |
| [MDict]() | ― | Proprietary | Android, iOS, Windows, Mac |  |
| [GoldenDict-NG by @xiaoyifang]() | [@xiaoyifang/goldendict-ng]() | GPL | Linux, Windows, Mac | C++ |
| [GoldenDict]() | [@goldendict/goldendict]() | GPL | Linux, Windows, Mac | C++ |
| [SilverDict]() | [@Crissium/SilverDict]() | GPL | Web | Python |
