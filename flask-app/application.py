from flask import Flask, render_template_string, jsonify
import os

application = Flask(__name__)

# Thông tin sinh viên - BẠN CẦN SỬA LẠI THÔNG TIN CỦA MÌNH
STUDENT_INFO = {
    "name": "Nguyễn Văn A",
    "student_id": "555555",
    "class": "CNTT-K65",
    "university": "Đại học XYZ"
}

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
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
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            padding: 40px;
            max-width: 600px;
            width: 100%;
            animation: fadeIn 0.5s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        h1 {
            color: #667eea;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
        }
        .info {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-radius: 15px;
            padding: 25px;
            margin: 20px 0;
        }
        .info-item {
            display: flex;
            justify-content: space-between;
            padding: 12px 0;
            border-bottom: 1px solid rgba(102, 126, 234, 0.2);
        }
        .info-item:last-child {
            border-bottom: none;
        }
        .label {
            font-weight: bold;
            color: #667eea;
        }
        .value {
            color: #333;
            text-align: right;
        }
        .nav-links {
            display: flex;
            gap: 10px;
            margin-top: 30px;
            flex-wrap: wrap;
        }
        .nav-links a {
            flex: 1;
            min-width: 120px;
            text-align: center;
            padding: 12px 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .nav-links a:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        .badge {
            display: inline-block;
            background: #4CAF50;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            margin-top: 20px;
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
        <h1>{{ title }}</h1>
        {{ content | safe }}
    </div>
</body>
</html>
"""

@application.route('/')
def home():
    content = f"""
        <div class="info">
            <div class="info-item">
                <span class="label">Họ và tên:</span>
                <span class="value">{STUDENT_INFO['name']}</span>
            </div>
            <div class="info-item">
                <span class="label">MSSV:</span>
                <span class="value">{STUDENT_INFO['student_id']}</span>
            </div>
            <div class="info-item">
                <span class="label">Lớp:</span>
                <span class="value">{STUDENT_INFO['class']}</span>
            </div>
            <div class="info-item">
                <span class="label">Trường:</span>
                <span class="value">{STUDENT_INFO['university']}</span>
            </div>
        </div>
        <div style="text-align: center;">
            <span class="badge">✓ Deployed on AWS Elastic Beanstalk</span>
        </div>
        <div class="nav-links">
            <a href="/about">About</a>
            <a href="/api/info">API Info</a>
            <a href="/health">Health</a>
        </div>
    """
    return render_template_string(HTML_TEMPLATE, title="Thông tin sinh viên", content=content)

@application.route('/about')
def about():
    content = """
        <div class="info">
            <h2 style="color: #667eea; margin-bottom: 20px;">Về ứng dụng này</h2>
            <p style="line-height: 1.8; color: #555;">
                Đây là ứng dụng web đơn giản được phát triển bằng Flask và triển khai trên 
                AWS Elastic Beanstalk. Ứng dụng này được tạo ra như một phần của bài tập 
                thực hành về Cloud Computing và AWS Services.
            </p>
            <h3 style="color: #667eea; margin: 20px 0 10px 0;">Công nghệ sử dụng:</h3>
            <ul style="list-style: none; padding: 0;">
                <li style="padding: 8px 0; color: #555;">🐍 Python 3.x</li>
                <li style="padding: 8px 0; color: #555;">🌶️ Flask Framework</li>
                <li style="padding: 8px 0; color: #555;">☁️ AWS Elastic Beanstalk</li>
                <li style="padding: 8px 0; color: #555;">🖥️ Amazon EC2</li>
            </ul>
        </div>
        <div class="nav-links">
            <a href="/">← Về trang chủ</a>
        </div>
        <div class="footer">
            <p>© 2025 - AWS Elastic Beanstalk Workshop</p>
        </div>
    """
    return render_template_string(HTML_TEMPLATE, title="About", content=content)

@application.route('/api/info')
def api_info():
    """API endpoint trả về thông tin sinh viên dạng JSON"""
    return jsonify({
        "status": "success",
        "data": STUDENT_INFO,
        "message": "Thông tin sinh viên được lấy thành công"
    })

@application.route('/health')
def health():
    """Health check endpoint cho Elastic Beanstalk"""
    return jsonify({
        "status": "healthy",
        "service": "Flask Application",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    # Elastic Beanstalk sẽ set PORT environment variable
    port = int(os.environ.get('PORT', 5000))
    application.run(host='0.0.0.0', port=port, debug=False)
