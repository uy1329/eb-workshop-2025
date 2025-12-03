---
title : "Các bước chuẩn bị"
date : "2025-11-30"
weight : 2
chapter : false
pre : " <b> 2. </b> "
---

#### Tổng quan về các bước chuẩn bị

Trước khi triển khai ứng dụng lên AWS Elastic Beanstalk, bạn cần chuẩn bị một số thành phần chính:

#### 1. EC2 Key Pair (Tùy chọn nhưng nên tạo)

**EC2 Key Pair là gì?**
- Key pair bao gồm public key (lưu trên AWS) và private key (bạn tải về)
- Dùng để kết nối an toàn đến EC2 instances qua SSH

**Tại sao nên tạo key pair?**
- Cho phép truy cập SSH trực tiếp vào EC2 instances để khắc phục sự cố
- Có thể xem logs, kiểm tra cấu hình và debug vấn đề
- Hữu ích cho người dùng nâng cao muốn kiểm soát hoàn toàn

{{% notice tip %}}
Trong workshop này, việc tạo key pair là tùy chọn nhưng khuyến khích để học tập.
{{% /notice %}}

#### 2. Chuẩn bị ứng dụng

**Yêu cầu ứng dụng:**
- Một ứng dụng web hoạt động được viết bằng ngôn ngữ/framework được hỗ trợ
- Được đóng gói đúng theo yêu cầu của Elastic Beanstalk

**Cho workshop này:**
- Chúng tôi cung cấp sẵn một ứng dụng Flask (Python) sẵn sàng triển khai
- Bạn sẽ tùy chỉnh nó với thông tin của mình
- Đóng gói thành file ZIP để triển khai

### Nội dung

Trong phần chuẩn bị này, chúng ta sẽ thực hiện:
- [2.1 - Tạo EC2 Key Pair](2.1-createkeypair/): Tạo key pair để truy cập SSH
- [2.2 - Chuẩn bị ứng dụng](2.2-prepareapp/): Tạo, tùy chỉnh và đóng gói ứng dụng Flask

{{% notice info %}}
Sau khi hoàn thành các bước chuẩn bị này, bạn sẽ sẵn sàng để tạo và triển khai ứng dụng Elastic Beanstalk!
{{% /notice %}}