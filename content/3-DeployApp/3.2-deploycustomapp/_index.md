---
title : "Deploy Custom Flask Application"
date : "2025-12-02"
weight : 2
chapter : false
pre : " <b> 3.2 </b> "
---

#### Deploy Your Custom Flask Application

After creating the Elastic Beanstalk environment with sample application in Section 3.1, now we'll deploy our custom Flask application.

{{% notice info %}}
**Prerequisites**: Make sure you have prepared your Flask application ZIP file from Section 2.2. If you haven't, please complete Section 2.2 first.
{{% /notice %}}

### Deploy Custom Application

1. **Go to Elastic Beanstalk Console**
   - Navigate to your application (created in 3.1)
   - Select your environment

![Environment Dashboard](/images/3.deployapp/0030.png)

2. **Upload and Deploy**
   - Click **Upload and deploy** button
   - Click **Choose file**
   - Select your `flask-app.zip` file
   - **Version label**: Enter `v1.0` (or your preferred version name)
   - Click **Deploy**

![Application Home Page](/images/3.deployapp/0032.png)

3. **Monitor Deployment**
   - Watch the **Events** section
   - Deployment typically takes 2-5 minutes
   - Wait for health status to return to **Ok** (green)

![About Page](/images/3.deployapp/0033.png)

{{% notice tip %}}
During deployment, the environment status will show "Updating". Don't worry, this is normal!
{{% /notice %}}

4. **Verify Deployment**
   - Once health status is **Ok** (green)
   - Click on the **Domain** URL
   - You should see your custom Flask application with your student information

![API Info Response](/images/3.deployapp/0034.png)

{{% notice success %}}
**Congratulations!** Your custom Flask application is now running on AWS Elastic Beanstalk. Take screenshots of your application for documentation.
{{% /notice %}}

### Troubleshooting

If deployment fails, check **Logs** in Elastic Beanstalk Console:

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| 502 Bad Gateway | App failed to start | Check logs for Python errors |
| Module not found | Missing in requirements.txt | Add Flask==3.0.0 to requirements.txt |
| Wrong file structure | Folder zipped instead of files | Re-create ZIP with only files at root level |

{{% notice info %}}
**Next Step**: Continue to Section 4 to learn how to monitor your application with CloudWatch and inspect EC2 instances.
{{% /notice %}}

