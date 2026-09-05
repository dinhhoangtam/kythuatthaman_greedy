# kythuatthaman_greedy

# ĐIỆN MÁY CÔNG NGHỆ NHẬT DUY

Website giới thiệu và kinh doanh các sản phẩm điện máy, điện tử, điện lạnh, thiết bị gia dụng và công nghệ hiện đại. Hệ thống được xây dựng nhằm hỗ trợ khách hàng tra cứu thông tin sản phẩm, đặt hàng trực tuyến và quản lý hoạt động kinh doanh hiệu quả.

---

## Giới thiệu

Điện Máy Công Nghệ Nhật Duy là đơn vị cung cấp các sản phẩm điện máy, điện tử và giải pháp công nghệ phục vụ nhu cầu gia đình và doanh nghiệp. Website được xây dựng nhằm:

* Giới thiệu sản phẩm đến khách hàng.
* Hỗ trợ đặt hàng trực tuyến.
* Quản lý sản phẩm và đơn hàng.
* Cập nhật thông tin khuyến mãi nhanh chóng.
* Nâng cao trải nghiệm mua sắm trực tuyến.

---

## Chức năng chính

### Dành cho khách hàng

* Xem danh sách sản phẩm.
* Tìm kiếm sản phẩm theo tên.
* Xem chi tiết sản phẩm.
* Thêm sản phẩm vào giỏ hàng.
* Đặt hàng trực tuyến.
* Liên hệ và nhận hỗ trợ tư vấn.

### Dành cho quản trị viên

* Quản lý sản phẩm.
* Quản lý danh mục sản phẩm.
* Quản lý khách hàng.
* Quản lý đơn hàng.
* Thống kê doanh thu.
* Quản lý nội dung website.

---

## Công nghệ sử dụng

### Front-end

* HTML5
* CSS3
* JavaScript
* Bootstrap

### Back-end

* PHP

### Cơ sở dữ liệu

* MySQL

### Môi trường phát triển

* XAMPP
* phpMyAdmin
* Visual Studio Code

---

## Cấu trúc thư mục

```text
DienMayNhatDuy/
│
├── index.php
├── login.php
├── register.php
├── cart.php
├── checkout.php
│
├── css/
│   └── style.css
│
├── js/
│   └── script.js
│
├── images/
│
├── admin/
│   ├── dashboard.php
│   ├── products.php
│   ├── orders.php
│   └── customers.php
│
├── includes/
│   ├── header.php
│   ├── footer.php
│   └── connect.php
│
└── database/
    └── dienmay_nhatduy.sql
```

---

## Cơ sở dữ liệu

### Bảng users

| Trường   | Kiểu dữ liệu |
| -------- | ------------ |
| id       | INT          |
| fullname | VARCHAR(100) |
| email    | VARCHAR(100) |
| password | VARCHAR(255) |
| role     | VARCHAR(20)  |

### Bảng categories

| Trường        | Kiểu dữ liệu |
| ------------- | ------------ |
| id            | INT          |
| category_name | VARCHAR(100) |

### Bảng products

| Trường       | Kiểu dữ liệu |
| ------------ | ------------ |
| id           | INT          |
| product_name | VARCHAR(255) |
| price        | DECIMAL      |
| image        | VARCHAR(255) |
| description  | TEXT         |
| category_id  | INT          |

### Bảng orders

| Trường        | Kiểu dữ liệu |
| ------------- | ------------ |
| id            | INT          |
| customer_name | VARCHAR(100) |
| phone         | VARCHAR(20)  |
| address       | TEXT         |
| total_amount  | DECIMAL      |
| order_date    | DATETIME     |

---

## Cài đặt hệ thống

### Bước 1: Cài đặt XAMPP

Khởi động:

* Apache
* MySQL

### Bước 2: Tạo cơ sở dữ liệu

Mở phpMyAdmin:

```sql
CREATE DATABASE dienmay_nhatduy;
```

Import file:

```text
dienmay_nhatduy.sql
```

### Bước 3: Cấu hình kết nối

File:

```php
includes/connect.php
```

```php
$host = "localhost";
$user = "root";
$password = "";
$dbname = "dienmay_nhatduy";
```

### Bước 4: Chạy dự án

Truy cập:

```text
http://localhost/DienMayNhatDuy
```

---

## Các nhóm sản phẩm

* Tivi
* Máy lạnh
* Tủ lạnh
* Máy giặt
* Nồi cơm điện
* Máy lọc không khí
* Thiết bị nhà bếp
* Thiết bị năng lượng mặt trời
* Thiết bị điện tử gia dụng

---

## Mục tiêu phát triển

* Tích hợp thanh toán trực tuyến.
* Tích hợp chatbot tư vấn khách hàng.
* Đồng bộ đơn hàng theo thời gian thực.
* Phát triển ứng dụng trên Android và iOS.
* Tích hợp AI đề xuất sản phẩm.

---

## Thành viên thực hiện

* Đinh Hoàng Tâm
* ....................................
* ....................................

---

## Giấy phép

Dự án được xây dựng phục vụ mục đích học tập, nghiên cứu và phát triển hệ thống quản lý bán hàng điện máy.
