# JSembed
Simple Python tool to embed JavaScript code in different types of files (pdf and svg for now)

## Rerequisites

- PyPDF2
- re
- argparse

## Install

```bash
$ git clone https://github.com/mathis2001/JSembed

$ cd JSembed

$ python3 jsembed.py
```

## Usage

```bash
$ python3 jsembed.py [--pdf path/to/input.pdf] [--svg path/to/input.svg] [--js path/to/input.js] [--output output.pdf or output.svg]
```

## Options

```bash

options:
  -h, --help                     show this help message and exit
  -p PDF, --pdf PDF              Path to the original PDF file
  -s SVG, --svg SVG              Path to the original SVG file
  -j JS, --js JS                 Path to the JavaScript file to embed
  -o OUTPUT, --output OUTPUT     Output file name (.pdf or .svg)

```

## Screenshots

![Usage](https://github.com/mathis2001/JSembed/assets/40497633/3d906be3-bf4a-4a26-b351-dbc8008648d7)
![PDF](https://github.com/mathis2001/JSembed/assets/40497633/01184dc9-b819-4abb-a668-17b44cabaf4c)
![SVG](https://github.com/mathis2001/JSembed/assets/40497633/8ea3e97a-6588-4d8f-bf34-03f4a05a9314)
