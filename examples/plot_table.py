import matplotlib.pyplot as plt
import sys
sys.path.insert(1, "/home/arthur/Dropbox/python")
from tctools import *

df = load_table('NP_EUROFER.DAT', sort='T', fill=0)
df['T'] = df['T'] - 273.15
plot_table(df, 'T')

df = load_table('52100MOD_COMP.TXT', sort='T')
df['T'] = df['T'] - 273.15
plot_table(df, 'T', colpattern='W(FCC_A1#1,*[!FE])')
plot_table(df, 'T', colpattern='W(*,C)')

plt.show()
