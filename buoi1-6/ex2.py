danhsach = []

hoten = input("Nhập họ tên: ")
danhsach.append(hoten)

hoten = input("Nhập họ tên: ")
danhsach.append(hoten)

hoten = input("Nhập họ tên: ")
danhsach.append(hoten)

hoten = input("Nhập họ tên: ")
danhsach.append(hoten)

hoten = input("Nhập họ tên: ")
danhsach.append(hoten)

print(danhsach)
vitri = int(input("Bạn muốn chỉnh sửa vị trí thứ: "))

hoten = input("Nhập họ tên: ")
danhsach[vitri] = hoten

print (danhsach)
print (danhsach.sort())