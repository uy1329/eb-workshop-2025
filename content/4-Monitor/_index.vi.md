---
title : "Giám sát ứng dụng"
date : "2025-12-01"
weight : 4
chapter : false
pre : " <b> 4. </b> "
---

#### Giám sát sức khỏe ứng dụng

Sau khi triển khai ứng dụng lên AWS Elastic Beanstalk, việc giám sát tình trạng và hiệu suất của nó rất quan trọng. AWS cung cấp các công cụ giám sát toàn diện được tích hợp với Elastic Beanstalk.

### Giám sát môi trường Elastic Beanstalk

Trong phần này, bạn sẽ học cách:

1. **Xem tình trạng môi trường**
   - Kiểm tra trạng thái sức khỏe tổng thể của môi trường
   - Xem xét các chỉ số và metrics
   - Hiểu các màu trạng thái (Xanh lá, Vàng, Đỏ, Xám)

2. **Giám sát EC2 Instances**
   - Xem các EC2 instances đang chạy ứng dụng của bạn
   - Kiểm tra trạng thái và chi tiết instance
   - Truy cập các metrics của instance

3. **Xem xét Events của môi trường**
   - Theo dõi các sự kiện tạo và cập nhật môi trường
   - Giám sát hoạt động triển khai
   - Khắc phục sự cố bằng event logs

4. **Tích hợp CloudWatch**
   - Xem CloudWatch metrics cho môi trường của bạn
   - Giám sát CPU utilization, network traffic và request counts
   - Thiết lập alarms để giám sát chủ động (tùy chọn)

5. **Truy cập Application Logs**
   - Xem application logs trực tiếp từ Elastic Beanstalk console
   - Tải logs về để phân tích offline
   - Stream logs đến CloudWatch Logs (nếu được bật)

### Trạng thái sức khỏe môi trường

Elastic Beanstalk sử dụng các màu trạng thái sau:

- **Xanh lá (Ok)**: Môi trường đang hoạt động bình thường
- **Vàng (Warning)**: Một hoặc nhiều instances gặp vấn đề, nhưng môi trường vẫn hoạt động
- **Đỏ (Degraded/Severe)**: Môi trường có vấn đề nghiêm trọng và có thể không hoạt động
- **Xám (Unknown)**: Không thể xác định trạng thái sức khỏe

### Truy cập Monitoring Dashboard

Để giám sát môi trường của bạn:

1. Truy cập [AWS Elastic Beanstalk Console](https://console.aws.amazon.com/elasticbeanstalk)
2. Chọn môi trường của bạn: `Elastic-beanstalk-demo-env`
3. Dashboard hiển thị:
   - Trạng thái sức khỏe
   - Environment URL
   - Phiên bản đang chạy
   - Thông tin Platform
   - Các sự kiện gần đây

### Các metrics quan trọng cần giám sát

Giám sát các metrics quan trọng sau cho ứng dụng của bạn:

- **Instances Health**: Số lượng instances khỏe mạnh vs không khỏe mạnh
- **Environment Health**: Trạng thái môi trường tổng thể
- **Requests**: Số lượng HTTP requests và response codes
- **Latency**: Thời gian phản hồi của ứng dụng
- **CPU Utilization**: Mức sử dụng CPU của EC2 instance
- **Network I/O**: Lưu lượng mạng đến và đi

{{% notice info %}}
**Lưu ý**: Đối với môi trường production, hãy cân nhắc bật Enhanced Health Reporting và CloudWatch log streaming để giám sát chi tiết hơn.
{{% /notice %}}

{{% notice tip %}}
**Best Practice**: Thiết lập CloudWatch alarms để nhận thông báo khi metrics vượt ngưỡng, cho phép bạn phản ứng nhanh với các vấn đề.
{{% /notice %}}


