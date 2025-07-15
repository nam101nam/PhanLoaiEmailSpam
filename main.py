# main.py
import os
import time
import tkinter as tk
from tkinter import *


def DuDoan(label, e):
    email_content = e.get()
    exit_code = os.system(f'python src/du_doan.py "{email_content}"')
    if exit_code == 1:
        label.config(text="Kết quả: Email spam.")
    elif exit_code == 0:
        label.config(text="Kết quả: Email không spam.")
    elif exit_code == 2:
        label.config(text="Kết quả: Nội dung email chưa được truyền vào.")
    elif exit_code == 3:
        label.config(text="Kết quả: Hiện chưa có mô hình nào.")


def HuanLuyen(label):
    label.config(text="Kết quả: Đang huấn luyện...")
    label.update()
    os.system("python src/tai_du_lieu.py")
    os.system("python src/huan_luyen.py")
    label.config(text="Kết quả: Huấn luyện thành công.")


def main():
    root = Tk()
    # root.geometry("600x400")
    e = Entry(root, width=100,font=('Arial',10))
    e.insert(0, "Nhập nội dung email cần kiểm tra: ")
    e.grid(row=0, columnspan=2,padx=20,pady=20,ipady=10,ipadx=10)

    label = Label(root, text="Kết quả: ",font=('Arial',10))
    label.grid(row=2, columnspan=2,pady=20)

    button = Button(root, text="Kiểm tra", command=lambda: DuDoan(label, e),font=('Arial',10))
    button.grid(row=1, column=1)

    button1 = Button(root, text="Huấn luyện mô hình", command=lambda: HuanLuyen(label),font=('Arial',10))
    button1.grid(row=1, column=0)

    root.mainloop()


if __name__ == "__main__":
    main()
