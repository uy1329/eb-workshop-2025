---
title : "Create EC2 Key Pair"
date : "2025-12-02"
weight : 1
chapter : false
pre : " <b> 2.1 </b> "
---

#### Create EC2 Key Pair

An EC2 Key Pair is used to securely connect to EC2 instances via SSH. Although this is optional for Elastic Beanstalk, creating a key pair allows you to troubleshoot and manage your instances directly if needed.

#### Steps to Create Key Pair

1. **Navigate to EC2 Console**
   - In the AWS Management Console, search for **EC2**
   - Click on **EC2** service
   - You can use any region (we recommend **Sydney - ap-southeast-2**)

2. **Access Key Pairs**
   - In the left sidebar under **Network & Security**, click **Key Pairs**
   - Click the **Create key pair** button (orange button at top right)

3. **Configure the Key Pair**

![Create Key Pair]({{< relref "/" >}}images/2.prerequisite/0003.png)

Fill in the following information:

- **Name**: `elastic-beanstalk-keypair`
  - Use this exact name or remember your custom name
- **Key pair type**: **RSA**
  - RSA is the most widely supported encryption type
- **Private key file format**: 
  - **.pem** (for Mac/Linux/Windows 10+)
  - **.ppk** (for PuTTY on older Windows)

4. **Create and Download**
   - Click **Create key pair** button
   - The private key file (`.pem` or `.ppk`) will automatically download to your computer
   - **Important**: Save this file in a secure location. You cannot download it again!

{{% notice warning %}}
**Keep your private key safe!** If you lose this file, you won't be able to connect to your EC2 instance via SSH. Store it in a secure location and never share it publicly.
{{% /notice %}}

{{% notice tip %}}
For Windows users: If you downloaded a .pem file, you may need to convert it to .ppk format using PuTTYgen if you want to use PuTTY for SSH connections.
{{% /notice %}}

#### Verify Key Pair Created

After creation, you should see your key pair listed in the Key Pairs console:

- **Name**: elastic-beanstalk-keypair
- **Fingerprint**: A unique identifier
- **Type**: RSA
- **Created**: Today's date

#### Next Steps

Your EC2 key pair is now ready to use! You'll select this key pair when creating your Elastic Beanstalk environment in Section 3.

In the next step, we'll prepare the application code for deployment.
