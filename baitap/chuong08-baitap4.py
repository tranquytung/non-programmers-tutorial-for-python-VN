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