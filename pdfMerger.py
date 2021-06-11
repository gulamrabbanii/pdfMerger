# pip install pdfrw
# pip install os-sys

from pdfrw import PdfReader, PdfWriter
import os

source_dir = os.getcwd()

writer = PdfWriter()

for item in os.listdir(source_dir):
    if item.endswith('pdf'):
        writer.addpages(PdfReader(item).pages)

writer.write('result.pdf')
