import numpy as np
import pandas as pd
import re
import string
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "DuLieu", "emails.csv")
def lam_sach_email(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)  # xóa link
    text = re.sub(r'\S+@\S+', '', text)  # xóa email
    text = re.sub(r'\d+', '', text)  # xóa số
    text = text.translate(str.maketrans('', '', string.punctuation))  # xóa dấu câu
    text = re.sub(r'\s+', ' ', text).strip()  # xóa khoảng trắng thừa
    words = text.split() # bỏ stopwords + stemming
    return ' '.join(words)
df = pd.read_csv(file_path)
df['Message'] = df['Message'].apply(lam_sach_email)
# Ghi lại file đã xử lý vào thư mục DuLieu
output_path = os.path.join(BASE_DIR, "DuLieu", "nemail.csv")
df.to_csv(output_path, index=False)
