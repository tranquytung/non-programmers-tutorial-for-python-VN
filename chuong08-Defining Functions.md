﻿#Chương 8: Định nghĩa ra hàm
Cấu trúc chương trình trong Python khi sử dụng hàm

## Tạo ra hàm

Ở chương một, chúng ta có một ví dụ về giá trị tuyệt đối của hai số như sau:

```sh
#!/bin/python
# chuong08-baitap1.py

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
# chuong08-baitap2.py

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
# chuong08-baitap3.py

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
root@cong-kvm:~# python chuong8-bai3.py
Xin chao cac ban !
Xin chao cac ban !
Xin chao Cong
Dien tich la:  20
```

Hãy quan sát ví dụ trên, ta sẽ thấy có hàm không cần đối số truyền vào, có hàm sẽ trả về kết quả thông qua lệnh `return`.


## Biến trong hàm

Trong hàm có một kiểu biến đặc biệt, gọi là biến cục bộ `local variable`. Biến này chỉ tồn tại khi hàm hoạt động. Khi biến cục bộ cùng tên với các biến khác (ví dụ như trùng tên với biện toàn cục - global variable) thì biến cục bộ sẽ bị ẩn đi. Hãy xem ví dụ dưới để rõ hơn về tình huống này.

```sh
#!/bin/python
# chuong08-baitap4.py

a = 4

def print_ham():
    a = 17
    print "trong ham print_ham() a =", a
#
# Goi ham print_ham()
print_ham()

# In ra bien a (bien toan cuc)

print "a = ", a, "la bien duoc gan o ngoai han print_ham()"

```

Kết quả:

```sh
root@cong-kvm:~# python chuong8-bai4.py
trong ham print_ham() a = 17
a =  4 la bien duoc gan o ngoai han print_ham()
```

Biến được gán trong hàm sẽ không bị ghi đè bởi biến toàn cục. Chúng chỉ tồn tại bên trong hàm mà thôi. Như chương trình trên, khi gọi biến `a` trong hàm, giá trị `17` sẽ được gán cho biến `a`. Nhưng khi kết thúc hàm, biến `a` lại trở về giá trị `4` - giá trị gán ở ngoài hàm.

```sh
#!/bin/python
# chuong08-baitap5.py
a_var = 10
b_var = 15
c_var = 25

def a_func(a_var):
    print "Trong ham a_func(), bien a_var =", a_var
    b_var = 100 + a_var
    d_var = 2 * a_var
    print "Trong ham a_func(), bien b_var = ", b_var
    print "Trong ham a_func(), bien d_var = ", d_var
    print "Trong ham a_func(), bien c_var = ", c_var
    return b_var + 10

c_var = a_func(b_var)

print
print "a_var =", a_var
print "b_var =", b_var
print "c_var =", c_var
print "d_var =", d_var
```

Kết quả:
```sh
root@cong-kvm:~# python chuong8-bai5.py
Trong ham a_func(), bien a_var = 15
Trong ham a_func(), bien b_var =  115
Trong ham a_func(), bien d_var =  30
Trong ham a_func(), bien c_var =  25

a_var = 10
b_var = 15
c_var = 125
d_var =
Traceback (most recent call last):
  File "chuong8-bai4.py", line 22, in <module>
    print "d_var =", d_var
NameError: name 'd_var' is not defined
```

Trong ví dụ trên, khi hàm `a_func` được thực hiện biến `a_var, b_var, d_var` là các biến cục bộ. Sau khi hàm kết thúc, sẽ có một giá trị trả về là kết quả của dòng `return b_var + 10`. Các giá trị này sẽ dừng ngay khi hàm kết thúc.

Khi hàm được gọi, `c_var = a_func(b_var)`, giá trị 15 của biến `b_var` được gán cho biến `a_var`, lúc này có thể hiểu rằng hàm sẽ thể hiện như sau `a_func(15)`.

Sau khi hàm được gọi, biến `b_var` và `d_var` sẽ là các biến cục bộ và được gán giá trị mới. Toàn bộ các lệnh `print` bên trong hàm sẽ hiển thị ra giá trị của các biến cục bộ. 

Khi thực hiện chương trình trên, ta sẽ gặp thông báo lỗi `NameError`. Lúc này là lỗi thông báo biến `d_var` không được gán giá trị. Trước đó, biến `d_var` được in ra vì nó được khai báo trong hàm `a_func`.Sau khi kết thúc hàm, biến `d_var` không còn giá trị nên sẽ gây ra lỗi.

## Ví dụ

```sh
#!/bin/python
# chuong08-baitap6.py
# Chuong trinh chuyen doi giua do C va do F

def lua_chon():
    print "Lua chon"
    print "'P': Hien thi cac lua chon"
    print "'c': Chuyen doi sang do C"
    print "'f': Chuyen doi sang do F"
    print "'q': Thoat khoi chuong trinh"

def tu_C_sang_F(do_c):
    return 9.0 / 5.0 * do_c + 32

def tu_F_sang_C(do_f):
    return (do_f - 32.0) * 5.0 / 9.0

chon = "p"
while chon != "q":
    if chon == "c":
        nhietdo = input("Nhap do C vao: ")
        print "Do F la: ", tu_C_sang_F(nhietdo)
    elif chon == "f":
        nhietdo = input("Nhap do F vao: ")
        print "Do C la: ", tu_F_sang_C(nhietdo)
    elif chon != "q":
        lua_chon()
    chon = raw_input("Lua chon: ")
```

Kết quả: 
```sh
Lua chon
'P': Hien thi cac lua chon
'c': Chuyen doi sang do C
'f': Chuyen doi sang do F
'q': Thoat khoi chuong trinh
Lua chon: c
Nhap do C vao: 10
Do F la:  50.0
Lua chon: f
Nhap do F vao: 50
Do C la:  10.0
Lua chon: q
```

Chương trình tính diện tích
```sh 
#!/bin/python
# chuong08-bai7.py

# Chuong trinh tinh dien tich do nguoi dung nhap vao

print
def xin_chao():
    print "Xin chao"

def dien_tich(chieucao, chieurong):
    return chieucao * chieurong

def hien_thi_xin_chao(name):
    print "Xin chao, ", name

name = raw_input("Nhap ten ban vao: ")

# Goi ham xin_chao() va ham hien_thi_xin_chao()
xin_chao()
hien_thi_xin_chao(name)

# Khai bao chieu cao va chieu rong
print
print "Nhap chieu cao va chieu rong de tinh dien tich"
print
w = input("Chao cao: ")
while w <= 0:
    print "Chieu cao phai lon hon 0"
    w = input("Chieu cao: ")

h = input("Chieu rong: ")
while h <= 0:
    print "Chieu rong phai lon hon 0"
    h = input("Chieu rong: ")

# Goi ham tinh dien tich
print "Dien tich la: ", dien_tich(w,h)
```

Kết quả: 
```sh
root@cong-kvm:~# python chuong08-bai7.py

Nhap ten ban vao: CONG
Xin chao
Xin chao,  CONG

Nhap chieu cao va chieu rong de tinh dien tich

Chao cao: 9
Chieu rong: -9
Chieu rong phai lon hon 0
Chieu rong: -23
Chieu rong phai lon hon 0
Chieu rong: 2
Dien tich la:  18
```












