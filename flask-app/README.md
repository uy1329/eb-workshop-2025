# Flask Application - AWS Elastic Beanstalk Workshop

## 📋 Hướng dẫn Deploy

### Bước 1: Sửa thông tin sinh viên

Mở file `application.py` và sửa thông tin của bạn:

```python
STUDENT_INFO = {
    "name": "Họ tên của bạn",
    "student_id": "MSSV của bạn",
    "class": "Lớp của bạn",
    "university": "Trường của bạn"
}
```

### Bước 2: Test ứng dụng trên local (Tùy chọn)

```bash
# Cài đặt Python packages
pip install -r requirements.txt

# Chạy ứng dụng
python application.py

# Truy cập: http://localhost:5000
```

### Bước 3: Đóng gói ứng dụng

**Quan trọng**: Chỉ nén các FILE, KHÔNG nén thư mục!

1. Chọn 2 files: `application.py` và `requirements.txt`
2. Click chuột phải → Send to → Compressed (zipped) folder
3. Đặt tên: `flask-app.zip`

### Bước 4: Deploy lên AWS Elastic Beanstalk

1. Vào **AWS Elastic Beanstalk Console**
2. Chọn environment đã tạo (ví dụ: `Elastic-beanstalk-demo-env`)
3. Click **Upload and deploy**
4. Click **Choose file** → chọn file `flask-app.zip`
5. Version label: nhập `v1.0` (hoặc tên khác)
6. Click **Deploy**
7. Đợi 2-5 phút để deploy hoàn tất
8. Click vào Environment URL để xem ứng dụng

### Bước 5: Xác minh ứng dụng

Kiểm tra các routes sau:

- `http://your-env-url/` - Trang chủ với thông tin sinh viên
- `http://your-env-url/about` - Trang About
- `http://your-env-url/api/info` - API trả về JSON
- `http://your-env-url/health` - Health check

## 🎯 Routes có sẵn

| Route | Mô tả |
|-------|-------|
| `/` | Trang chủ hiển thị thông tin sinh viên |
| `/about` | Trang giới thiệu về ứng dụng |
| `/api/info` | API endpoint trả về JSON |
| `/health` | Health check cho monitoring |

## 📸 Chụp ảnh để hoàn thiện workshop

Sau khi deploy thành công, hãy chụp các ảnh sau:

### 3.3 Verify Application (5 ảnh)
- `0032.png` - Trang chủ ứng dụng
- `0033.png` - Trang About
- `0034.png` - Response JSON từ /api/info
- `0035.png` - Response JSON từ /health
- `0036.png` - Request logs trong EB Console

### 4. Monitor (4 ảnh)
- `0001.png` - EC2 Dashboard
- `0002.png` - EB Health Dashboard
- `0003.png` - CloudWatch Metrics
- `0004.png` - Environment Events

## 🛠️ Troubleshooting

### Lỗi: Application không chạy
- Kiểm tra file có tên đúng `application.py` không
- Kiểm tra PORT configuration
- Xem logs: EB Console → Logs → Request Logs

### Lỗi: Module not found
- Kiểm tra file `requirements.txt` có đúng không
- Đảm bảo đã list tất cả dependencies

### Lỗi: 502 Bad Gateway
- Ứng dụng có thể đang khởi động
- Đợi thêm vài phút
- Kiểm tra logs để xem lỗi chi tiết

## 📞 Support

Nếu gặp vấn đề, hãy kiểm tra:
1. Environment logs trong EB Console
2. CloudWatch logs
3. EC2 instance status
