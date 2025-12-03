---
title : "Check EC2 in Elastic Beanstalk"
date : "2025-11-30"
weight : 1
chapter : false
pre : " <b> 4.1 </b> "
---

#### Check EC2 Instances Created by Elastic Beanstalk

Elastic Beanstalk automatically creates and manages EC2 instances for your application. Let's examine these instances.

### View EC2 Instances

1. **From Elastic Beanstalk Console:**
   - Go to your environment
   - Click **Configuration** in the left menu
   - Under **Instances**, click **Edit**
   - You'll see instance type and scaling settings

2. **From EC2 Console:**
   - Navigate to **EC2 Console**
   - Click **Instances** in the left menu
   - Look for instances with names containing your environment name
   - Tags will include: `elasticbeanstalk:environment-name`

### Instance Details

Check the following information:

- **Instance Type**: Default is `t2.micro` (free tier)
- **Instance State**: Should be **Running**
- **Security Groups**: Elastic Beanstalk creates security groups automatically
- **IAM Role**: Should have `aws-elasticbeanstalk-ec2-role`
- **Tags**: Include application and environment information

### Security Groups

Elastic Beanstalk creates security groups for:

1. **EC2 Instance Security Group**
   - Allows HTTP (port 80) from load balancer or internet
   - Allows HTTPS (port 443) if configured
   - Allows SSH (port 22) if key pair configured

2. **Load Balancer Security Group** (if high availability)
   - Allows HTTP/HTTPS from internet
   - Forwards to EC2 instances

### Monitor Instance Health

1. **In Elastic Beanstalk Console:**
   - Go to your environment
   - View **Health** tab
   - Check instance status (green = healthy)

2. **In CloudWatch:**
   - View CPU utilization
   - View network in/out
   - View disk operations

### Connect to Instance (Optional)

If you configured an EC2 key pair during setup:

1. Go to **EC2 Console**
2. Select your instance
3. Click **Connect**
4. Choose connection method:
   - **EC2 Instance Connect** (browser-based)
   - **SSH client** (using your key pair)

### View Application Logs

Logs are stored on the instance:
- Location: `/var/log/`
- Application logs: `/var/log/web.stdout.log`
- Error logs: `/var/log/web.stderr.log`
- Elastic Beanstalk logs: `/var/log/eb-engine.log`

{{% notice tip %}}
You can also download logs directly from Elastic Beanstalk Console → Logs → Request Logs
{{% /notice %}}

### Understand Auto Scaling

If you enabled auto scaling:
- **Minimum instances**: Minimum number always running
- **Maximum instances**: Maximum during high traffic
- **Scaling triggers**: CPU utilization, network, etc.
- Monitor scaling activity in **Events** tab

