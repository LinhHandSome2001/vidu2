print("Nhập vào 3 số")
a = int(input(""))
c = int(input(""))
b = int(input(""))

if a > b and a > c:
        print("Số lớn nhất là: ", a)
elif b > c and b > a:
        print("Số lớn nhất là: ", b)
else:
        print("Số lớn nhất là: ", c)