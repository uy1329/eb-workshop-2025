---
title : "Create EB"
date : "2025-11-30"
weight : 1
chapter : false
pre : " <b> 3.1 </b> "
---

#### Create Elastic Beanstalk Environment with Sample Application

In this section, we will create an Elastic Beanstalk environment and deploy a sample application for testing.

### Step 1: Access Elastic Beanstalk Console

1. Log in to AWS Management Console
2. Search for **Elastic Beanstalk** in the search bar
3. Click **Create application**

![Create Application](/eb-workshop-2025/images/3.deployapp/0001.png)

### Step 2: Configure Environment

1. **Environment tier**: Select **Web server environment**
2. **Application name**: Enter application name, example: `elastic-beanstalk-demo`
3. **Environment name**: Auto-generated or customize, example: `Elastic-beanstalk-demo-env`

![Configure Environment](/eb-workshop-2025/images/3.deployapp/0002.png)

4. **Platform**: Select **Python**
5. **Platform branch**: Select **Python 3.14 running on 64bit Amazon Linux 2023**
6. **Platform version**: Leave as default (recommended version)
7. **Application code**: Select **Sample application**
   - We will deploy AWS sample application for testing
   - Later we'll deploy custom Flask app in Section 3.2

![Platform Selection](/eb-workshop-2025/images/3.deployapp/0003.png)

8. **Presets**: Select **Single instance (free tier eligible)**
   - Suitable for test/learning environment
   - No Load Balancer, helps save costs
   - EC2 Instance will have Public IP for direct access

{{% notice warning %}}**This workshop uses Single Instance mode** (without Load Balancer). If you want a production environment with Load Balancer, see the "Upgrade to Load Balanced Mode" section below.{{% /notice %}}

![Presets](/eb-workshop-2025/images/3.deployapp/0004.png)

#### 💡 Upgrade to Load Balanced Mode (Optional)

If you want to deploy a production environment with Load Balancer:

**Step 2 - Changes:**
- **Presets**: Select **High availability (with Load Balancer)**
- Environment will create:
  - Application Load Balancer (ALB)
  - Auto Scaling Group (min: 1, max: 4 instances)
  - Multi-AZ deployment
  - Health checks via Load Balancer

**Time & Cost:**
- Creation time: 8-12 minutes (instead of 5-10 minutes)
- Additional cost: ~$16-18/month for ALB
- EC2 instances: Charged by number of running instances

**Benefits:**
- High Availability: Application continues running if 1 instance fails
- Auto Scaling: Automatically expands when traffic increases
- Zero-downtime deployment: Deploy without service interruption
- Better security: EC2 instances in private subnet

{{% notice tip %}}If you choose Load Balanced mode, skip the "Public IP" warning in Step 4 as the Load Balancer will handle public access.{{% /notice %}}

---

9. Click **Next** to configure service access

### Step 3: Configure Service Access

**Service Role**

If you don't have a Service role yet:

![Service Access Empty](/eb-workshop-2025/images/3.deployapp/0005.png)

1. Select **Create and use new service role**

![Create Service Role](/eb-workshop-2025/images/3.deployapp/0006.png)

2. AWS automatically creates role named `aws-elasticbeanstalk-service-role`

![Service Role Creating](/eb-workshop-2025/images/3.deployapp/0007.png)

3. Role will have these policies:
   - `AWSElasticBeanstalkEnhancedHealth`
   - `AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy`

![Service Role Policies](/eb-workshop-2025/images/3.deployapp/0008.png)

4. After creation, select the newly created role in dropdown

![Service Role Selected](/eb-workshop-2025/images/3.deployapp/0009.png)

**EC2 Instance Profile**

If you don't have an EC2 instance profile yet:

1. Select **Create and use new EC2 instance profile**

![Create Instance Profile](/eb-workshop-2025/images/3.deployapp/0010.png)

2. AWS automatically creates instance profile named `aws-elasticbeanstalk-ec2-role`

![Instance Profile Creating](/eb-workshop-2025/images/3.deployapp/0011.png)

3. Instance profile will have these policies:
   - `AWSElasticBeanstalkWebTier`
   - `AWSElasticBeanstalkWorkerTier`
   - `AWSElasticBeanstalkMulticontainerDocker`

![Instance Profile Policies](/eb-workshop-2025/images/3.deployapp/0012.png)

