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
