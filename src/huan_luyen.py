# #Khai báo thư viện
# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB
# import joblib
# import os
#
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# file_path = os.path.join(BASE_DIR, "DuLieu", "nemail.csv")
# #Nhận data
# spam_df=pd.read_csv(file_path)
# #Thêm cột spam với giá trị từ cột Category nếu giá trị spam=0, ham=1
# spam_df['spam']=spam_df['Category'].apply(lambda x: 1 if x=='spam' else 0)
# #Chia bộ dữ liệu ra 2 phần 1 phần để huấn luyện, 1 phần để đánh giá
# x_train,x_test,y_train,y_test=train_test_split(spam_df.Message,spam_df.spam, test_size=0.25)
# x_train = x_train.fillna('')
# x_test = x_test.fillna('')
# #Chuyển văn bản thành ma trận
# cv = CountVectorizer()
# x_train_count=cv.fit_transform(x_train)
# x_train_count.toarray()
# #Huấn luyện mô hình
# model=MultinomialNB()
# model.fit(x_train_count, y_train)
# x_test_count=cv.transform(x_test)
# print("Tỉ lệ mô hình:",model.score(x_test_count, y_test))
# # Lưu mô hình và vectorizer vào file Models
# model_path = os.path.join(BASE_DIR, "Models", "naive_bayes_model.pkl")
# vec_path = os.path.join(BASE_DIR, "Models", "count_vectorizer.pkl")
# joblib.dump(model, model_path)
# joblib.dump(cv, vec_path)



import pandas as pd
import numpy as np
import pickle
import os
# Doc du lieu tu file csv
data = pd.read_csv(r'C:\Users\User\PycharmProjects\PhanLoaiEmailSpam\DuLieu\nemail.csv')

# Tach du lieu
category = data['Category'].values
messages = data['Message'].values

# Tach tu
tokenized_messages = [msg.lower().split() for msg in messages]

vocab = sorted(set(word for msg in tokenized_messages for word in msg))

word_to_index = {word: idx for idx, word in enumerate(vocab)}
# Tao ma tran co so hang la so email, so cot la so tu
X = np.zeros((len(messages), len(vocab)), dtype=int)
# Chuyen cac email thanh dang ma tran danh so
for i, msg in enumerate(tokenized_messages):
    for word in msg:
        if word in word_to_index:
            X[i][word_to_index[word]] += 1

# Chuyen email dau la spam -> 1 con khong spam -> ham
y = np.array([1 if label == 'spam' else 0 for label in category])
# Tách spam và ham
X_spam = X[y == 1]
X_ham = X[y == 0]

# Tính xác suất tiên nghiệm
p_spam = X_spam.shape[0] / X.shape[0]
p_ham = X_ham.shape[0] / X.shape[0]

# Tính xác suất có điều kiện (Laplace smoothing)
alpha = 1  # smoothing
spam_word_count = X_spam.sum(axis=0) + alpha
ham_word_count = X_ham.sum(axis=0) + alpha

# Tổng số từ sau smoothing
total_spam_words = spam_word_count.sum()
total_ham_words = ham_word_count.sum()

# Log-likelihood để tránh underflow
log_prob_spam = np.log(spam_word_count / total_spam_words)
log_prob_ham = np.log(ham_word_count / total_ham_words)

def predict(msg):
    tokens = msg.lower().split()
    x = np.zeros(len(vocab), dtype=int)
    for word in tokens:
        if word in word_to_index:
            x[word_to_index[word]] += 1

    # Tính log xác suất
    log_p_spam = np.log(p_spam) + np.dot(x, log_prob_spam)
    log_p_ham = np.log(p_ham) + np.dot(x, log_prob_ham)

    return 'spam' if log_p_spam > log_p_ham else 'ham'
# print(predict("you are won, please connect to phone number 911"))       # spam
# print(predict("Let's meet for lunch today"))  # ham
# Luu mo hinh
save_dir = r"C:\Users\User\PycharmProjects\PhanLoaiEmailSpam\Models"
model_path = os.path.join(save_dir, "my_naive_bayes_model.pkl")
model_data = {
    'vocab': vocab,
    'word_to_index': word_to_index,
    'log_prob_spam': log_prob_spam,
    'log_prob_ham': log_prob_ham,
    'p_spam': p_spam,
    'p_ham': p_ham
}
with open(model_path, 'wb') as f:
    pickle.dump(model_data, f)

