import pandas as pd
import tabula as tb
import tabula
from PyPDF2 import PdfFileReader
from helper import *
from os import listdir
from os.path import isfile, join
pd.set_option("max_colwidth", 1000)
pd.set_option("display.max_rows", 200)

def folder(folderpath):
    paths_pdf = [folderpath+'\\'+f for f in listdir(folderpath) if isfile(join(folderpath, f))]
    return paths_pdf

def pages(path):
    pdf = PdfFileReader(open(path,'rb'))
    pageno = pdf.getNumPages()
    no_of_pages = f"2-{pageno}"    
    return no_of_pages

def modifier(dffrompdf):
    first_value = [dffrompdf.columns[0]]  #string
    vals = dffrompdf.values.tolist()  #list of lists
    for unit in vals:
        first_value.append(unit[0])
    dffrompdf = first_value
    return dffrompdf 

paths_pdf = folder(r'C:\Users\adria\Desktop\Miratoni\Imports\September\10-09-21\Groupagem AM\Despachos')

desc_areas = [[146.891,303.45,156.559,574.175],[215.316,303.45,227.216,574.919],[285.228,303.45,296.384,574.175],[355.884,304.194,366.297,574.919],[425.797,303.45,437.697,575.663],[495.709,302.706,506.866,574.919],[566.366,304.194,577.522,574.175],[636.278,303.45,646.691,573.431],[706.191,304.194,716.603,574.919]]
code_areas = [[165.484,304.194,177.384,574.175],[235.397,303.45,246.553,574.175],[306.053,304.194,316.466,574.175],[375.222,303.45,387.866,574.919],[445.878,304.194,456.291,574.919],[516.534,303.45,526.947,575.663],[584.959,303.45,596.116,574.919],[656.359,304.194,666.772,574.919],[726.272,304.194,735.941,574.175]]
gr_wt_areas = [[196.722,490.875,206.391,574.919],[266.634,490.131,277.047,574.175],[335.803,490.875,346.959,574.919],[405.716,489.388,417.616,574.175],[475.628,490.875,486.784,574.175],[545.541,490.875,557.441,574.919],[615.453,490.875,627.353,574.919],[686.109,490.875,697.266,574.175],[756.022,490.875,765.691,574.919]]
net_wt_areas = [[206.391,490.875,216.803,574.175],[275.559,490.875,287.459,574.175],[346.216,490.875,356.628,574.175],[416.128,490.875,426.541,573.431],[486.041,490.875,496.453,574.175],[555.953,490.875,566.366,574.175],[626.609,490.875,636.278,574.919],[695.778,490.875,706.934,573.431],[765.691,490.875,775.359,574.175]]
value_areas = [[205.647,375.594,215.316,491.619],[275.559,375.594,285.972,490.875],[346.216,375.594,355.141,492.363],[416.128,375.594,425.053,492.363],[486.784,375.594,497.197,491.619],[555.953,375.594,566.366,491.619],[625.866,375.594,637.022,491.619],[696.522,375.594,705.447,490.619],[766.434,375.594,776.847,492.363]]
first_page_areas = [[487.528,298.988,499.428,574.175],[509.841,296.756,520.253,574.919],[539.591,487.156,550.003,573.431],[549.259,486.413,560.416,574.175],[549.259,374.85,560.416,486.413]]
normal_areas = [134.991, 303.078, 778.334, 576.778]

def read_despacho(path):
    no_of_pages = pages(path)
    desc = tb.read_pdf(path, pages=no_of_pages, stream=True, area=desc_areas,
                    multiple_tables=False, format="CSV")
    commcode = tb.read_pdf(path, pages=no_of_pages, stream=True, area=code_areas,
                    multiple_tables=False, format="CSV")
    gr_wgt = tb.read_pdf(path, pages=no_of_pages, stream=True, area=gr_wt_areas,
                    multiple_tables=False, format="CSV")
    nt_wgt = tb.read_pdf(path, pages=no_of_pages, stream=True, area=net_wt_areas,
                    multiple_tables=False, format="CSV")
    values = tb.read_pdf(path, pages=no_of_pages, stream=True, area=value_areas,
                    multiple_tables=False, format="CSV")

    all_items = [desc[0], commcode[0], gr_wgt[0], nt_wgt[0], values[0]]

    dict_for_df = {'Description':modifier(desc[0]),'PTCode':modifier(commcode[0]),'Gross Weight (kg)':modifier(gr_wgt[0]),'Net Weight(kg)':modifier(nt_wgt[0]),'Value (EUR)':modifier(values[0])}

    final = pd.DataFrame.from_dict(dict_for_df)

    pg1 = tb.read_pdf(path, pages=1, stream=True, area=first_page_areas,
                    multiple_tables=False, format="CSV")

    pg1_series = pd.Series(modifier(pg1[0]), index = final.columns)
    final = final.append(pg1_series, ignore_index=True)
    return final

def read_one_page(path):
    final = pd.DataFrame

    pg1 = tb.read_pdf(path, pages=1, stream=True, area=first_page_areas,
                    multiple_tables=False, format="CSV")

    pg1_series = pd.Series(modifier(pg1[0]), index = ['Description','PTCode','Gross Weight (kg)','Net Weight (kg)','Value (EUR)'])
    pg1_dict = pg1_series.to_dict
    pg1_df = pd.DataFrame.from_dict(pg1_series)
    final = pg1_df.transpose()
    return final

def commcode_translate(dataframe):
    dataframe['splitcode'] = 



for x in paths_pdf:
    pdf = PdfFileReader(open(x,'rb'))
    pageno = pdf.getNumPages()
    if int(pageno) > 1:
        final = read_despacho(x)
    else:
        final = read_one_page(x)
    final.to_csv(str(x).replace('.pdf','.csv'))