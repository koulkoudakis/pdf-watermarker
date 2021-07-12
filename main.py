
# Name: pdf watermarker
# Version: 0.1.0
# Description: Simple script adds predetermined watermark to .pdf file
# Author: Sharome Burton
# Repository: https://github.com/koulkoudakis/pdf-watermarker
# Repl: https://replit.com/@Koulkoudakis/pdf-watermarker#main.py

import PyPDF2 as pdf2

template = pdf2.PdfFileReader(open('pdf-1.pdf', 'rb'))
watermark = pdf2.PdfFileReader(open('wtr.pdf', 'rb'))
output = pdf2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open('result.pdf', 'wb') as file:
    output.write(file)