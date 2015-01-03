#Chương 8: Định nghĩa ra hàm

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