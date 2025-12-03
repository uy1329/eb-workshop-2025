---
title : "Dọn dẹp tài nguyên"
date : "2025-12-01"
weight : 5
chapter : false
pre : " <b> 5. </b> "
---

#### Dọn dẹp tài nguyên

{{% notice warning %}}
**Quan trọng**: Nhớ xóa tất cả tài nguyên sau khi hoàn thành workshop để tránh chi phí AWS không mong muốn.
{{% /notice %}}

Sau khi hoàn thành workshop này, bạn nên xóa tất cả các tài nguyên AWS đã tạo để tránh phát sinh chi phí liên tục. Mặc dù chúng ta đã sử dụng các tài nguyên đủ điều kiện free tier, nhưng việc dọn dẹp khi hoàn thành là một best practice.

### Các tài nguyên cần xóa

Trong workshop này, chúng ta đã tạo các tài nguyên sau:

1. **Elastic Beanstalk Environment** - `Elastic-beanstalk-demo-env`
2. **Elastic Beanstalk Application** - `elastic-beanstalk-demo`
3. **EC2 Instance** - Được tạo bởi Elastic Beanstalk
4. **Security Groups** - Được tạo bởi Elastic Beanstalk
5. **IAM Roles** - Service role và EC2 instance profile
6. **EC2 Key Pair** - `elastic-beanstalk-keypair`

### Bước 1: Terminate Elastic Beanstalk Environment

Environment phải được terminate trước khi application có thể bị xóa.

1. Điều hướng đến [AWS Elastic Beanstalk Console](https://console.aws.amazon.com/elasticbeanstalk)
2. Chọn environment của bạn: `Elastic-beanstalk-demo-env`
3. Click menu dropdown **Actions**
4. Chọn **Terminate environment**
5. Trong hộp thoại xác nhận:
   - Nhập tên environment: `Elastic-beanstalk-demo-env`
   - Click **Terminate**

Quá trình terminate sẽ:
- Dừng EC2 instance
- Xóa security groups
- Gỡ bỏ các cấu hình cụ thể của environment
- Mất khoảng 5 phút

{{% notice info %}}
**Lưu ý**: Bạn có thể theo dõi tiến trình terminate trong tab Events.
{{% /notice %}}

### Bước 2: Xóa Elastic Beanstalk Application

Sau khi environment đã terminate hoàn toàn:

1. Trong Elastic Beanstalk Console, vào **Applications**
2. Chọn `elastic-beanstalk-demo`
3. Click menu dropdown **Actions**
4. Chọn **Delete application**
5. Xác nhận xóa bằng cách nhập tên application
6. Click **Delete**

### Bước 3: Xóa EC2 Key Pair (Tùy chọn)

Nếu bạn không cần key pair nữa:

1. Điều hướng đến **EC2 Console**
2. Trong menu bên trái, chọn **Key Pairs** dưới **Network & Security**
3. Chọn `elastic-beanstalk-keypair`
4. Click **Actions** → **Delete**
5. Xác nhận xóa

{{% notice warning %}}
**Cảnh báo**: Sau khi xóa, bạn không thể khôi phục private key. Đảm bảo bạn có backup nếu cần.
{{% /notice %}}

### Bước 4: Xóa IAM Roles (Tùy chọn)

Nếu bạn tạo IAM roles riêng cho workshop này và không cần chúng:

1. Điều hướng đến **IAM Console**
2. Click **Roles** trong menu bên trái
3. Xóa các roles sau:
   - `aws-elasticbeanstalk-service-role`
   - `aws-elasticbeanstalk-ec2-role`

**Cho mỗi role:**
1. Chọn role
2. Click **Delete**
3. Xác nhận xóa

{{% notice info %}}
**Lưu ý**: Nếu bạn dự định tạo thêm các môi trường Elastic Beanstalk trong tương lai, bạn có thể giữ lại các IAM roles này để tái sử dụng.
{{% /notice %}}

### Bước 5: Xác minh dọn dẹp hoàn tất

Xác minh rằng tất cả tài nguyên đã được xóa:

1. **EC2 Dashboard**:
   - Kiểm tra không có instances liên quan đến Elastic Beanstalk đang chạy
   - Xác minh security groups đã bị xóa (có thể mất vài phút)

2. **Elastic Beanstalk Console**:
   - Xác minh không có environments hoặc applications được liệt kê

3. **CloudWatch Logs** (nếu được bật):
   - Kiểm tra các log groups được tạo bởi Elastic Beanstalk
   - Xóa chúng nếu không còn cần

4. **S3 Buckets**:
   - Kiểm tra các S3 buckets được tạo bởi Elastic Beanstalk
   - Định dạng: `elasticbeanstalk-<region>-<account-id>`
   - Làm rỗng và xóa nếu không còn cần

### Thời gian hoàn thành dọn dẹp

Quá trình dọn dẹp hoàn toàn thường mất:
- **Environment termination**: 5-7 phút
- **Application deletion**: 1 phút
- **Các tài nguyên khác**: 1-2 phút

### Cân nhắc chi phí

- **Elastic Beanstalk**: Không tính phí cho bản thân dịch vụ
- **EC2 Instances**: Chi phí dừng khi instances bị terminate
- **S3 Storage**: Chi phí nhỏ nếu buckets chứa dữ liệu
- **CloudWatch Logs**: Chi phí cho logs được lưu trữ

{{% notice tip %}}
**Best Practice**: Luôn dọn dẹp tài nguyên sau khi hoàn thành workshop hoặc khi không còn cần. Thiết lập AWS Budgets để nhận cảnh báo nếu chi phí vượt quá số tiền dự kiến.
{{% /notice %}}

**Chúc mừng!** Bạn đã hoàn thành thành công workshop AWS Elastic Beanstalk và dọn dẹp tất cả tài nguyên.

