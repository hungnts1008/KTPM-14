# 🧠 Chinese Chess Online - WebSocket + Pygame

Một ứng dụng cờ tướng chơi online 2 người sử dụng Python, Pygame và WebSocket.

---

## 📦 Mục lục

- [Giới thiệu](#giới-thiệu)
- [Tính năng](#tính-năng)
- [Cài đặt](#cài-đặt)
- [Cách chơi](#cách-chơi)
- [Cấu trúc dự án](#cấu-trúc-dự-án)
- [Đóng góp](#đóng-góp)
- [Giấy phép](#giấy-phép)

---

## 🚀 Giới thiệu

Dự án giúp bạn chơi cờ tướng với bạn bè qua mạng LAN hoặc internet bằng WebSocket. Giao diện sử dụng Pygame đơn giản và trực quan, xử lý thời gian thực.

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

