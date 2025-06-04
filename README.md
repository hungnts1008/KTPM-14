# 🧠 Chinese Chess Online - WebSocket + Pygame

Một ứng dụng cờ tướng (xiangqi) chơi online 2 người sử dụng Python, Pygame và WebSocket.

---

## 📦 Mục lục

- [Giới thiệu](#giới-thiệu)
- [Yêu cầu trước](#yêu-cầu-trước)
- [Tính năng](#tính-năng)
- [Cài đặt](#cài-đặt)
- [Cách chơi](#cách-chơi)
- [Cấu trúc dự án](#cấu-trúc-dự-án)
- [Đóng góp](#đóng-góp)
- [Giấy phép](#giấy-phép)

---

## 🚀 Giới thiệu

Dự án **Chinese Chess Online** cho phép bạn chơi cờ tướng với bạn bè qua mạng LAN hoặc Internet bằng cách sử dụng WebSocket để kết nối hai client. Giao diện đồ họa được xây dựng bằng Pygame, đơn giản và trực quan, đảm bảo trải nghiệm chơi mượt mà, thời gian thực.

---

## 🛠️ Yêu cầu trước

- **Python**: phiên bản 3.7 trở lên.  
- **Pygame**: phiên bản mới nhất (có trong `requirements.txt`).  
- **websockets**: thư viện WebSocket để kết nối client-server.  
- Kết nối mạng LAN hoặc Internet để hai client có thể giao tiếp với server.  

---

## ✅ Tính năng

- **Chơi 2 người qua mạng**: Kết nối client với server bằng WebSocket.  
- **Giao diện đồ họa**: Hiển thị bàn cờ, quân cờ, và các nước đi hợp lệ.  
- **Xử lý luật cờ**:  
  - Quản lý lượt đi (đỏ – đen).  
  - Kiểm tra chiếu tướng (check) và chiếu bí (game over).  
- **Tùy chỉnh cấu hình bàn cờ**: Hỗ trợ file cấu hình `standard.cfg` để định nghĩa vị trí khởi tạo.  
- **Thông báo thời gian thực**: Khi đối phương đi nước, client sẽ nhận và cập nhật ngay.  

---

## ⚙️ Cài đặt

1. Clone dự án về máy:

   ```bash
   git clone https://github.com/tenban/chinese-chess-online.git
   cd chinese-chess-online
   ```

2. Khởi tạo môi trường ảo (tuỳ chọn):

```bash
python -m venv venv
# Trên Linux/macOS
source venv/bin/activate
# Trên Windows
venv\Scripts\activate
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
├── client.py             
│   └─ Khởi động Pygame, kết nối đến server, xử lý giao diện và nhập xuất của người chơi.
│
├── server.py             
│   └─ WebSocket server: chịu trách nhiệm lắng nghe kết nối, trung chuyển thông tin nước đi giữa các client.
│
├── game/
│   ├── board.py          
│   │   └─ Lớp BoardGame: quản lý trạng thái bàn cờ, ô, kiểm tra nước đi hợp lệ, chiếu tướng, chiếu bí.
│   │
│   ├── pieces.py         
│   │   └─ Các lớp đại diện cho từng loại quân cờ (Tướng, Sĩ, Tượng, Xe, Pháo, Mã, Tốt), bao gồm luật di chuyển riêng.
│   │
│   ├── utils.py          
│   │   └─ Định nghĩa hằng số (màu sắc, kích thước ô, thư mục lưu trữ, v.v.).
│   │
│   └── presets/          
│       └── standard.cfg  
│           └─ File cấu hình bàn cờ chuẩn: định nghĩa vị trí khởi tạo của các quân. Bạn có thể tự tạo thêm preset khác nếu muốn.
│
├── requirements.txt      
│   └─ Danh sách các thư viện Python cần thiết (pygame, websockets...).
│
└── README.md             
    └─ Tài liệu hướng dẫn này.
```

