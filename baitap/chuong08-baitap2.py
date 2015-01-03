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
