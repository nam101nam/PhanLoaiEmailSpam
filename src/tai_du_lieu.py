import numpy as np
import pandas as pd
import re
import string
def lam_sach_email(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)  # xóa link
    text = re.sub(r'\S+@\S+', '', text)  # xóa email
    text = re.sub(r'\d+', '', text)  # xóa số
    text = text.translate(str.maketrans('', '', string.punctuation))  # xóa dấu câu
    text = re.sub(r'\s+', ' ', text).strip()  # xóa khoảng trắng thừa
    words = text.split() # bỏ stopwords + stemming
    return ' '.join(words)

df=pd.read_csv('../DuLieu/emails.csv')
df.loc[df['Category']=='spam','Category']=1
df.loc[df['Category']=='ham','Category']=0
df['Message'] = df['Message'].apply(lam_sach_email)
df.to_csv('../DuLieu/nemail.csv')
print(df)
