#Chương 8: Định nghĩa ra hàm
Cấu trúc chương trình trong Python khi sử dụng hàm

## Tạo ra hàm

Ở chương một, chúng ta có một ví dụ về giá trị tuyệt đối của hai số như sau:

```sh
#!/bin/python

a = 23
b = -23

if a < 0:
    a = -a
if b < 0:
    b = -b
if a == b:
    print "Gia tri tuyet doi cua a va b bang nhau"
else:
    print "Gia tri tuyet doi cua a va b khac nhau"

```

Kết quả
```sh
Gia tri tuyet doi cua a va b bang nhau
```

Ở chương trình trên có các chi tiết được lặp đi lặp lại. Người lập trình thường ghét điều này. May mắn thay, Python đã cung cấp cho bạn một thứ gọi là Hàm để làm những việc lặp đi lặp lại như này. Dưới là đoạn code của chương trình trên được viết lại bằng hàm. 

