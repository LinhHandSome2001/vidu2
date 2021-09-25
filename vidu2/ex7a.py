tongtien = int(input("Số tiền đã nộp: "))
songuoidonggop = 0
while tongtien <= 100000:
    donggop = int(input("Mời bạn góp tiền uống cà phê: "))
    tongtien += donggop

    if tongtien > 100000: continue
    songuoidonggop += 1
else:
    print("Bạn đã nộp đủ tiền, không cần đóng nữa")
    
print("Đã đủ tiền để đóng: {}k vnđ, đang có {} người đóng góp".format(tongtien/1000, songuoidonggop))