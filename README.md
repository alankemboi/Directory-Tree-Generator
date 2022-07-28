# Directory Tree generator

💨Python app to recursively traverse through a directory and print its tree structure.

## Usage - ` main.py [-h] [-o [OUTPUT_FILE]] [-d] [-v] [ROOT_DIR]`

### Options:

`-h, --help ` shows all options and usage<br>
`-o [OUTPUT_FILE], --output-file [OUTPUT_FILE] ` Generate a full directory tree and save it to a file<br>
`-d, --dir-only ` Generate a directory only tree<br>
`-v,--version ` show program's version number and exit

## Examples

`$ python tree.py -v`<br>
` RP Tree v0.1.0`

`$ python tree.py ./sample_dir -o hello.md ` <br>

```
hello\
│
├──hello\
│   ├──hello.py
│   └──__init__.py
│
├──tests\
│   └──test_hello.py
│
├──LICENCE
├──README.md
├──requirements.txt
└──setup.py
```

`$ python tree.py -h `

```
usage: tree [-h] [-o [OUTPUT_FILE]] [-d] [-v] [ROOT_DIR]

RP Tree, a directory tree generator

positional arguments:
  ROOT_DIR              Generate a full directory tree starting at ROOT_DIR

options:
  -h, --help            show this help message and exit
  -o [OUTPUT_FILE], --output-file [OUTPUT_FILE]
                        Generate a full directory tree and save it to a file
  -d, --dir-only        Generate a directory only tree
  -v, --version         show program's version number and exit

Thanks for using RP Tree
```

## Contributions are welcome, Thanks!💖
