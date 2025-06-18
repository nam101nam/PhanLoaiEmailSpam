import pandas as pd
import joblib
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "Models", "naive_bayes_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "Models", "count_vectorizer.pkl")

# Kiểm tra tồn tại của model
if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
    print("Không tìm thấy mô hình Vui lòng huấn luyện mô hình trước.")
    exit()
#Tải mô hình và vectorizer
model = joblib.load(model_path)
cv = joblib.load(vectorizer_path)
#Nhập nội dung email cần kiểm tra
email_input = input("Nhập nội dung email: ").strip()
email_list = [email_input]
#biến đổi thành vector
email_count = cv.transform(email_list)
#Dự đoán
prediction = model.predict(email_count)
#in kết quả
if prediction[0] == 1:
    print("Đây là email SPAM.")
else:
    print("Đây KHÔNG PHẢI là email spam.")
