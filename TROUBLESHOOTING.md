# 🔧 Khắc phục lỗi Deployment - Health Degraded

## Tình trạng hiện tại:
- Health: **Degraded** (Đỏ)
- Platform: Python 3.14 on Amazon Linux 2023
- Running version: elastic-beanstalk-demo-version-1

## Các bước khắc phục:

### Bước 1: Kiểm tra Logs
1. Trong EB Console, click tab **"Logs"**
2. Click **"Request Logs"** → **"Last 100 Lines"**
3. Đợi 1-2 phút, sau đó click **"Download"**
4. Mở file logs và tìm các dòng ERROR

### Bước 2: Các lỗi thường gặp

#### Lỗi 1: Module 'Flask' not found
**Nguyên nhân**: File `requirements.txt` thiếu hoặc sai

**Giải pháp**:
```
Flask==3.0.0
Werkzeug==3.0.1
```
- Đảm bảo file `requirements.txt` có đúng 2 dòng trên
- Tạo lại ZIP và deploy lại

#### Lỗi 2: Port binding error
**Nguyên nhân**: Flask không lắng nghe đúng port

**Kiểm tra**: File `application.py` dòng cuối phải có:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    application.run(host='0.0.0.0', port=port, debug=False)
```

#### Lỗi 3: Wrong file structure
**Nguyên nhân**: Nén thư mục thay vì nén files

**Giải pháp**:
- ĐÚNG: Chọn 2 files → nén → flask-app.zip
  ```
  flask-app.zip
    ├── application.py
    └── requirements.txt
  ```
- SAI: Chọn folder → nén
  ```
  flask-app.zip
    └── flask-app/
        ├── application.py
        └── requirements.txt
  ```

#### Lỗi 4: Python syntax error
**Nguyên nhân**: Code có lỗi cú pháp

**Giải pháp**: Test local trước:
```bash
python application.py
# Truy cập http://localhost:5000
```

### Bước 3: Deploy lại

Sau khi sửa lỗi:
1. Tạo lại file ZIP đúng cách
2. Vào EB Console → **Upload and deploy**
3. Chọn file ZIP mới
4. Version label: `v1.1` (tăng version)
5. Click **Deploy**
6. Đợi 2-5 phút

### Bước 4: Nếu vẫn lỗi

Gửi cho tôi:
1. Screenshot logs (phần có chữ ERROR)
2. Nội dung file `application.py` (dòng 1-20)
3. Nội dung file `requirements.txt`

## Checklist trước khi deploy:

✅ File `application.py` có tên CHÍNH XÁC (không phải `app.py`)
✅ File `requirements.txt` có Flask==3.0.0
✅ Chỉ nén 2 FILES, không nén folder
✅ File `application.py` có biến `application` (không phải `app`)
✅ Code đã test local thành công

## Liên hệ hỗ trợ:
- Copy logs lỗi và gửi cho giảng viên/trợ giảng
- Hoặc gửi screenshot cho tôi để debug
