import sys
import numpy as np
import pandas as pd
from pcsaft_electrolyte import pcsaft_den, pcsaft_hres, pcsaft_gres, pcsaft_sres
def gres(x,m,s,e,t=325,p=101325):
    den = pcsaft_den(x, m, s, e, t, p, phase='liq')
    calc = pcsaft_gres(x, m, s, e, t, den)
    return calc

if __name__ == '__main__':
#    print(gres(x,m,s,e))
    t = 298.15
    p = 101325
    df = pd.read_csv('parameters.csv',index_col='name')
    data = df.loc[sys.argv[1]]
    M = 200000.0 if np.isnan(data['M']) else data['M']
    dens = pcsaft_den(x=np.asarray([1.0]), m=np.asarray([M*0.0352]), s=np.asarray([2.939]), e=np.asarray([229.450]), t=273.15, p=101325, phase='liq')
    #dens mol/m3
    dens *= M/1000000
    print(dens)
    sys.exit()
    dens = pcsaft_den(x=np.asarray([1.0]), m=np.asarray([18.015*0.06687]), s=np.asarray([2.7927]), e=np.asarray([353.9449]), t=273.15, p=101325, phase='liq')
    dens *= 18.015/1000000
    print(dens)
