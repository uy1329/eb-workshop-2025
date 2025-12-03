---
title : "Prepare Application"
date : "2025-12-02"
weight : 2
chapter : false
pre : " <b> 2.2 </b> "
---

#### Prepare Your Application for Deployment

Before deploying to Elastic Beanstalk, you need to prepare your application code and package it correctly.

#### Option 1: Use Sample Application

For this workshop, you can use a simple Python Flask application that we'll create.

**Create a simple Flask app:**

1. **Create a new folder** on your computer: `my-flask-app`

2. **Create `application.py`** file with the following content:

```python
from flask import Flask, jsonify

# Elastic Beanstalk looks for 'application' variable
application = Flask(__name__)

# Student Information - CHANGE HERE
STUDENT_INFO = {
    "name": "Your Name",
    "student_id": "555555",
    "class": "Your Class",
    "university": "Your University"
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
                <p>Deployment Successful!</p>
                <div class="badge">✅ Application Running on AWS</div>
                <div class="info">
                    <p><strong>Student:</strong> {STUDENT_INFO['name']}</p>
                    <p><strong>ID:</strong> {STUDENT_INFO['student_id']}</p>
                    <p><strong>Class:</strong> {STUDENT_INFO['class']}</p>
                    <p><strong>University:</strong> {STUDENT_INFO['university']}</p>
                </div>
            </div>
        </body>
    </html>
    '''

@application.route('/health')
def health():
    return jsonify({'status': 'healthy', 'message': 'Application is running!'})

@application.route('/api/info')
def api_info():
    return jsonify(STUDENT_INFO)

# For local testing
if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000, debug=True)
```

3. **Create `requirements.txt`** file:

```txt
Flask==3.0.0
Werkzeug==3.0.1
```

#### Test Locally (Optional)

If you want to test before deploying:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python application.py
```

Then open browser at `http://localhost:8000`

{{% notice note %}}
Testing locally is **optional**. You can skip directly to packaging.
{{% /notice %}}

#### Package Application for Deployment

Elastic Beanstalk requires your application to be packaged as a **ZIP file**.

**Important Rules:**
- ✅ Compress the **FILES** (application.py, requirements.txt)
- ❌ Do NOT compress the **FOLDER** itself

**For Windows:**

1. Open the `my-flask-app` folder
2. Select **ALL files** inside (Ctrl + A):
   - `application.py`
   - `requirements.txt`
3. Right-click → **Send to** → **Compressed (zipped) folder**
4. Rename the ZIP file to: `my-flask-app.zip`

**For Mac/Linux:**

```bash
cd my-flask-app
zip -r ../my-flask-app.zip *
```

#### Verify ZIP Structure

Open your ZIP file and verify it looks like this:

```
my-flask-app.zip
├── application.py
└── requirements.txt
```

{{% notice warning %}}
**Common Mistake:** If you see `my-flask-app/application.py` (with folder inside), you compressed the wrong way. Start over and select only the **files**, not the folder.
{{% /notice %}}

#### Why "application.py"?

Elastic Beanstalk for Python looks for a file named **`application.py`** with a variable named **`application`**. This naming convention is mandatory!

```python
# Must be named 'application'
application = Flask(__name__)
```

#### What's Next?

Now you have:
- ✅ EC2 key pair created
- ✅ Application code packaged as ZIP

You're ready to deploy to Elastic Beanstalk in Section 3!

{{% notice tip %}}
Keep your ZIP file ready - you'll upload it when creating the Elastic Beanstalk environment.
{{% /notice %}}
