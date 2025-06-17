import numpy as np
import pandas as pd
df=pd.read_csv('../DuLieu/emails.csv')
data=df.fillna('')
data.head()
