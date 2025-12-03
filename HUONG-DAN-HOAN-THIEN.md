# 📋 CHECKLIST HOÀN THIỆN DỰ ÁN

## ✅ BƯỚC 1: TẠO CODE ỨNG DỤNG FLASK

### 1.1 Tạo folder dự án
```
Tạo folder: C:\my-flask-app
```

### 1.2 Tạo file `application.py`

Tạo file `C:\my-flask-app\application.py` với nội dung:

```python
from flask import Flask, jsonify, render_template_string
from datetime import datetime

# Elastic Beanstalk cần biến tên 'application'
application = Flask(__name__)

# ========== THÔNG TIN CỦA BẠN - THAY ĐỔI Ở ĐÂY ==========
STUDENT_INFO = {
    "name": "Nguyễn Văn A",           # ← Đổi tên của bạn
    "student_id": "555555",            # ← Đổi MSSV của bạn
    "class": "IT01-K66",               # ← Đổi lớp của bạn
    "university": "Đại học",           # ← Đổi tên trường
    "subject": "Cloud Computing với AWS",
    "project": "Triển khai ứng dụng trên AWS Elastic Beanstalk",
    "deployment_date": datetime.now().strftime("%B %Y")
}
# =========================================================

@application.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AWS Elastic Beanstalk Demo</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            .container {
                background: rgba(255, 255, 255, 0.95);
                border-radius: 20px;
                padding: 50px;
                max-width: 800px;
                width: 100%;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                animation: fadeIn 0.8s ease-in;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            .header {
                text-align: center;
                margin-bottom: 40px;
            }
            .header h1 {
                color: #667eea;
                font-size: 2.5em;
                margin-bottom: 10px;
            }
            .header .emoji {
                font-size: 4em;
                animation: bounce 2s infinite;
            }
            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-10px); }
            }
            .badge {
                background: linear-gradient(135deg, #4CAF50, #45a049);
                color: white;
                padding: 15px 30px;
                border-radius: 50px;
                display: inline-block;
                margin: 20px 0;
                font-weight: bold;
                font-size: 1.1em;
                box-shadow: 0 4px 15px rgba(76, 175, 80, 0.4);
            }
            .info-box {
                background: #f8f9fa;
                border-left: 5px solid #667eea;
                padding: 20px;
                margin: 20px 0;
                border-radius: 5px;
            }
            .info-box h3 {
                color: #333;
                margin-bottom: 15px;
                font-size: 1.3em;
            }
            .info-item {
                display: flex;
                padding: 10px 0;
                border-bottom: 1px solid #e0e0e0;
            }
            .info-item:last-child {
                border-bottom: none;
            }
            .info-label {
                font-weight: bold;
                color: #555;
                min-width: 150px;
            }
            .info-value {
                color: #333;
            }
            .buttons {
                display: flex;
                gap: 15px;
                justify-content: center;
                margin-top: 30px;
                flex-wrap: wrap;
            }
            .btn {
                padding: 12px 25px;
                border: none;
                border-radius: 25px;
                font-size: 1em;
                cursor: pointer;
                text-decoration: none;
                display: inline-block;
                transition: all 0.3s ease;
                font-weight: 500;
            }
            .btn-primary {
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
            }
            .btn-primary:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
            }
            .btn-secondary {
                background: #6c757d;
                color: white;
            }
            .btn-secondary:hover {
                background: #5a6268;
                transform: translateY(-2px);
            }
            .footer {
                text-align: center;
                margin-top: 30px;
                color: #666;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="emoji">🚀</div>
                <h1>AWS Elastic Beanstalk</h1>
                <div class="badge">✅ Triển khai thành công!</div>
            </div>
            
            <div class="info-box">
                <h3>📊 Thông tin sinh viên</h3>
                <div class="info-item">
                    <span class="info-label">Họ và tên:</span>
                    <span class="info-value">{{ student.name }}</span>
                </div>
                <div class="info-item">
                    <span class="info-label">Mã số sinh viên:</span>
                    <span class="info-value">{{ student.student_id }}</span>
                </div>
                <div class="info-item">
                    <span class="info-label">Lớp:</span>
                    <span class="info-value">{{ student.class }}</span>
                </div>
                <div class="info-item">
                    <span class="info-label">Trường:</span>
                    <span class="info-value">{{ student.university }}</span>
                </div>
            </div>

            <div class="info-box">
                <h3>📚 Thông tin đồ án</h3>
                <div class="info-item">
                    <span class="info-label">Môn học:</span>
                    <span class="info-value">{{ student.subject }}</span>
                </div>
                <div class="info-item">
                    <span class="info-label">Đề tài:</span>
                    <span class="info-value">{{ student.project }}</span>
                </div>
                <div class="info-item">
                    <span class="info-label">Thời gian:</span>
                    <span class="info-value">{{ student.deployment_date }}</span>
                </div>
            </div>

            <div class="buttons">
                <a href="/about" class="btn btn-primary">📖 Giới thiệu</a>
                <a href="/api/info" class="btn btn-secondary">📡 API Info</a>
                <a href="/health" class="btn btn-secondary">💚 Health Check</a>
            </div>

            <div class="footer">
                <p>🔧 Powered by AWS Elastic Beanstalk | Python Flask</p>
            </div>
        </div>
    </body>
    </html>
    ''', student=STUDENT_INFO)

@application.route('/about')
def about():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Giới thiệu - AWS Elastic Beanstalk</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
            }
            .container {
                max-width: 900px;
                margin: 0 auto;
                background: white;
                border-radius: 20px;
                padding: 40px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            }
            h1 { color: #667eea; margin-bottom: 20px; }
            h2 { color: #555; margin: 30px 0 15px; }
            p { line-height: 1.8; color: #333; margin-bottom: 15px; }
            ul { margin-left: 30px; line-height: 2; color: #555; }
            .back-btn {
                display: inline-block;
                margin-top: 30px;
                padding: 12px 25px;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                text-decoration: none;
                border-radius: 25px;
                transition: all 0.3s;
            }
            .back-btn:hover { transform: translateY(-2px); }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📖 Giới thiệu về Đồ án</h1>
            
            <h2>🎯 Mục tiêu</h2>
            <p>Đồ án này nhằm mục đích thực hành triển khai ứng dụng web lên AWS Elastic Beanstalk, 
            một dịch vụ Platform as a Service (PaaS) giúp đơn giản hóa việc deploy và quản lý ứng dụng.</p>

            <h2>🛠️ Công nghệ sử dụng</h2>
            <ul>
                <li><strong>AWS Elastic Beanstalk</strong>: Nền tảng triển khai</li>
                <li><strong>Python 3.11</strong>: Ngôn ngữ lập trình</li>
                <li><strong>Flask 3.0</strong>: Web framework</li>
                <li><strong>EC2</strong>: Virtual server</li>
                <li><strong>CloudWatch</strong>: Giám sát và logging</li>
            </ul>

            <h2>✨ Tính năng</h2>
            <ul>
                <li>Trang chủ hiển thị thông tin sinh viên</li>
                <li>Trang giới thiệu về đồ án</li>
                <li>API endpoint trả về thông tin JSON</li>
                <li>Health check endpoint cho monitoring</li>
                <li>Responsive design, hoạt động tốt trên mobile</li>
            </ul>

            <h2>📦 Quy trình triển khai</h2>
            <ul>
                <li>Tạo và cấu hình ứng dụng Flask</li>
                <li>Đóng gói ứng dụng thành file ZIP</li>
                <li>Tạo môi trường Elastic Beanstalk</li>
                <li>Upload và deploy code</li>
                <li>Giám sát và kiểm tra ứng dụng</li>
            </ul>

            <a href="/" class="back-btn">⬅️ Quay lại trang chủ</a>
        </div>
    </body>
    </html>
    ''')

@application.route('/api/info')
def api_info():
    """API endpoint trả về thông tin dạng JSON"""
    return jsonify({
        "status": "success",
        "message": "API is working!",
        "student_info": STUDENT_INFO,
        "server_time": datetime.now().isoformat(),
        "endpoints": {
            "home": "/",
            "about": "/about",
            "api_info": "/api/info",
            "health": "/health"
        }
    })

@application.route('/health')
def health():
    """Health check endpoint cho Elastic Beanstalk monitoring"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "message": "Application is running successfully!",
        "version": "1.0.0"
    })

# Để test local
if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000, debug=True)
```

