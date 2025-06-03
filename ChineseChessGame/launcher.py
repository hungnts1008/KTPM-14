import tkinter as tk
from tkinter import messagebox
from game.login import ManHinhDangNhap
import main  # import file main.py để gọi hàm main()

def on_click_vs_human(selection_window, user_info):
    """
    Khi bấm 'Chơi với người': đóng cửa sổ chọn chế độ
    và gọi thẳng main.main() để vào bàn cờ.
    """
    selection_window.destroy()
    # Gọi hàm main() từ main.py
    main.main()

def on_click_vs_computer():
    """
    Khi bấm 'Chơi với máy': hiển thị thông báo tạm thời.
    Bạn có thể thay bằng logic call AI sau này.
    """
    messagebox.showinfo("Thông báo", "Tính năng 'Chơi với máy' đang phát triển.")

def show_mode_selection(user_info):
    """
    Hiển thị cửa sổ Tkinter với 2 nút: 'Chơi với người' và 'Chơi với máy'.
    """
    sel_root = tk.Tk()
    sel_root.title("Chọn chế độ chơi")
    sel_root.geometry("300x150")
    sel_root.resizable(False, False)

    # Canh giữa màn hình
    screen_w = sel_root.winfo_screenwidth()
    screen_h = sel_root.winfo_screenheight()
    x = (screen_w // 2) - (300 // 2)
    y = (screen_h // 2) - (150 // 2)
    sel_root.geometry(f"300x150+{x}+{y}")

    btn_vs_human = tk.Button(
        sel_root,
        text="Chơi với người",
        width=20,
        height=2,
        command=lambda: on_click_vs_human(sel_root, user_info)
    )
    btn_vs_human.pack(pady=(20, 10))

    btn_vs_computer = tk.Button(
        sel_root,
        text="Chơi với máy",
        width=20,
        height=2,
        command=on_click_vs_computer
    )
    btn_vs_computer.pack()

    sel_root.mainloop()

def main():
    """
    Entry-point: 
    1) Hiển thị màn hình đăng nhập.
    2) Nếu đăng nhập thành công, show màn hình chọn chế độ.
    """
    # Màn hình đăng nhập
    root = tk.Tk()
    login_screen = ManHinhDangNhap(root)
    root.mainloop()

    user_info = login_screen.user_info
    if not user_info:
        # Nếu đóng cửa sổ hoặc login thất bại, dừng chương trình
        return

    # Hiển thị màn hình chọn chế độ
    show_mode_selection(user_info)
    # Khi bấm 'Chơi với người', hàm on_click_vs_human sẽ gọi main.main()

if __name__ == "__main__":
    main()
