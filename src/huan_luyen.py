#Khai báo thư viện
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "DuLieu", "nemail.csv")
#Nhận data
spam_df=pd.read_csv(file_path)
#Thêm cột spam với giá trị từ cột Category nếu giá trị spam=0, ham=1
spam_df['spam']=spam_df['Category'].apply(lambda x: 1 if x=='spam' else 0)
#Chia bộ dữ liệu ra 2 phần 1 phần để huấn luyện, 1 phần để đánh giá
x_train,x_test,y_train,y_test=train_test_split(spam_df.Message,spam_df.spam, test_size=0.25)
x_train = x_train.fillna('')
x_test = x_test.fillna('')
#Chuyển văn bản thành ma trận
cv = CountVectorizer()
x_train_count=cv.fit_transform(x_train)
x_train_count.toarray()
#Huấn luyện mô hình
model=MultinomialNB()
model.fit(x_train_count, y_train)
# #pre-test ham
# email_ham=["hey wanna meet up for the game?"]
# email_ham_count=cv.transform(email_ham)
# print(model.predict(email_ham_count))
# # pre-test spam
# email_spam=[(input("Nhập nội dung email:"))]
# email_spam_count=cv.transform(email_spam)
# print(model.predict(email_spam_count))
#test model
x_test_count=cv.transform(x_test)
print("Tỉ lệ mô hình:",model.score(x_test_count, y_test))
# Lưu mô hình và vectorizer vào file Models
model_path = os.path.join(BASE_DIR, "Models", "naive_bayes_model.pkl")
vec_path = os.path.join(BASE_DIR, "Models", "count_vectorizer.pkl")
joblib.dump(model, model_path)
joblib.dump(cv, vec_path)

