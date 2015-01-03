# File IO - Input Output
Trong chương này chúng ta sẽ học về các ghi và đọc file.

```sh
root@cong-kvm:~# cat bai17.py
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

```

Kết quả 
```sh
root@cong-kvm:~# python bai17.py
Day la doan text duoc ghi vao file
Boi To Thanh Cong
root@cong-kvm:~#
```

Chương trình trên đã thực hiện việc tạo ra một file tên là `filecanghi.txt` vào chính thưc mục chứa mã nguồn của chương trình này. 

`\n` là ký tự ngắt dòng trong Python.



