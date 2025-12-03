---
title : "Chuẩn bị ứng dụng"
date : "2025-12-02"
weight : 2
chapter : false
pre : " <b> 2.2 </b> "
---

#### Chuẩn bị ứng dụng để triển khai

Trước khi triển khai lên Elastic Beanstalk, bạn cần chuẩn bị code ứng dụng và đóng gói đúng cách.

#### Lựa chọn 1: Sử dụng ứng dụng mẫu

Cho workshop này, bạn có thể sử dụng một ứng dụng Python Flask đơn giản mà chúng ta sẽ tạo.

**Tạo Flask app đơn giản:**

1. **Tạo folder mới** trên máy tính: `my-flask-app`

2. **Tạo file `application.py`** với nội dung sau:

```python
from flask import Flask, jsonify

# Elastic Beanstalk tìm biến 'application'
application = Flask(__name__)

# Thông tin sinh viên - THAY ĐỔI Ở ĐÂY
STUDENT_INFO = {
    "name": "Tên của bạn",
    "student_id": "555555",
    "class": "Lớp của bạn",
    "university": "Tên trường của bạn"
}

@application.route('/')
def home():
    return f'''
    <html>
        <head>
            <title>AWS Elastic Beanstalk Demo</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                    margin: 0;
                }}
                .container {{
                    text-align: center;
                    background: rgba(255,255,255,0.1);
                    padding: 40px;
                    border-radius: 10px;
                    backdrop-filter: blur(10px);
                    max-width: 600px;
                }}
                h1 {{ font-size: 3em; margin: 0; }}
                p {{ font-size: 1.2em; }}
                .badge {{
                    background: #4CAF50;
                    padding: 10px 20px;
                    border-radius: 20px;
                    margin-top: 20px;
                    display: inline-block;
                }}
                .info {{ 
                    background: rgba(255,255,255,0.2);
                    padding: 20px;
                    border-radius: 10px;
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 AWS Elastic Beanstalk</h1>
                <p>Triển khai thành công!</p>
                <div class="badge">✅ Ứng dụng đang chạy trên AWS</div>
                <div class="info">
                    <p><strong>Sinh viên:</strong> {STUDENT_INFO['name']}</p>
                    <p><strong>MSSV:</strong> {STUDENT_INFO['student_id']}</p>
                    <p><strong>Lớp:</strong> {STUDENT_INFO['class']}</p>
                    <p><strong>Trường:</strong> {STUDENT_INFO['university']}</p>
                </div>
            </div>
        </body>
    </html>
    '''

@application.route('/health')
def health():
    return jsonify({'status': 'healthy', 'message': 'Ứng dụng đang chạy!'})

@application.route('/api/info')
def api_info():
    return jsonify(STUDENT_INFO)

# Để test local
if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000, debug=True)
```

3. **Tạo file `requirements.txt`**:

```txt
Flask==3.0.0
Werkzeug==3.0.1
```

#### Test Local (Tùy chọn)

Nếu muốn test trước khi deploy:

```bash
# Cài dependencies
pip install -r requirements.txt

# Chạy ứng dụng
python application.py
```

Sau đó mở trình duyệt tại `http://localhost:8000`

{{% notice note %}}
Test local là **tùy chọn**. Bạn có thể bỏ qua và đóng gói trực tiếp.
{{% /notice %}}

#### Đóng gói ứng dụng để triển khai

Elastic Beanstalk yêu cầu ứng dụng được đóng gói dưới dạng file **ZIP**.

**Quy tắc quan trọng:**
- ✅ Nén các **FILE** (application.py, requirements.txt)
- ❌ KHÔNG nén **FOLDER** chứa các file

**Với Windows:**

1. Mở folder `my-flask-app`
2. Chọn **TẤT CẢ files** bên trong (Ctrl + A):
   - `application.py`
   - `requirements.txt`
3. Click chuột phải → **Send to** → **Compressed (zipped) folder**
4. Đổi tên file ZIP thành: `my-flask-app.zip`

**Với Mac/Linux:**

```bash
cd my-flask-app
zip -r ../my-flask-app.zip *
```

#### Xác minh cấu trúc ZIP

Mở file ZIP của bạn và xác minh nó trông như thế này:

```
my-flask-app.zip
├── application.py
└── requirements.txt
```

{{% notice warning %}}
**Lỗi thường gặp:** Nếu bạn thấy `my-flask-app/application.py` (có folder bên trong), bạn đã nén sai cách. Bắt đầu lại và chỉ chọn các **files**, không phải folder.
{{% /notice %}}

#### Tại sao phải là "application.py"?

Elastic Beanstalk cho Python tìm file tên **`application.py`** với biến tên **`application`**. Quy ước đặt tên này là bắt buộc!

```python
# Phải đặt tên là 'application'
application = Flask(__name__)
```

#### Bước tiếp theo

Bây giờ bạn đã có:
- ✅ EC2 key pair đã tạo
- ✅ Code ứng dụng đã đóng gói thành ZIP

Bạn đã sẵn sàng để triển khai lên Elastic Beanstalk trong Phần 3!

{{% notice tip %}}
Giữ file ZIP sẵn sàng - bạn sẽ upload nó khi tạo môi trường Elastic Beanstalk.
{{% /notice %}}
