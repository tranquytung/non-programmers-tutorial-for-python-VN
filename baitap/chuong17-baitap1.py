#!/bin/python

# Ghi vao mot file
out_file = open("filecanghi.txt","w")
out_file.write("Day la doan text duoc ghi vao file \nBoi To Thanh Cong")
out_file.close()

# Doc file vua ghi
in_file = open("filecanghi.txt", "r")
text = in_file.read()
in_file.close()

# In ra file vua doc
print text
