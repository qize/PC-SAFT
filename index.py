import sys
import pandas as pd

df = pd.read_csv('parameters.csv',index_col='name')
get = df.loc[sys.argv[1]]
get2 = get[get.notna()]
if 'm' in get2:
    print(get2['m'])
else:
    print(get2['m/M'])
