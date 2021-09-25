for x in range(5):
    print(x)
    if x == 2: break
else:
    print("Vòng lặp lết thúc tại x = {}".format(x))



danhsachsinhvien = ["An, Khánh, Minh, Lĩnh, Tỵ"]
for sinhvien in danhsachsinhvien:
    print(sinhvien)

for char in danhsachsinhvien[1]:
    print(char)

tong = 0
for x in range(11):
    tong += input
    print("Tổng từ 1-10: {}".format(tong))