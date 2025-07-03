import joblib
import numpy as np
import os
import sys

# Đường dẫn model đã lưu
model_path = r"C:\Users\User\PycharmProjects\PhanLoaiEmailSpam\Models\my_naive_bayes_model.pkl"

# Kiểm tra tồn tại
if not os.path.exists(model_path):
    print("❌ Không tìm thấy mô hình. Vui lòng huấn luyện và lưu mô hình trước.")
    sys.exit()

# Tải mô hình
model = joblib.load(model_path)

vocab = model['vocab']
word_to_index = model['word_to_index']
log_prob_spam = model['log_prob_spam']
log_prob_ham = model['log_prob_ham']
p_spam = model['p_spam']
p_ham = model['p_ham']

# Nhập nội dung email
email_input = input("📧 Nhập nội dung email cần kiểm tra: ").strip()
words = email_input.lower().split()

# Chuyển email thành vector đếm
X_input = np.zeros(len(vocab), dtype=int)
for word in words:
    if word in word_to_index:
        X_input[word_to_index[word]] += 1

# Tính xác suất theo log
log_likelihood_spam = np.sum(X_input * log_prob_spam) + p_spam
log_likelihood_ham = np.sum(X_input * log_prob_ham) + p_ham

# Dự đoán
if log_likelihood_spam > log_likelihood_ham:
    print("🛑 Đây là email SPAM.")
else:
    print("✅ Đây KHÔNG PHẢI là email spam.")
