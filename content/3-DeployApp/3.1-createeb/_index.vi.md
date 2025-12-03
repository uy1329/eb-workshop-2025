---
title : "Tạo EB"
date : "2025-11-30"
weight : 1
chapter : false
pre : " <b> 3.1 </b> "
---

#### Tạo Elastic Beanstalk Environment với Sample Application

Trong phần này, chúng ta sẽ tạo môi trường Elastic Beanstalk và deploy ứng dụng mẫu để kiểm tra.

### Bước 1: Truy cập Elastic Beanstalk Console

1. Đăng nhập vào AWS Management Console
2. Tìm kiếm **Elastic Beanstalk** trong thanh tìm kiếm
3. Click vào **Create application**

![Create Application](/images/3.deployapp/0001.png)

### Bước 2: Cấu hình Environment

1. **Environment tier**: Chọn **Web server environment**
2. **Application name**: Nhập tên ứng dụng, ví dụ: `elastic-beanstalk-demo`
3. **Environment name**: Tự động tạo hoặc tùy chỉnh, ví dụ: `Elastic-beanstalk-demo-env`

![Configure Environment](/images/3.deployapp/0002.png)

4. **Platform**: Chọn **Python**
5. **Platform branch**: Chọn **Python 3.14 running on 64bit Amazon Linux 2023**
6. **Platform version**: Để mặc định (phiên bản khuyến nghị)
7. **Application code**: Chọn **Sample application**
   - Chúng ta sẽ deploy ứng dụng mẫu của AWS để test
   - Sau đó sẽ deploy ứng dụng Flask tùy chỉnh ở Section 3.2

![Platform Selection](/images/3.deployapp/0003.png)

8. **Presets**: Chọn **Single instance (free tier eligible)**
   - Phù hợp cho môi trường test/học tập
   - Không có Load Balancer, giúp tiết kiệm chi phí
   - EC2 Instance sẽ có Public IP để truy cập trực tiếp

{{% notice warning %}}**Workshop này sử dụng Single Instance mode** (không có Load Balancer). Nếu bạn muốn môi trường production với Load Balancer, xem phần "Nâng cấp lên Load Balanced Mode" bên dưới.{{% /notice %}}

![Presets](/images/3.deployapp/0004.png)

#### 💡 Nâng cấp lên Load Balanced Mode (Tùy chọn)

Nếu bạn muốn triển khai production environment với Load Balancer:

**Bước 2 - Thay đổi:**
- **Presets**: Chọn **High availability (with Load Balancer)**
- Environment sẽ tạo:
  - Application Load Balancer (ALB)
  - Auto Scaling Group (min: 1, max: 4 instances)
  - Multi-AZ deployment
  - Health checks qua Load Balancer

**Thời gian & Chi phí:**
- Thời gian tạo: 8-12 phút (thay vì 5-10 phút)
- Chi phí thêm: ~$16-18/tháng cho ALB
- EC2 instances: Tính theo số lượng instances chạy

**Lợi ích:**
- High Availability: Ứng dụng vẫn chạy nếu 1 instance fail
- Auto Scaling: Tự động mở rộng khi traffic tăng
- Zero-downtime deployment: Deploy không gián đoạn service
- Better security: EC2 instances trong private subnet

{{% notice tip %}}Nếu chọn Load Balanced mode, bỏ qua cảnh báo về "Public IP" ở Bước 4 vì Load Balancer sẽ xử lý public access.{{% /notice %}}

---

9. Click **Next** để cấu hình service access

### Bước 3: Cấu hình Service Access

**Service Role**

Nếu bạn chưa có Service role:

![Service Access Empty](/images/3.deployapp/0005.png)

1. Chọn **Create and use new service role**

![Create Service Role](/images/3.deployapp/0006.png)

2. AWS tự động tạo role với tên `aws-elasticbeanstalk-service-role`

![Service Role Creating](/images/3.deployapp/0007.png)

3. Role sẽ có các policies:
   - `AWSElasticBeanstalkEnhancedHealth`
   - `AWSElasticBeanstalkManagedUpdatesCustomerRolePolicy`

![Service Role Policies](/images/3.deployapp/0008.png)

4. Sau khi tạo, chọn role vừa tạo trong dropdown

![Service Role Selected](/images/3.deployapp/0009.png)

**EC2 Instance Profile**

Nếu bạn chưa có EC2 instance profile:

1. Chọn **Create and use new EC2 instance profile**

![Create Instance Profile](/images/3.deployapp/0010.png)

2. AWS tự động tạo instance profile với tên `aws-elasticbeanstalk-ec2-role`

![Instance Profile Creating](/images/3.deployapp/0011.png)

