# 🧠 Chinese Chess Online - WebSocket + Pygame

Một ứng dụng cờ tướng chơi online 2 người sử dụng Python, Pygame và WebSocket.

---

## 📦 Mục lục

- [Giới thiệu](#giới-thiệu)
- [Giới thiệu thành viên](#giới-thiệu-thành-viên)
- [Tính năng](#tính-năng)
- [Cài đặt](#cài-đặt)
- [Cách chơi](#cách-chơi)
- [Cấu trúc dự án](#cấu-trúc-dự-án)
- [Câu hỏi thường gặp](#câu-hỏi-thường-gặp)
- [Đóng góp](#đóng-góp)
- [Giấy phép](#giấy-phép)


---

## 🚀 Giới thiệu

Dự án giúp bạn chơi cờ tướng với bạn bè qua mạng LAN hoặc internet bằng WebSocket. Giao diện sử dụng Pygame đơn giản và trực quan, xử lý thời gian thực.

---

## 🧑‍💻 Giới thiệu thành viên

Dự án được thực hiện bởi các thành viên:
- Phạm Đức Hưng (Mã sinh viên: 22010479)
- Phạm Hoài Nam (Mã sinh viên: 22010183)
- Trần Thái Hưng (Mã sinh viên: 23010693)

---

## ✅ Tính năng

- Chơi 2 người qua mạng bằng WebSocket
- Hiển thị bàn cờ, quân cờ, nước đi hợp lệ
- Giao diện đồ họa bằng Pygame
- Quản lý lượt chơi, kiểm tra chiếu tướng

---

## ⚙️ Cài đặt

1. Clone dự án:

```bash
git clone https://github.com/tenban/chinese-chess-online.git
cd chinese-chess-online
```

2. Khởi tạo môi trường ảo (tuỳ chọn):

```bash
python -m venv venv
source venv/bin/activate
```

3. Cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

## 🕹️ Cách chơi
4. Chạy máy chủ WebSocket:

```bash
python server.py
```

5. Chạy ứng dụng Pygame:

```bash
python client.py
```

## 📁 Cấu trúc dự án
```plaintext
chinese-chess-online/
│
├── client.py             # Khởi động giao diện và xử lý client
├── server.py             # WebSocket server
├── game/
│   ├── board.py          # Lớp BoardGame, quản lý bàn cờ
│   ├── pieces.py         # Các lớp quân cờ
│   ├── utils.py          # Các hằng số, màu sắc
│   └── presets/          # File cấu hình bàn cờ
│       └── standard.cfg
├── requirements.txt
└── README.md
```
## ❓ Câu hỏi thường gặp

**1. Làm sao để kết nối hai máy tính chơi với nhau?**  
Bạn cần đảm bảo cả hai máy cùng kết nối vào cùng một mạng LAN hoặc biết địa chỉ IP của máy chủ. Máy khách nhập IP của máy chủ khi chạy `client.py`.

**2. Tôi gặp lỗi khi chạy Pygame hoặc WebSocket, phải làm sao?**  
Hãy kiểm tra lại phiên bản Python, cài đặt đúng các thư viện trong `requirements.txt` và đảm bảo firewall không chặn cổng WebSocket.

**3. Có thể chơi trên nhiều hệ điều hành không?**  
Có, dự án hỗ trợ Windows, macOS và Linux miễn là cài đặt được Python và các thư viện cần thiết.

---
## 🤝 Đóng góp

Chào mừng mọi đóng góp từ cộng đồng!

- Fork repository và tạo branch mới cho tính năng hoặc sửa lỗi.
- Gửi pull request kèm mô tả chi tiết thay đổi.
- Vui lòng tuân thủ phong cách code và quy tắc đặt tên của dự án.
- Nếu có ý tưởng hoặc phát hiện lỗi, hãy tạo issue để mọi người cùng thảo luận.

---

## 📜 Giấy phép

Dự án được phát hành theo giấy phép MIT. Bạn có thể tự do sử dụng, chỉnh sửa và phân phối lại mã nguồn với điều kiện giữ nguyên thông tin bản quyền ban đầu.

##
