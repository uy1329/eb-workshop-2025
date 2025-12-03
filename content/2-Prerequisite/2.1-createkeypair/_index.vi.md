---
title : "Tạo EC2 Key Pair"
date : "2025-12-02"
weight : 1
chapter : false
pre : " <b> 2.1 </b> "
---

#### Tạo EC2 Key Pair

EC2 Key Pair được sử dụng để kết nối an toàn đến EC2 instances qua SSH. Mặc dù đây là tùy chọn cho Elastic Beanstalk, việc tạo key pair cho phép bạn khắc phục sự cố và quản lý instances trực tiếp nếu cần.

#### Các bước tạo Key Pair

1. **Điều hướng đến EC2 Console**
   - Trong AWS Management Console, tìm kiếm **EC2**
   - Click vào dịch vụ **EC2**
   - Bạn có thể sử dụng bất kỳ region nào (khuyến nghị **Sydney - ap-southeast-2**)

2. **Truy cập Key Pairs**
   - Trong thanh bên trái dưới **Network & Security**, click **Key Pairs**
   - Click nút **Create key pair** (nút màu cam ở góc trên bên phải)

3. **Cấu hình Key Pair**

![Tạo Key Pair](/eb-workshop-2025/images/2.prerequisite/0003.png)

Điền các thông tin sau:

- **Name**: `elastic-beanstalk-keypair`
  - Sử dụng chính xác tên này hoặc nhớ tên tùy chỉnh của bạn
- **Key pair type**: **RSA**
  - RSA là loại mã hóa được hỗ trợ rộng rãi nhất
- **Private key file format**: 
  - **.pem** (cho Mac/Linux/Windows 10+)
  - **.ppk** (cho PuTTY trên Windows cũ hơn)

4. **Tạo và Tải xuống**
   - Click nút **Create key pair**
   - File private key (`.pem` hoặc `.ppk`) sẽ tự động tải về máy tính của bạn
   - **Quan trọng**: Lưu file này ở nơi an toàn. Bạn không thể tải lại file này!

{{% notice warning %}}
**Giữ private key an toàn!** Nếu mất file này, bạn sẽ không thể kết nối đến EC2 instance qua SSH. Lưu trữ nó ở vị trí an toàn và không bao giờ chia sẻ công khai.
{{% /notice %}}

{{% notice tip %}}
Đối với người dùng Windows: Nếu bạn tải file .pem, bạn có thể cần chuyển đổi sang định dạng .ppk bằng PuTTYgen nếu muốn sử dụng PuTTY cho kết nối SSH.
{{% /notice %}}

#### Xác minh Key Pair đã tạo

Sau khi tạo, bạn sẽ thấy key pair của mình được liệt kê trong Key Pairs console:

- **Name**: elastic-beanstalk-keypair
- **Fingerprint**: Một mã định danh duy nhất
- **Type**: RSA
- **Created**: Ngày hôm nay

#### Bước tiếp theo

EC2 key pair của bạn đã sẵn sàng để sử dụng! Bạn sẽ chọn key pair này khi tạo môi trường Elastic Beanstalk trong Phần 3.

Ở bước tiếp theo, chúng ta sẽ chuẩn bị code ứng dụng để triển khai.