4. After creation, select the instance profile in dropdown

![Instance Profile Selected](/eb-workshop-2025/images/3.deployapp/0013.png)

**EC2 Key Pair**

1. **EC2 key pair**: Select `elastic-beanstalk-keypair`
   - This key pair was created in Section 2.1
   - Used for SSH access to EC2 instance if troubleshooting needed

![Key Pair Selected](/eb-workshop-2025/images/3.deployapp/0014.png)

2. Click **Next** to configure networking

### Step 4: Configure Networking, Database and Tags

**VPC and Networking**

1. **VPC**: Select default VPC
   - Example: `vpc-067152750ba5e4cf4 (172.31.0.0/16)`

2. **Public IP address**: Select **Activated**
   - Required for single instance without load balancer

3. **Instance subnets**: Select one availability zone
   - Example: `ap-southeast-2a` with subnet `172.31.0.0/20`

![Networking Configuration](/eb-workshop-2025/images/3.deployapp/0015.png)

**Database and Tags**

1. **Database**: Don't select (leave empty)
   - This workshop doesn't use RDS

2. **Tags**: Leave empty (optional)

![Database and Tags](/eb-workshop-2025/images/3.deployapp/0016.png)

3. Click **Next** to configure instance

### Step 5: Configure Instance Traffic and Scaling

**Instance Configuration**

1. **Root volume**: Leave as default
2. **EC2 security groups**: Leave as default
3. **CloudWatch monitoring**: 5 minute (basic monitoring)
4. **IMDSv1**: **Disabled** (recommended)
5. **IMDSv2**: Enabled

![Instance Configuration](/eb-workshop-2025/images/3.deployapp/0017.png)

**Capacity**

1. **Environment type**: Single instance
2. **Fleet composition**: On-Demand instances
3. **Architecture**: x86_64

![Capacity](/eb-workshop-2025/images/3.deployapp/0018.png)

4. **Instance types**: Select only `t3.micro`
   - Remove `t3.small` if present (not free tier eligible)

{{% notice warning %}}
**Only use t3.micro** to avoid charges! Instance `t3.small` costs ~$15/month.
{{% /notice %}}

5. **AMI ID**: Leave as default (Amazon Linux 2023 for Python)

![Instance Types](/eb-workshop-2025/images/3.deployapp/0019.png)

6. Click **Next** to configure monitoring

### Step 6: Configure Updates, Monitoring and Logging

**Monitoring**

1. **Health reporting**: Enhanced
2. **CloudWatch Logs**: Disabled (to save costs)

![Monitoring](/eb-workshop-2025/images/3.deployapp/0020.png)

**Managed Platform Updates**

1. **Managed updates**: Enabled
2. **Update window**: Tuesday, 19:45 UTC, 1 hour
3. **Update level**: Minor and patch

![Managed Updates](/eb-workshop-2025/images/3.deployapp/0021.png)

**Rolling Updates and Deployments**

1. **Deployment policy**: All at once
   - Deploy all instances simultaneously
   - Brief downtime

![Rolling Updates](/eb-workshop-2025/images/3.deployapp/0022.png)

**Platform Software**

1. **Proxy server**: Nginx
2. **WSGI Path**: application
3. **Logs retention**: 7 days
4. **NumThreads**: 15

![Platform Software](/eb-workshop-2025/images/3.deployapp/0023.png)

5. Click **Next** to review

### Step 7: Submit and Wait

1. Click **Submit** to create environment
2. Creation process takes **5-10 minutes**

AWS Elastic Beanstalk will:
- Launch EC2 instance
- Configure security groups
- Deploy sample application
- Perform health checks

### Step 8: Verify Environment

When environment creation is complete:

1. **Health status**: Ok (green)
2. **Domain URL**: Public URL displayed

![Environment Created](/eb-workshop-2025/images/3.deployapp/0030.png)

3. Click on **Domain** to access the application

You will see the AWS Elastic Beanstalk sample application welcome page.

![Sample App Running](/eb-workshop-2025/images/3.deployapp/0031.png)

{{% notice success %}}
**Congratulations!** Elastic Beanstalk environment is ready. Now we can deploy custom Flask application in Section 3.2.
{{% /notice %}}

{{% notice info %}}
Environment URL format: `<env-name>.<random>.<region>.elasticbeanstalk.com`
{{% /notice %}}
