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

```sh
#!/bin/python

# script, a, b = argv

def gia_tri_tuyet_doi(n):
    if n < 0:
        n = -n
    return n

a = 6
b = -5

# print "Gia tri tuyet doi cua %s va %s la: " % (a, b)

if gia_tri_tuyet_doi(a) == gia_tri_tuyet_doi(b):
    print "Gia tri tuyet doi cua %d va %d la BANG nhau" % (a, b)

else:
    print "Gia tri tuyet doi cua %d va %d la KHAC nhau" % (a, b)
```

Kết quả của chương trình trên là 
```sh
Gia tri tuyet doi cua 6 va -5 la KHAC nhau
```

Một vài chú ý được rút ra từ chương trình trên: 
* Từ khóa chính trong chương trình trên là `def` - viết tắt của từ `define`, nó dùng để bắt đầu một hàm trong Python.
* Ngay sau nó là tên của hàm `gia_tri_tuyet_doi`. 
* Sau tên của hàm là `(n)`, giá trị `n` được truyền vào khi hàm được gọi ở phần dưới. Kết thúc hàm luôn là dấu hai chấm `:`. 
* Hàm có thể có hoặc không có giá trị trả về, nếu có thì nó được gọi bằng từ khóa `return`. 

Hãy quan sát ví dụ dưới để biết thêm về hàm trong Python.

```sh
#!/bin/python

def xin_chao():
    print "Xin chao cac ban !"

def dien_tich(chieucao, chieurong):
    return chieucao * chieurong

def chao_mung(ten):
    print "Xin chao", ten

# Goi hai lan ham xin_chao()
xin_chao()
xin_chao()

# Goi ham chao_mung() voi doi so truyen vao la Cong
chao_mung("Cong")

# Khai bao gia tri chieucao va chieu rong, sau do goi ham dien tich
chieucao = 5
chieurong = 4
print "Dien tich la: ", dien_tich(chieucao, chieurong)
```

Kết quả:

```sh
root@cong-kvm:~# python chuong18-bai3.py
Xin chao cac ban !
Xin chao cac ban !
Xin chao Cong
Dien tich la:  20

```





