3. Instance profile sẽ có các policies:
   - `AWSElasticBeanstalkWebTier`
   - `AWSElasticBeanstalkWorkerTier`
   - `AWSElasticBeanstalkMulticontainerDocker`

![Instance Profile Policies](/images/3.deployapp/0012.png)

4. Sau khi tạo, chọn instance profile trong dropdown

![Instance Profile Selected](/images/3.deployapp/0013.png)

**EC2 Key Pair**

1. **EC2 key pair**: Chọn `elastic-beanstalk-keypair`
   - Key pair này đã tạo ở Section 2.1
   - Dùng để SSH vào EC2 instance nếu cần troubleshoot

![Key Pair Selected](/images/3.deployapp/0014.png)

2. Click **Next** để cấu hình networking

### Bước 4: Cấu hình Networking, Database và Tags

**VPC và Networking**

1. **VPC**: Chọn default VPC
   - Ví dụ: `vpc-067152750ba5e4cf4 (172.31.0.0/16)`

2. **Public IP address**: Chọn **Activated**
   - Bắt buộc cho single instance không có load balancer

3. **Instance subnets**: Chọn một availability zone
   - Ví dụ: `ap-southeast-2a` với subnet `172.31.0.0/20`

![Networking Configuration](/images/3.deployapp/0015.png)

**Database và Tags**

1. **Database**: Không chọn (để trống)
   - Workshop này không sử dụng RDS

2. **Tags**: Để trống (tùy chọn)

![Database and Tags](/images/3.deployapp/0016.png)

3. Click **Next** để cấu hình instance

### Bước 5: Cấu hình Instance Traffic và Scaling

**Instance Configuration**

1. **Root volume**: Để mặc định
2. **EC2 security groups**: Để mặc định
3. **CloudWatch monitoring**: 5 minute (basic monitoring)
4. **IMDSv1**: **Disabled** (khuyến nghị)
5. **IMDSv2**: Enabled

![Instance Configuration](/images/3.deployapp/0017.png)

**Capacity**

1. **Environment type**: Single instance
2. **Fleet composition**: On-Demand instances
3. **Architecture**: x86_64

![Capacity](/images/3.deployapp/0018.png)

4. **Instance types**: Chỉ chọn `t3.micro`
   - Xóa `t3.small` nếu có (không thuộc free tier)

{{% notice warning %}}
**Chỉ dùng t3.micro** để tránh phí! Instance `t3.small` tốn ~$15/tháng.
{{% /notice %}}

5. **AMI ID**: Để mặc định (Amazon Linux 2023 cho Python)

![Instance Types](/images/3.deployapp/0019.png)

6. Click **Next** để cấu hình monitoring

### Bước 6: Cấu hình Updates, Monitoring và Logging

**Monitoring**

1. **Health reporting**: Enhanced
2. **CloudWatch Logs**: Disabled (để tiết kiệm chi phí)

![Monitoring](/images/3.deployapp/0020.png)

**Managed Platform Updates**

1. **Managed updates**: Enabled
2. **Update window**: Tuesday, 19:45 UTC, 1 hour
3. **Update level**: Minor and patch

![Managed Updates](/images/3.deployapp/0021.png)

**Rolling Updates và Deployments**

1. **Deployment policy**: All at once
   - Deploy tất cả instances cùng lúc
   - Có downtime ngắn

![Rolling Updates](/images/3.deployapp/0022.png)

**Platform Software**

1. **Proxy server**: Nginx
2. **WSGI Path**: application
3. **Logs retention**: 7 days
4. **NumThreads**: 15

![Platform Software](/images/3.deployapp/0023.png)

5. Click **Next** để review

### Bước 7: Submit và Đợi

1. Click **Submit** để tạo environment
2. Quá trình tạo mất **5-10 phút**

AWS Elastic Beanstalk sẽ:
- Launch EC2 instance
- Cấu hình security groups
- Deploy sample application
- Thực hiện health checks

### Bước 8: Xác minh Environment

Khi environment tạo xong:

1. **Health status**: Ok (màu xanh)
2. **Domain URL**: Hiển thị URL công khai

![Environment Created](/images/3.deployapp/0030.png)

3. Click vào **Domain** để truy cập ứng dụng

Bạn sẽ thấy trang chào mừng của AWS Elastic Beanstalk sample application.

![Sample App Running](/images/3.deployapp/0031.png)

{{% notice success %}}
**Chúc mừng!** Environment Elastic Beanstalk đã sẵn sàng. Bây giờ chúng ta có thể deploy ứng dụng Flask tùy chỉnh ở Section 3.2.
{{% /notice %}}

{{% notice info %}}
Environment URL có dạng: `<env-name>.<random>.<region>.elasticbeanstalk.com`
{{% /notice %}}