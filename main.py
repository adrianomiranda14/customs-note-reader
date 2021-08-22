# Idea


import pandas as pd
import tabula as tb
from tabula import read_pdf

paths_pdf = ["/content/drive/MyDrive/Miratoni/Miratoni/Imports/July/23-7-21/Main Lorry/Despacho FAC A21_623 _ 627.pdf"]
paths_csv = ["/content/drive/MyDrive/Miratoni/Miratoni/Imports/July/23-7-21/Main Lorry/Despacho FAC A21_623 _ 627.csv"]
pd.set_option("max_colwidth", 1000)
pd.set_option("display.max_rows", 200)

areas = [134.991, 303.078, 778.334, 576.778]
"""areas=[
[146.891,305.309,157.303,576.034],
[163.997,391.584,178.872,489.759],
[195.234,373.734,215.316,573.803],
[216.059,303.078,227.216,571.572],
[236.884,307.541,247.297,568.597],
[267.378,375.222,285.972,573.803],
[287.459,304.566,296.384,571.572],
[305.309,312.003,316.466,566.366],
[335.803,375.222,355.884,576.778],
[357.372,303.822,367.041,573.803],
[375.966,304.566,386.378,571.572],
[405.716,375.966,425.797,574.547],
[426.541,305.309,436.953,572.316],
[445.134,303.822,454.803,570.084],
[474.884,376.709,495.709,574.547],
[496.453,305.309,507.609,576.778],
[516.534,303.822,525.459,574.547],
[546.284,373.734,565.622,573.803],
[567.109,304.566,579.009,571.572],
[586.447,303.822,597.603,568.597],
[615.453,373.734,635.534,575.291],
[636.278,303.822,645.203,573.059],
[653.384,303.822,665.284,570.828],
[685.366,374.478,705.447,574.547],
[706.191,302.334,716.603,572.316],
[726.272,303.822,735.197,570.084],
[756.022,375.966,775.359,574.547]]
"""

df = tb.read_pdf(paths_pdf[0], pages="all", stream=True, area=[134.991, 303.078, 778.334, 576.778],
                 multiple_tables=True,
                 options="--columns 415,521,675,798"
                 )

first_page = tb.read_pdf(paths_pdf[0], pages=1, stream=True, area=[475.628, 297.872, 561.159, 576.778],
                         options="--columns 415,521,675,798"
                         )
df[0] = first_page[0]

all_df = pd.concat(df, axis=0, ignore_index=True)
all_df = all_df.dropna(how='all')

all_df.to_csv("C:\Users\adria\Documents\Dev\Customs Note Reader\customs note.csv")