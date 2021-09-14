import pandas as pd
import tabula as tb
import tabula
from PyPDF2 import PdfFileReader
from os import listdir
from os.path import isfile, join





def modifier(dffrompdf):
    first_value = [dffrompdf.columns[0]]  #string
    vals = dffrompdf.values.tolist()  #list of lists
    for unit in vals:
        first_value.append(unit[0])
    dffrompdf = first_value
    return dffrompdf  

def folder(folderpath):
    paths_pdf = [folderpath+'\\'+f for f in listdir(folderpath) if isfile(join(folderpath, f))]
    return paths_pdf


def pages(path):
    pdf = PdfFileReader(open(path[0],'rb'))
    pageno = pdf.getNumPages()
    no_of_pages = f"2-{pageno}"
    return no_of_pages