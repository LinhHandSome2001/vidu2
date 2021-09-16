import random
n = (random.randint(1,3))
lua_chon = int(input("Đoán số từ 1 đến 3: "))
if n == lua_chon:
    print("Bạn đã đoán đúng")
else:
    print("Số được máy tạo ra là: ", n)