---
title : "Preparation"
date : "2025-11-30"
weight : 2
chapter : false
pre : " <b> 2. </b> "
---

#### Overview of Prerequisites

Before deploying your application to AWS Elastic Beanstalk, you need to prepare several key components:

#### 1. EC2 Key Pair (Optional but Recommended)

**What is an EC2 Key Pair?**
- A key pair consists of a public key (stored in AWS) and a private key (you download)
- Used to securely connect to EC2 instances via SSH

**Why create a key pair?**
- Allows direct SSH access to EC2 instances for troubleshooting
- Can view logs, check configurations, and debug issues
- Useful for advanced users who want full control

{{% notice tip %}}
For this workshop, creating a key pair is optional but recommended for learning purposes.
{{% /notice %}}

#### 2. Prepare Your Application

**Application Requirements:**
- A working web application in one of the supported languages/frameworks
- Properly packaged according to Elastic Beanstalk requirements

**For this workshop:**
- We provide a ready-to-deploy Flask (Python) application
- You will customize it with your information
- Package it as a ZIP file for deployment

### Content

In this preparation section, we will:
- [2.1 - Create EC2 Key Pair](2.1-createkeypair/): Create a key pair for SSH access
- [2.2 - Prepare Application](2.2-prepareapp/): Create, customize, and package the Flask application

{{% notice info %}}
After completing these preparation steps, you'll be ready to create and deploy your Elastic Beanstalk application!
{{% /notice %}}
