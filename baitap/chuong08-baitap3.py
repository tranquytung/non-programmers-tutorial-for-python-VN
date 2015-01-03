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
