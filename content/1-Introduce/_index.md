---
title : "Introduction"
date: "2025-12-02" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---

#### What is AWS Elastic Beanstalk?

**AWS Elastic Beanstalk** is a Platform as a Service (PaaS) that makes it easy to deploy, manage, and scale web applications and services. You simply upload your code, and Elastic Beanstalk automatically handles the deployment details including:

- Capacity provisioning
- Load balancing
- Auto-scaling
- Application health monitoring

#### Key Benefits

**1. Easy to Use**
- Upload your application code and Elastic Beanstalk does the rest
- No need to worry about infrastructure management
- Focus on writing code, not managing servers

**2. Fast Deployment**
- Deploy applications in minutes
- Automatic environment setup
- Built-in support for multiple platforms (Node.js, Python, Java, .NET, PHP, Ruby, Go, Docker)

**3. Cost Effective**
- No additional charge for Elastic Beanstalk itself
- Pay only for the AWS resources (EC2, S3, RDS, etc.) your application uses
- Automatic scaling saves costs by adjusting resources based on demand

**4. Full Control**
- Complete access to underlying AWS resources
- Can customize any aspect of the infrastructure
- Choose instance types, database, scaling rules, etc.

**5. Monitoring and Management**
- Built-in CloudWatch monitoring
- Health dashboard shows application status
- Automatic log collection and storage

#### How It Works

1. **Choose a platform**: Select your programming language/framework (e.g., Node.js, Python, PHP)
2. **Upload your code**: Deploy via console, CLI, or Git
3. **Elastic Beanstalk provisions resources**: Automatically creates EC2 instances, load balancers, auto-scaling groups
4. **Monitor and manage**: Use the dashboard to check health, view logs, and make updates

#### Elastic Beanstalk Components

- **Application**: Logical container for your project
- **Environment**: Collection of AWS resources running your application version
- **Platform**: Operating system, programming language, runtime, and web server
- **Application Version**: Specific iteration of your deployable code

#### Workshop Architecture

{{% notice info %}}**Important**: This workshop uses **Single Instance mode** (without Load Balancer) to:
- Save costs (free within Free Tier)
- Simplify the learning process
- Suitable for development/testing environments
{{% /notice %}}

**Architecture Diagram:**

![AWS Elastic Beanstalk Architecture](/eb-workshop-2025/images/1.introduce/architecture.png)

**Component Explanation:**

1. **Developer**: The developer who uploads code to Elastic Beanstalk
2. **Internet Gateway**: Gateway connecting Internet and VPC
3. **VPC (Virtual Private Cloud)**: Private virtual network on AWS
4. **Public Subnet**: Subnet with Internet connectivity, containing EC2 Instance
5. **EC2 Instance**: 
   - Server running Python Flask application
   - Has Public IP for direct Internet access
   - Instance type: t3.micro (Free Tier)
6. **Elastic Beanstalk**: 
   - Manages and monitors EC2 Instance
   - Automatically deploys code and configures environment
   - Performs health checks
7. **S3 Bucket**: 
   - Stores code versions (application versions)
   - Stores logs and artifacts

**Workflow:**
1. Developer uploads code to Elastic Beanstalk
2. EB saves code version to S3 Bucket
3. EB deploys code to EC2 Instance in Public Subnet
4. Users access application via Internet Gateway → EC2 Instance (Public IP)

---

**Upgrade to Load Balanced Mode** (Optional - Production):

For production environment with high availability:
- **Load Balancer**: Distributes traffic to multiple EC2 instances
- **Auto Scaling Group**: Automatically scales instances (min: 1, max: 4)
- **Multi-AZ Deployment**: Instances in multiple Availability Zones
- **Additional cost**: ~$16-18/month for Application Load Balancer

See detailed guide in Section 3.1 (Step 2).

#### When to Use Elastic Beanstalk

✅ **Good for:**
- Web applications and APIs
- Microservices
- Applications that need quick deployment
- Development and testing environments
- Teams wanting to focus on code rather than infrastructure

❌ **Consider alternatives for:**
- Complex multi-tier architectures (use CloudFormation or Terraform)
- Applications requiring very specific custom configurations
- Serverless applications (use Lambda instead)

#### Elastic Beanstalk vs Traditional Deployment

| Traditional Deployment | Elastic Beanstalk |
|------------------------|-------------------|
| Manual server setup | Automatic provisioning |
| Manual scaling configuration | Built-in auto-scaling |
| Manual monitoring setup | Integrated monitoring |
| Complex deployment process | Simple code upload |
| Hours to deploy | Minutes to deploy |

In this workshop, you will learn hands-on how to deploy a web application using AWS Elastic Beanstalk!
