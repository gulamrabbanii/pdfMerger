from PyPDF2 import PdfFileMerger
import os

merger = PdfFileMerger()

for item in os.listdir():
     if item.endswith('pdf'):
        merger.append(items)

merger.write('waste_pdf.pdf')
merger.close()
