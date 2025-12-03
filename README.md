# AWS Elastic Beanstalk Workshop

Deploy your Python Flask application to AWS Elastic Beanstalk - A comprehensive hands-on workshop.

## 🚀 Overview

This workshop guides you through deploying a web application on AWS Elastic Beanstalk using a Single Instance architecture (free tier eligible).

**Topics Covered:**
- AWS Elastic Beanstalk fundamentals
- EC2 Key Pair creation
- Flask application preparation and packaging
- Environment configuration
- Application deployment
- Monitoring with CloudWatch
- Resource cleanup

## 🌐 View Workshop

**Live Site:** [Your GitHub Pages URL will be here]

## 🏗️ Architecture

Workshop uses **Single Instance mode** for cost-effective learning:
- VPC with Public Subnet
- EC2 Instance (t3.micro)
- Internet Gateway for public access
- Elastic Beanstalk for management
- S3 for application versions

## 📚 Local Development

### Prerequisites
- Hugo Extended v0.152.2+
- Git

### Run Locally

```bash
# Clone repository
git clone [your-repo-url]
cd 000058-SessionManager

# Start Hugo server
hugo server -D

# Access at http://localhost:1313
```

## 📖 Workshop Sections

1. **Introduction** - AWS Elastic Beanstalk overview and architecture
2. **Prerequisites** - EC2 Key Pair and application preparation
3. **Deploy Application** - Create environment and deploy Flask app
4. **Monitor** - Application health monitoring
5. **Cleanup** - Resource deletion

## 👤 Author

**Võ Văn Uy**
- LinkedIn: [linkedin.com/in/uy-võ-văn-7881b4334](https://www.linkedin.com/in/uy-v%C3%B5-v%C4%83n-7881b4334)
- Workshop Date: December 2025

## 📝 License

This workshop is created for educational purposes.

## 🙏 Acknowledgments

- AWS Study Group FCJ
- Hugo Learn Theme
