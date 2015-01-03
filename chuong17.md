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

`\n` là ký tự ngắt dòng trong Python. Nó sẽ nói cho Python biết rằng "Dòng tiếp theo cần ngắt và xuống dòng.

Tóm tắt về việc đọc ghi file trong Python như sau:
* Để thao tác với một đối tượng file, ta sử dụng hàm `open`.
* Có thể đọc hoặc ghi với đối tượng file trong Python (phụ thuộc vào việc mở file đó như thế nào).
* Hãy đóng file khi thao tác xong với nó.

Để làm việc với file, bước đầu tiên cần sử dụng hàm `open`. Cú pháp `file_object = open(filename, mode)`. Trong đó: 
* file_object : Là biến truyền vào cho đối tượng file cần thao tác.
* filename: Là tên của file.
* mode: là chế độ để chỉ ra thao tác với file, là đọc `(r)` hay là ghi `(w)`.

Tiếp theo là các đối tượng hàm thường được gọi. Có 02 hàm phổ biến là `write` và `read`. Hàm `write` sẽ thêm một chuỗi vào file. Hàm `read` dùng để đọc nội dung file và trả về kết quả là một chuỗi. Nếu không có đối số truyền vào thì nó sẽ về toàn bộ nội dung file đó.





