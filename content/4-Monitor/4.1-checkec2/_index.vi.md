---
title : "Kiểm tra EC2 trong Elastic Beanstalk"
date : "2025-11-30"
weight : 1
chapter : false
pre : " <b> 4.1 </b> "
---

#### Kiểm tra EC2 Instances do Elastic Beanstalk tạo

Elastic Beanstalk tự động tạo và quản lý EC2 instances cho ứng dụng của bạn. Hãy cùng kiểm tra các instances này.

### Xem EC2 Instances

1. **Từ Elastic Beanstalk Console:**
   - Vào environment của bạn
   - Click **Configuration** trong menu bên trái
   - Ở phần **Instances**, click **Edit**
   - Bạn sẽ thấy instance type và cài đặt scaling

2. **Từ EC2 Console:**
   - Truy cập **EC2 Console**
   - Click **Instances** trong menu bên trái
   - Tìm instances có tên chứa tên environment của bạn
   - Tags sẽ bao gồm: `elasticbeanstalk:environment-name`

### Chi tiết Instance

Kiểm tra các thông tin sau:

- **Instance Type**: Mặc định là `t2.micro` (free tier)
- **Instance State**: Phải là **Running**
- **Security Groups**: Elastic Beanstalk tạo security groups tự động
- **IAM Role**: Phải có `aws-elasticbeanstalk-ec2-role`
- **Tags**: Bao gồm thông tin application và environment

### Security Groups

Elastic Beanstalk tạo security groups cho:

1. **EC2 Instance Security Group**
   - Cho phép HTTP (port 80) từ load balancer hoặc internet
   - Cho phép HTTPS (port 443) nếu được cấu hình
   - Cho phép SSH (port 22) nếu có cấu hình key pair

2. **Load Balancer Security Group** (nếu high availability)
   - Cho phép HTTP/HTTPS từ internet
   - Chuyển tiếp đến EC2 instances

### Giám sát Instance Health

1. **Trong Elastic Beanstalk Console:**
   - Vào environment của bạn
   - Xem tab **Health**
   - Kiểm tra trạng thái instance (xanh = healthy)

2. **Trong CloudWatch:**
   - Xem CPU utilization
   - Xem network in/out
   - Xem disk operations

### Kết nối đến Instance (Tùy chọn)

Nếu bạn đã cấu hình EC2 key pair khi setup:

1. Vào **EC2 Console**
2. Chọn instance của bạn
3. Click **Connect**
4. Chọn phương thức kết nối:
   - **EC2 Instance Connect** (dựa trên trình duyệt)
   - **SSH client** (sử dụng key pair của bạn)

### Xem Application Logs

Logs được lưu trên instance:
- Vị trí: `/var/log/`
- Application logs: `/var/log/web.stdout.log`
- Error logs: `/var/log/web.stderr.log`
- Elastic Beanstalk logs: `/var/log/eb-engine.log`

{{% notice tip %}}
Bạn cũng có thể tải logs trực tiếp từ Elastic Beanstalk Console → Logs → Request Logs
{{% /notice %}}

### Hiểu về Auto Scaling

Nếu bạn bật auto scaling:
- **Minimum instances**: Số lượng tối thiểu luôn chạy
- **Maximum instances**: Số lượng tối đa khi có traffic cao
- **Scaling triggers**: CPU utilization, network, v.v.
- Theo dõi hoạt động scaling trong tab **Events**

