# Sử dụng hình ảnh Nginx chính thức từ Docker Hub
FROM nginx:latest

# Sao chép tệp cấu hình tùy chỉnh vào container
COPY ./nginx.conf /etc/nginx/nginx.conf

# Sao chép nội dung trang web tĩnh vào thư mục HTML của Nginx
COPY ./html /usr/share/nginx/html

# Expose cổng 80 để truy cập HTTP
EXPOSE 80

# Khởi động Nginx
CMD ["nginx", "-g", "daemon off;"]