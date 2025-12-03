---
title : "Clean Up Resources"
date : "2025-12-01"
weight : 5
chapter : false
pre : " <b> 5. </b> "
---

#### Clean Up Resources

{{% notice warning %}}
**Important**: Remember to delete all resources after completing the workshop to avoid unwanted AWS charges.
{{% /notice %}}

After completing this workshop, you should delete all AWS resources created to avoid incurring ongoing costs. Even though we used free tier eligible resources, it's a best practice to clean up when you're done.

### Resources to Delete

In this workshop, we created the following resources:

1. **Elastic Beanstalk Environment** - `Elastic-beanstalk-demo-env`
2. **Elastic Beanstalk Application** - `elastic-beanstalk-demo`
3. **EC2 Instance** - Created by Elastic Beanstalk
4. **Security Groups** - Created by Elastic Beanstalk
5. **IAM Roles** - Service role and EC2 instance profile
6. **EC2 Key Pair** - `elastic-beanstalk-keypair`

### Step 1: Terminate Elastic Beanstalk Environment

The environment must be terminated before the application can be deleted.

1. Navigate to the [AWS Elastic Beanstalk Console](https://console.aws.amazon.com/elasticbeanstalk)
2. Select your environment: `Elastic-beanstalk-demo-env`
3. Click **Actions** dropdown menu
4. Select **Terminate environment**
5. In the confirmation dialog:
   - Type the environment name: `Elastic-beanstalk-demo-env`
   - Click **Terminate**

The termination process will:
- Stop the EC2 instance
- Delete the security groups
- Remove environment-specific configurations
- Takes approximately 5 minutes

{{% notice info %}}
**Note**: You can monitor the termination progress in the Events tab.
{{% /notice %}}

### Step 2: Delete Elastic Beanstalk Application

After the environment is completely terminated:

1. In the Elastic Beanstalk Console, go to **Applications**
2. Select `elastic-beanstalk-demo`
3. Click **Actions** dropdown menu
4. Select **Delete application**
5. Confirm deletion by typing the application name
6. Click **Delete**

### Step 3: Delete EC2 Key Pair (Optional)

If you no longer need the key pair:

1. Navigate to **EC2 Console**
2. In the left menu, select **Key Pairs** under **Network & Security**
3. Select `elastic-beanstalk-keypair`
4. Click **Actions** → **Delete**
5. Confirm deletion

{{% notice warning %}}
**Warning**: Once deleted, you cannot recover the private key. Make sure you have a backup if you need it.
{{% /notice %}}

### Step 4: Delete IAM Roles (Optional)

If you created IAM roles specifically for this workshop and don't need them:

1. Navigate to **IAM Console**
2. Click **Roles** in the left menu
3. Delete the following roles:
   - `aws-elasticbeanstalk-service-role`
   - `aws-elasticbeanstalk-ec2-role`

**For each role:**
1. Select the role
2. Click **Delete**
3. Confirm deletion

{{% notice info %}}
**Note**: If you plan to create more Elastic Beanstalk environments in the future, you can keep these IAM roles to reuse them.
{{% /notice %}}

### Step 5: Verify Complete Cleanup

Verify that all resources have been deleted:

1. **EC2 Dashboard**:
   - Check that no instances related to Elastic Beanstalk are running
   - Verify security groups are deleted (may take a few minutes)

2. **Elastic Beanstalk Console**:
   - Verify no environments or applications are listed

3. **CloudWatch Logs** (if enabled):
   - Check for log groups created by Elastic Beanstalk
   - Delete them if no longer needed

4. **S3 Buckets**:
   - Check for S3 buckets created by Elastic Beanstalk
   - Format: `elasticbeanstalk-<region>-<account-id>`
   - Empty and delete if no longer needed

### Cleanup Completion Time

The complete cleanup process typically takes:
- **Environment termination**: 5-7 minutes
- **Application deletion**: 1 minute
- **Other resources**: 1-2 minutes

### Cost Considerations

- **Elastic Beanstalk**: No charge for the service itself
- **EC2 Instances**: Charges stop when instances are terminated
- **S3 Storage**: Small charges if buckets contain data
- **CloudWatch Logs**: Charges for stored logs

{{% notice tip %}}
**Best Practice**: Always clean up resources after completing a workshop or when they are no longer needed. Set up AWS Budgets to receive alerts if your costs exceed expected amounts.
{{% /notice %}}

**Congratulations!** You have successfully completed the AWS Elastic Beanstalk workshop and cleaned up all resources.

