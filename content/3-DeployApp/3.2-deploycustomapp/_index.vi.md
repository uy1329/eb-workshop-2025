---
title : "Deploy Ứng dụng Flask Tùy chỉnh"
date : "2025-12-02"
weight : 2
chapter : false
pre : " <b> 3.2 </b> "
---

#### Deploy Ứng dụng Flask Tùy chỉnh của bạn

Sau khi tạo môi trường Elastic Beanstalk với ứng dụng mẫu ở Phần 3.1, bây giờ chúng ta sẽ deploy ứng dụng Flask tùy chỉnh.

{{% notice info %}}
**Yêu cầu**: Đảm bảo bạn đã chuẩn bị file ZIP ứng dụng Flask từ Phần 2.2. Nếu chưa, vui lòng hoàn thành Phần 2.2 trước.
{{% /notice %}}

### Deploy Ứng dụng Tùy chỉnh

1. **Vào Elastic Beanstalk Console**
   - Truy cập application của bạn (đã tạo ở 3.1)
   - Chọn environment của bạn

![Environment Dashboard](/eb-workshop-2025/images/3.deployapp/0030.png)

2. **Upload và Deploy**
   - Click nút **Upload and deploy**
   - Click **Choose file**
   - Chọn file `flask-app.zip` của bạn
   - **Version label**: Nhập `v1.0` (hoặc tên phiên bản bạn muốn)
   - Click **Deploy**

![Trang chủ ứng dụng](/eb-workshop-2025/images/3.deployapp/0032.png)

3. **Theo dõi quá trình Deploy**
   - Xem phần **Events**
   - Deploy thường mất 2-5 phút
   - Đợi health status trở về **Ok** (màu xanh)

![Trang About](/eb-workshop-2025/images/3.deployapp/0033.png)

{{% notice tip %}}
Trong quá trình deploy, environment status sẽ hiển thị "Updating". Đừng lo lắng, đây là bình thường!
{{% /notice %}}

4. **Xác minh Deploy**
   - Khi health status hiển thị **Ok** (màu xanh)
   - Click vào **Domain** URL
   - Bạn sẽ thấy ứng dụng Flask tùy chỉnh với thông tin sinh viên của bạn

![API Info Response](/eb-workshop-2025/images/3.deployapp/0034.png)

{{% notice success %}}
**Chúc mừng!** Ứng dụng Flask tùy chỉnh của bạn đã chạy trên AWS Elastic Beanstalk. Hãy chụp màn hình ứng dụng để làm tài liệu.
{{% /notice %}}

### Khắc phục sự cố

Nếu deploy thất bại, kiểm tra **Logs** trong Elastic Beanstalk Console:

| Vấn đề | Nguyên nhân có thể | Giải pháp |
|-------|---------------|----------|
| 502 Bad Gateway | App không khởi động được | Kiểm tra logs để tìm lỗi Python |
| Module not found | Thiếu trong requirements.txt | Thêm Flask==3.0.0 vào requirements.txt |
| Cấu trúc file sai | Nén folder thay vì files | Tạo lại ZIP chỉ với files ở cấp gốc |

{{% notice info %}}
**Bước tiếp theo**: Tiếp tục Phần 4 để học cách monitoring ứng dụng với CloudWatch và kiểm tra EC2 instances.
{{% /notice %}}