### 1.3 Tạo file `requirements.txt`

Tạo file `C:\my-flask-app\requirements.txt`:

```txt
Flask==3.0.0
Werkzeug==3.0.1
```

### 1.4 Kiểm tra cấu trúc folder

```
C:\my-flask-app\
├── application.py
└── requirements.txt
```

---

## ✅ BƯỚC 2: TEST ỨNG DỤNG LOCAL (TÙY CHỌN)

### 2.1 Mở PowerShell/Terminal
```powershell
cd C:\my-flask-app
```

### 2.2 Cài đặt Python packages
```powershell
pip install -r requirements.txt
```

### 2.3 Chạy ứng dụng
```powershell
python application.py
```

### 2.4 Mở browser
```
http://localhost:8000
```

Kiểm tra:
- ✅ Trang chủ hiển thị thông tin của bạn
- ✅ http://localhost:8000/about - Trang giới thiệu
- ✅ http://localhost:8000/api/info - JSON response
- ✅ http://localhost:8000/health - Health check

### 2.5 Dừng ứng dụng
```
Nhấn Ctrl+C trong terminal
```

---

## ✅ BƯỚC 3: ĐÓNG GÓI ỨNG DỤNG

### 3.1 Mở Windows Explorer
```
Mở folder: C:\my-flask-app
```

