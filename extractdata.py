import pandas as pd
df = pd.read_excel('file2extract.xls')
a =df['Email']
a.to_csv('textextracted.txt',header='Email',index=None,mode='w')
