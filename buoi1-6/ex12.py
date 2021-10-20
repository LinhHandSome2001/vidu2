def thongtinsinhvien(**sinhvien):
    if "hoten" in sinhvien.keys():
        print("Họ tên: {}".format(sinhvien["hoten"]))
    if "diachi" in sinhvien.keys():
        print("Địa chỉ: {}".format(sinhvien["diachi"]))
    if "namsinh" in sinhvien.keys():
        tuoi = 2021 - sinhvien["namsinh"]
        print("Tuổi: {}".format(tuoi))

thongtinsinhvien(hoten="Lĩnh", diachi="176 Trần Phú", namsinh=2001)
print("-------")
thongtinsinhvien(hoten="Lĩnh", diachi="176 Trần Phú",)
print("-------")



def hello2(*name):
    print("Số lượng tham số: {}".format(len(name)))
    for x in name:
        print(f"Xin chào {x}")

hello2("Hoa")
hello2("Tí", "Tèo", "Teo")
hello2()

def hello(name, age):
    print("Xin chào, tôi là {} - {} tuổi".format(name, age))
    print("Tôi đang ở Việt Nam")
hello("Lĩnh", 20)
hello(age=20, name="Lĩnh")

print("---------------")
def hello3(name = "Lĩnh"):
    print(f"Xin chào tôi là: {name}")

hello3()
hello3("Đại")

print("---------------")
def hello4(dssv):
    for sv in dssv:
        print(f"Hello {sv}")

dssv = ["Lĩnh, Tỵ, Việt, Sơn"]
hello4(dssv)
print("---------------")

# lambda
x = lambda a: a + 10
y =  lambda a, b: a + b
print(x(20))
print(y(100, 200))