### 3.2 Chọn TẤT CẢ files
```
- Chọn application.py
- Chọn requirements.txt
(Ctrl + A để chọn tất cả)
```

### 3.3 Tạo file ZIP
```
1. Click chuột phải vào files đã chọn
2. Chọn "Send to" > "Compressed (zipped) folder"
3. Đổi tên thành: my-flask-app.zip
```

### 3.4 Xác minh ZIP structure
```
Mở file my-flask-app.zip và kiểm tra:

my-flask-app.zip
├── application.py
└── requirements.txt

❌ KHÔNG ĐƯỢC có folder bên trong!
✅ Files phải nằm ngay ở root level của ZIP
```

---

## 📸 BƯỚC 4: DANH SÁCH ẢNH CẦN CHỤP

### 📂 Folder: `static/images/2.prerequisite/`

| File | Mô tả | Đã có |
|------|-------|-------|
| 0001.png | IAM Console - trang chính | ✅ |
| 0002.png | IAM Policies - danh sách ElasticBeanstalk policies | ✅ |
| 0003.png | EC2 Key Pairs - Create key pair form | ✅ |

**✅ Phần 2 ĐÃ ĐỦ ẢNH!**

---

### 📂 Folder: `static/images/3.deployapp/`

| File | Mô tả | Đã có |
|------|-------|-------|
| 0001.png | EB Console - Create Application button | ✅ |
| 0002.png | Configure environment - Environment name | ✅ |
| 0003.png | Platform selection - Python 3.11 | ✅ |
| 0004.png | Upload application code - Choose file | ✅ |
| 0005.png | Service Access - IAM roles selection | ✅ |
| 0006.png | IAM - Create service role step 1 | ✅ |
| 0007.png | IAM - Attach policies to service role | ✅ |
| 0008.png | IAM - Service role name | ✅ |
| 0009.png | EB - Service role selected | ✅ |
| 0010.png | IAM - Create EC2 instance profile step 1 | ✅ |
| 0011.png | IAM - Attach policies to EC2 role | ✅ |
| 0012.png | IAM - EC2 instance profile name | ✅ |
| 0013.png | EB - Both roles selected | ✅ |
| 0014.png | EB - EC2 key pair selected | ✅ |
| 0015.png | EB - Networking configuration | ✅ |
| 0016.png | EB - Database and tags | ✅ |
| 0017.png | EB - Instance configuration | ✅ |
| 0018.png | EB - Capacity - Single instance | ✅ |
| 0019.png | EB - Instance types - t3.micro | ✅ |
| 0020.png | EB - Monitoring configuration | ✅ |
| 0021.png | EB - Managed platform updates | ✅ |
| 0022.png | EB - Rolling updates | ✅ |
| 0023.png | EB - Platform software configuration | ✅ |
| 0024.png | Không cần | ❌ |
| 0025.png | EB - Review step 1-2 | ✅ |
| 0026.png | EB - Review step 3 | ✅ |
| 0027.png | EB - Review step 4 | ✅ |
| 0028.png | EB - Review step 5 | ✅ |
| 0029.png | EB - Environment creating (Events tab) | ✅ |
| 0030.png | EB - Environment health OK (green) | ✅ |
| 0031.png | EB - Application URL highlighted | ✅ |

**✅ Phần 3 ĐÃ ĐỦ ẢNH!**

---

### 📂 Folder: `static/images/3.deployapp/` (tiếp - cho phần Verify)

**CẦN CHỤP THÊM:**

