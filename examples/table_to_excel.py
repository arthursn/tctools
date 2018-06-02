import sys
sys.path.insert(1, '/home/arthur/Dropbox/python')
from tctools import table_to_excel

table_to_excel('NP_EUROFER.DAT', 'NP_EUROFER.xls', sort='T', fill=0, index=False)