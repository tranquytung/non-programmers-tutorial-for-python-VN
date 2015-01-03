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

Hãy quan sát ví dụ trên, ta sẽ thấy có hàm không cần đối số truyền vào, có hàm sẽ trả về kết quả thông qua lệnh `return`.


## Biến trong hàm

Trong hàm có một kiểu biến đặc biệt, gọi là biến cục bộ `local variable`. Biến này chỉ tồn tại khi hàm hoạt động. Khi biến cục bộ cùng tên với các biến khác (ví dụ như trùng tên với biện toàn cục - global variable) thì biến cục bộ sẽ bị ẩn đi. Hãy xem ví dụ dưới để rõ hơn về tình huống này.

```sh
#!/bin/python

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
root@cong-kvm:~# python chuong8-bai3.py
trong ham print_ham() a = 17
a =  4 la bien duoc gan o ngoai han print_ham()
root@cong-kvm:~# cat chuong8-bai3.py
```

Biến được gán trong hàm sẽ không bị ghi đè bởi biến toàn cục. Chúng chỉ tồn tại bên trong hàm mà thôi. Như chương trình trên, khi gọi biến `a` trong hàm, giá trị `17` sẽ được gán cho biến `a`. Nhưng khi kết thúc hàm, biến `a` lại trở về giá trị `4` - giá trị gán ở ngoài hàm.

```sh
#!/bin/python

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
root@cong-kvm:~# python chuong8-bai4.py
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



