| File | Mô tả | Cách chụp |
|------|-------|-----------|
| 0032.png | Trang chủ app đang chạy | Mở URL EB trong browser, chụp trang chủ với thông tin sinh viên |
| 0033.png | Trang About | Click nút "Giới thiệu", chụp trang about |
| 0034.png | API Info endpoint | Vào URL/api/info, chụp JSON response |
| 0035.png | Health check endpoint | Vào URL/health, chụp JSON response |
| 0036.png | Request Logs | EB Console > Logs > Request Logs button |

**❌ CẦN 5 ẢNH NỮA (0032-0036)**

---

### 📂 Folder: `static/images/4.monitor/`

**CẦN CHỤP:**

| File | Mô tả | Cách chụp |
|------|-------|-----------|
| 0001.png | EC2 Dashboard | EC2 Console, show instance created by EB |
| 0002.png | EB Health Dashboard | EB Console > Health tab |
| 0003.png | CloudWatch Metrics | EB Console > Monitoring tab, show charts |
| 0004.png | Environment Events | EB Console > Events tab |

**❌ CẦN 4 ẢNH (0001-0004)**

---

## 🎯 BƯỚC 5: QUY TRÌNH DEPLOY HOÀN CHỈNH

### Bước 5.1: Chuẩn bị
- [x] Tạo code ứng dụng Flask
- [x] Sửa thông tin sinh viên trong application.py
- [x] Test local (optional)
- [x] Tạo file ZIP đúng cách

### Bước 5.2: AWS Console - IAM
- [x] Chụp ảnh 0001.png: IAM Console
- [x] Chụp ảnh 0002.png: IAM Policies

### Bước 5.3: AWS Console - EC2 Key Pair
- [x] Chụp ảnh 0003.png: Create Key Pair form
- [x] Download private key (.pem hoặc .ppk)

### Bước 5.4: AWS Console - Elastic Beanstalk
1. Truy cập EB Console
2. Click "Create Application"
3. Làm theo từng bước trong workshop
4. Chụp ảnh 0001-0031 theo danh sách trên
5. Đợi environment deploy xong (~10 phút)

### Bước 5.5: Verify và chụp ảnh app
1. Mở URL của EB environment
2. Chụp 0032.png: Trang chủ
3. Click "Giới thiệu", chụp 0033.png
4. Vào /api/info, chụp 0034.png
5. Vào /health, chụp 0035.png
6. Trong EB Console > Logs, chụp 0036.png

### Bước 5.6: Monitor và chụp ảnh
1. EC2 Console, chụp 0001.png
2. EB > Health, chụp 0002.png
3. EB > Monitoring, chụp 0003.png
4. EB > Events, chụp 0004.png

---

## 📊 TỔNG KẾT

### Đã có:
- ✅ Code ứng dụng hoàn chỉnh (application.py + requirements.txt)
- ✅ 34 ảnh trong folder 2.prerequisite và 3.deployapp

### Cần bổ sung:
- ❌ **5 ảnh** cho phần Verify App (0032-0036 trong 3.deployapp)
- ❌ **4 ảnh** cho phần Monitor (0001-0004 trong 4.monitor)

**TỔNG CỘNG: Cần chụp thêm 9 ảnh**

---

## 🚀 CHECKLIST CUỐI CÙNG

### Trước khi deploy:
- [ ] Đã sửa thông tin sinh viên trong application.py
- [ ] Đã tạo file ZIP đúng cách (files ở root level)
- [ ] File ZIP có tên: my-flask-app.zip

### Trong quá trình deploy:
- [ ] Chụp đủ 31 ảnh cho các bước tạo EB
- [ ] Đợi environment status = "Ok" (màu xanh)

### Sau khi deploy thành công:
- [ ] Chụp 5 ảnh verify app (trang chủ, about, API endpoints, logs)
- [ ] Chụp 4 ảnh monitoring (EC2, Health, Metrics, Events)
- [ ] Copy tất cả ảnh vào đúng folder
- [ ] Chạy hugo server để kiểm tra

### Hoàn thành:
- [ ] Hugo build thành công
- [ ] Tất cả links và ảnh hiển thị đúng
- [ ] Cả tiếng Anh và tiếng Việt đều hoàn chỉnh

---

🎉 **SAU KHI HOÀN THÀNH TẤT CẢ, DỰ ÁN CỦA BẠN SẼ HOÀN HẢO 100%!**
