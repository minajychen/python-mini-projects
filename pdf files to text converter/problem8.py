#problem8
#jiang-ying mina chen
#a function that converts pdf files into text

import PyPDF2
import sys

def pdf_text_converter(pdf_file):
    """this is a pdf to text converter function.
    your terminal command-line format should be:
    python problem8.py text_convert 'pdf_file'"""
    args = sys.argv[1:]
    text_convert=False
    if args[0]== 'text_convert':
        text_convert=True
        del args[0]
    for pdf_file in args:
        if text_convert:
            textopen=open(pdf_file+'.txt','a')
            pdfopen=open(pdf_file, 'rb')
            pdfreader=PyPDF2.PdfFileReader(pdfopen)
            pagenum=0
            while pagenum < int(pdfreader.numPages):
                pageObj=pdfreader.getPage(pagenum)
                textopen.write(pageObj.extractText())
                pagenum+=1
            pdfopen.close()

if __name__ == '__main__':
  pdf_text_converter("pdf")