import sys
import re
import argparse
from PyPDF2 import PdfFileWriter, PdfFileReader

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--pdf", help="Path to the original PDF file", type=str)
parser.add_argument("-s", "--svg", help="Path to the original SVG file", type=str)
parser.add_argument("-j", "--js", help="Path to the JavaScript file to embed", type=str)
parser.add_argument("-o", "--output", help="Output file name (.pdf)", type=str)
args = parser.parse_args()

class bcolors:
	OK = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	RESET = '\033[0m'
	INFO = '\033[94m'

def PDF_JS_Embed(pdf_path, js_path, output_path):
    outputwriter = PdfFileWriter()
    print(f'{bcolors.INFO}[*]{bcolors.RESET} Opening {bcolors.INFO}{pdf_path}{bcolors.RESET}...')
    inputwriter = PdfFileReader(open(pdf_path, "rb"))

    with open(js_path, 'r') as js_file:
        javascript_code = js_file.read()

        for page_num in range(inputwriter.getNumPages()):
            outputwriter.addPage(inputwriter.getPage(page_num - 1))
            print(f'{bcolors.INFO}[*]{bcolors.RESET} Embedding JavaScript code from {bcolors.INFO}{js_path}{bcolors.RESET} in page {page_num+1}...')
            outputwriter.addJS(javascript_code)

        with open(output_path, 'wb') as output_file:
            outputwriter.write(output_file)

def SVG_JS_Embed(svg_path, js_path, output_svg_path):
    with open(js_path, 'r') as js_file:
        javascript_code = js_file.read()

    print(f'{bcolors.INFO}[*]{bcolors.RESET} Opening {bcolors.INFO}{svg_path}{bcolors.RESET}...')
    with open(svg_path, 'r') as svg_file:
        svg_content = svg_file.read()

    print(f'{bcolors.INFO}[*]{bcolors.RESET} Searching insertion point...')
    match = re.search(r'<svg[^>]*>', svg_content)
    if match:
        insert_position = match.end()
    else:
        print(f'{bcolors.FAIL}[!]{bcolors.RESET} Error: <svg> tag not found in the provided file.')
        return

    print(f'{bcolors.INFO}[*]{bcolors.RESET} Embeding JavaScript code from {bcolors.INFO}{js_path}{bcolors.RESET}...')
    embedded_svg_content = svg_content[:insert_position] + f'<script>{javascript_code}</script>' + svg_content[insert_position:]

    with open(output_svg_path, 'w') as output_file:
        output_file.write(embedded_svg_content)

def main():
    input_js = args.js
    output = args.output

    if len(sys.argv) != 7:
        print(f'{bcolors.FAIL}[-]{bcolors.RESET} Error: invalid number of arguments.')
        print(f'{bcolors.WARNING}[-]{bcolors.RESET} Usage: python3 jsembed.py [--pdf path/to/input.pdf] [--svg path/to/input.svg] [--js path/to/input.js] [--output output.pdf or output.svg]')
        exit(0)
    if args.pdf:
        input = args.pdf
        PDF_JS_Embed(input, input_js, output)
    if args.svg:
        input = args.svg
        SVG_JS_Embed(input, input_js, output)

    print(f'{bcolors.OK}[+]{bcolors.RESET} JavaScript embedded successfully. Output file: {bcolors.OK}{output}{bcolors.RESET}')

try:
    main()
except Exception as e:
    print(e)
