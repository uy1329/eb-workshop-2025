---
title : "Giới thiệu"
date: "2025-12-02" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---

#### AWS Elastic Beanstalk là gì?

**AWS Elastic Beanstalk** là một dịch vụ Platform as a Service (PaaS) giúp dễ dàng triển khai, quản lý và mở rộng ứng dụng web và dịch vụ. Bạn chỉ cần tải code lên, và Elastic Beanstalk sẽ tự động xử lý các chi tiết triển khai bao gồm:

- Cung cấp dung lượng
- Cân bằng tải
- Tự động mở rộng
- Giám sát tình trạng ứng dụng

#### Lợi ích chính

**1. Dễ sử dụng**
- Tải code ứng dụng lên và Elastic Beanstalk lo phần còn lại
- Không cần lo lắng về quản lý hạ tầng
- Tập trung vào viết code, không phải quản lý server

**2. Triển khai nhanh**
- Triển khai ứng dụng trong vài phút
- Tự động thiết lập môi trường
- Hỗ trợ nhiều nền tảng (Node.js, Python, Java, .NET, PHP, Ruby, Go, Docker)

**3. Tiết kiệm chi phí**
- Không tính phí cho chính dịch vụ Elastic Beanstalk
- Chỉ trả tiền cho các tài nguyên AWS (EC2, S3, RDS, v.v.) mà ứng dụng sử dụng
- Tự động mở rộng giúp tiết kiệm chi phí bằng cách điều chỉnh tài nguyên theo nhu cầu

**4. Kiểm soát hoàn toàn**
- Truy cập đầy đủ vào các tài nguyên AWS cơ bản
- Có thể tùy chỉnh bất kỳ khía cạnh nào của hạ tầng
- Chọn loại instance, database, quy tắc scaling, v.v.

**5. Giám sát và Quản lý**
- Tích hợp sẵn CloudWatch monitoring
- Dashboard hiển thị trạng thái ứng dụng
- Tự động thu thập và lưu trữ log

#### Cách hoạt động

1. **Chọn nền tảng**: Chọn ngôn ngữ lập trình/framework của bạn (ví dụ: Node.js, Python, PHP)
2. **Tải code lên**: Triển khai qua console, CLI, hoặc Git
3. **Elastic Beanstalk cung cấp tài nguyên**: Tự động tạo EC2 instances, load balancers, auto-scaling groups
4. **Giám sát và quản lý**: Sử dụng dashboard để kiểm tra tình trạng, xem logs và cập nhật

#### Các thành phần Elastic Beanstalk

- **Application**: Container logic cho dự án của bạn
- **Environment**: Tập hợp các tài nguyên AWS chạy phiên bản ứng dụng của bạn
- **Platform**: Hệ điều hành, ngôn ngữ lập trình, runtime và web server
- **Application Version**: Phiên bản cụ thể của code có thể triển khai

#### Kiến trúc Workshop

{{% notice info %}}**Quan trọng**: Workshop này sử dụng **Single Instance mode** (không có Load Balancer) để:
- Tiết kiệm chi phí (miễn phí trong Free Tier)
- Đơn giản hóa quá trình học
- Phù hợp cho môi trường development/testing
{{% /notice %}}

**Sơ đồ Kiến trúc:**

![AWS Elastic Beanstalk Architecture]({{< relref "/" >}}images/1.introduce/architecture.png)

**Giải thích các thành phần:**

1. **Developer**: Người phát triển upload code lên Elastic Beanstalk
2. **Internet Gateway**: Cổng kết nối giữa Internet và VPC
3. **VPC (Virtual Private Cloud)**: Mạng ảo riêng biệt trên AWS
4. **Public Subnet**: Subnet có kết nối Internet, chứa EC2 Instance
5. **EC2 Instance**: 
   - Máy chủ chạy ứng dụng Python Flask
   - Có Public IP để truy cập trực tiếp từ Internet
   - Instance type: t3.micro (Free Tier)
6. **Elastic Beanstalk**: 
   - Quản lý và giám sát EC2 Instance
   - Tự động deploy code, cấu hình môi trường
   - Thực hiện health checks
7. **S3 Bucket**: 
   - Lưu trữ các phiên bản code (application versions)
   - Lưu logs và artifacts

**Luồng hoạt động:**
1. Developer upload code lên Elastic Beanstalk
2. EB lưu code version vào S3 Bucket
3. EB deploy code lên EC2 Instance trong Public Subnet
4. User truy cập ứng dụng qua Internet Gateway → EC2 Instance (Public IP)

---

**Nâng cấp lên Load Balanced Mode** (Tùy chọn - Production):

Nếu cần môi trường production với high availability:
- **Load Balancer**: Phân phối traffic đến nhiều EC2 instances
- **Auto Scaling Group**: Tự động tăng/giảm instances (min: 1, max: 4)
- **Multi-AZ Deployment**: Instances ở nhiều Availability Zones
- **Chi phí thêm**: ~$16-18/tháng cho Application Load Balancer

Xem hướng dẫn chi tiết ở Section 3.1 (Bước 2).

#### Khi nào nên sử dụng Elastic Beanstalk

✅ **Phù hợp cho:**
- Ứng dụng web và API
- Microservices
- Ứng dụng cần triển khai nhanh
- Môi trường phát triển và thử nghiệm
- Nhóm muốn tập trung vào code hơn là hạ tầng

❌ **Cân nhắc các lựa chọn khác cho:**
- Kiến trúc đa tầng phức tạp (sử dụng CloudFormation hoặc Terraform)
- Ứng dụng yêu cầu cấu hình tùy chỉnh rất cụ thể
- Ứng dụng serverless (sử dụng Lambda thay thế)

#### Elastic Beanstalk vs Triển khai Truyền thống

| Triển khai Truyền thống | Elastic Beanstalk |
|-------------------------|-------------------|
| Thiết lập server thủ công | Tự động cung cấp |
| Cấu hình scaling thủ công | Auto-scaling tích hợp sẵn |
| Thiết lập monitoring thủ công | Monitoring tích hợp |
| Quy trình triển khai phức tạp | Tải code đơn giản |
| Mất hàng giờ để triển khai | Mất vài phút để triển khai |

Trong workshop này, bạn sẽ học cách thực hành triển khai ứng dụng web sử dụng AWS Elastic Beanstalk!
