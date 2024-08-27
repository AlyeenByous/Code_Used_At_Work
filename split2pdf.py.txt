# Basic program to take a multi page pdf and split it to single pages and save with a specific name.
# Naming system could be improved, but since the names get changed anyway, I didn't worry much about it.
# Based off of geeks4geeks and some answers found on StackExchange, but tailored.

from pypdf import PdfWriter, PdfReader
import os

path = input("Type the path here:  ")
inputpdf = PdfReader(open(path, "rb"))
rootpath='D:\\scripts\\pdfs'
dir = os.listdir(rootpath)

counter = 0
for i in range(0,len(inputpdf.pages),1):
    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    docname = "document-page%s.pdf"%i

    # if the file name I want exists, come up with a new unique one
    if docname in dir:  
        #print(docname)
        trythisname = "{name}({num}).pdf".format(name=docname,num=counter)
        while trythisname in dir:
            counter += 1
            trythisname = "{name}({num}).pdf".format(name=docname,num=counter) #basically just add numbers to make a unique name
        outputFileName = os.path.join('D:\\scripts\\pdfs', trythisname)
        with open(outputFileName, "wb") as outputStream:
            output.write(outputStream)
        counter += 1
    else:  
        outputFileName = os.path.join('D:\\scripts\\pdfs', "document-page%s.pdf"%i)
        with open(outputFileName, "wb") as outputStream:
            output.write(outputStream)
    
