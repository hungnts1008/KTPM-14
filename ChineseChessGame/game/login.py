# game/login.py

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Thêm Pillow để xử lý ảnh
import mysql.connector

class ManHinhDangNhap:
    def __init__(self, master):
        self.master = master
        self.master.title("Đăng nhập")
        self.master.geometry("500x400")  # tăng kích thước cho đẹp
        self.master.resizable(False, False)
        # đặt ở giữa màn hình
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width // 2) - (500 // 2)
        y = (screen_height // 2) - (400 // 2)
        self.master.geometry(f"500x400+{x}+{y}")
        self.master.configure(bg='white')
                

        self.login_successful = False

        # Load ảnh nền
        self.background_image = Image.open("images/screenshots/logo.jpg")  # sửa path nếu cần
        self.background_image = self.background_image.resize((500, 400), Image.Resampling.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Đặt ảnh làm nền
        # đặt ảnh làm nền ở giữa màn hình
        self.background_label = tk.Label(master, image=self.background_photo)
        self.background_label.place(relx=0.5, rely=0.5, anchor="center")

        
        self.frame = tk.Frame(master, bg='white', bd=2, relief=tk.RIDGE)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        
        
        # Frame để chứa các ô nhập, nút đăng nhập
        self.frame = tk.Frame(master, bg='white', bd=5)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Các widget
        self.label_username = tk.Label(self.frame, text="Tên đăng nhập:", bg="white")
        self.label_username.grid(row=0, column=0, padx=10, pady=5)

        self.entry_username = tk.Entry(self.frame)
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)

        self.label_password = tk.Label(self.frame, text="Mật khẩu:", bg="white")
        self.label_password.grid(row=1, column=0, padx=10, pady=5)

        self.entry_password = tk.Entry(self.frame, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        self.button_login = tk.Button(self.frame, text="Đăng nhập", command=self.dang_nhap)
        self.button_login.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.user_info = None
        
    def get_connection(self):
        conn= mysql.connector.connect(
            host="localhost",
            user="root",
            password="duchungpro108",
            database="chinese_chess" 
        )
        if conn.is_connected():
            print("✅ Kết nối thành công!")
        else:
            print("❌ Kết nối thất bại!")
        return conn
            
    def register_user(self,id, handle, fullname, phone, email, elo, username, password,status):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (id, handle, fullname, phone, email, elo, username, password,status) VALUES (%s, %s, %s, %s, %s, %d, %s, %s,%s)",
                           (id, handle, fullname, phone, email, elo, username, password,status))
            conn.commit()
            return True
        except mysql.connector.errors.IntegrityError:
            print("Username đã tồn tại.")
            return False
        finally:
            cursor.close()
            conn.close()

    def dang_nhap(self):
        # username = self.entry_username.get()
        # password = self.entry_password.get()

        # if username == "admin" and password == "1234":
        #     messagebox.showinfo("Đăng nhập thành công", "Chào mừng!")
        #     self.login_successful = True
        #     self.master.destroy()
        # else:
        #     messagebox.showerror("Thất bại", "Sai tài khoản hoặc mật khẩu.")
        conn = self.get_connection()
        cursor = conn.cursor()
        username = self.entry_username.get()
        password = self.entry_password.get()
        cursor.execute("SELECT * FROM Player WHERE UserUserName = %s AND UserPassword = %s", (username, password))
        result = cursor.fetchone()
        cursor.close()
        if result:
            messagebox.showinfo("Đăng nhập thành công", "Chào mừng!")   
            self.login_successful = True
            elo = result[5]
            self.user_info = {"username": username, "elo": elo}
            self.master.destroy()
        else:
            messagebox.showerror("Thất bại", "Sai tài khoản hoặc mật khẩu.")
