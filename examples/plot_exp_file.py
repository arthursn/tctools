import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(1, '/home/arthur/Dropbox/python')

from tctools import *

# fname = 'FE-C.EXP'
# fname = 'FE-CEM.EXP'
# fname = 'CU-ZN.EXP'
fname = 'AL-CU.EXP'
# fname = 'CARBON_PHASES.EXP'
# fname = 'PHASE_FRACTION.EXP'
# fname = 'AL6063.EXP'
# fname = 'ISOPLETH_S1.EXP'
# fname = 'ISOPLETH.EXP'

fig, ax = plt.subplots()
plot_exp_datafile(fname, ax, False, 'k-')
plt.show()

# fig, ax = plt.subplots()
# plot_exp_datafile('FE-C.EXP', ax, False, 'k-')
# plot_exp_datafile('FE-CEM.EXP', ax, False, 'k:')
# ax.set_xlim(0, 7)
# plt.show()