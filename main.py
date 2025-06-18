# main.py
import os
def huan_luyen():
    print("Đang huấn luyện mô hình...")
    os.system("python src/tai_du_lieu.py")
    os.system("python src/huan_luyen.py")
def du_doan():
    print("Dự đoán email spam hoặc không...")
    os.system("python src/du_doan.py")
def main():
    while True:
        print("\n=== PHÂN LOẠI EMAIL SPAM ===")
        print("1. Huấn luyện mô hình")
        print("2. Dự đoán email")
        print("3. Thoát")
        choice = input("Chọn chức năng (1/2/3): ").strip()
        if choice == "1":
            huan_luyen()
        elif choice == "2":
            du_doan()
        elif choice == "3":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
if __name__ == "__main__":
    main()
