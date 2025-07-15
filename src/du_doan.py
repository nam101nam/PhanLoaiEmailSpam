import joblib
import numpy as np
import os
import sys

from sympy.codegen.ast import Return

# Đường dẫn model đã lưu
model_path = r"C:\Users\User\PycharmProjects\PhanLoaiEmailSpam\Models\my_naive_bayes_model.pkl"

# Kiểm tra tồn tại
if not os.path.exists(model_path):
    sys.exit(3)

# tai mo hinh
model = joblib.load(model_path)

vocab = model['vocab']
word_to_index = model['word_to_index']
log_prob_spam = model['log_prob_spam']
log_prob_ham = model['log_prob_ham']
p_spam = model['p_spam']
p_ham = model['p_ham']


if sys.argv[1]=="": sys.exit(2)


# nhap noi dung
email_input = sys.argv[1].strip()
words = email_input.lower().split()

# chuyen email
X_input = np.zeros(len(vocab), dtype=int)
for word in words:
    if word in word_to_index:
        X_input[word_to_index[word]] += 1

# tinh sac xuat
log_likelihood_spam = np.sum(X_input * log_prob_spam) + p_spam
log_likelihood_ham = np.sum(X_input * log_prob_ham) + p_ham

# Du doan
if log_likelihood_spam > log_likelihood_ham:
    sys.exit(1)
else:
    sys.exit(0)
