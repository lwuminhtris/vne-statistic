### VnE Statistic là gì? 
VnE Statistic được tạo ra để thống kê xem quốc gia nào được nhắc đến nhiều nhất trong chuyên mục thế giới của báo VnExpress, qua đó phần nào cho thấy 
quốc gia nào trên thế giới đang là điểm nóng.
![alt](https://cdn.discordapp.com/attachments/835921395292700776/837957016643043348/Untitled.png)
### Môi trường và thư viện cần thiết
- Server được viết bằng Python, sử dụng web framework là Flask, cùng với đó có thư viện BeautifulSoup và request dùng để crawl dữ liệu từ trang web VnExpress
- Front-end (index.html) được viết bằng HTML, CSS và Javascript, có sử dụng Axios để fetch dữ liệu và ChartJS để tạo biểu đồ
### Hướng dẫn sử dụng 
- Sau khi clone repository về, cd vào folder server và trên powershell thực hiện các lệnh sau
```
$env:FLASK_APP = "app.py"
```
```
$ python -m flask run 
```
- Nếu thấy thông báo như sau thì có nghĩa server đã chạy thành công
![alt](https://cdn.discordapp.com/attachments/835921395292700776/837955371590221874/unknown.png)
- Server đưa tất cả dữ liệu cần thiết để thống kê lên localhost:5000 dưới dạng JSON
![alt](https://cdn.discordapp.com/attachments/835921395292700776/837957733805981746/unknown.png)
- Tiếp theo mở file index.html nằm ở thư mục gốc để xem kết quả là xong rồi đó 🎉
