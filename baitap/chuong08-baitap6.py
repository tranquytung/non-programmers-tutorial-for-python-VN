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