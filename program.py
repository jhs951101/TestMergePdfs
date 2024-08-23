# pip install 'PyPDF2<3.0' (python 3.11.4)

from PyPDF2 import PdfFileMerger, PdfFileReader

inputPaths = ['input1.pdf', 'input2.pdf',]
merger = PdfFileMerger()

for i in range(len(inputPaths)):
    merger.append(PdfFileReader(open(inputPaths[i], 'rb')))
    
merger.write('output.pdf')