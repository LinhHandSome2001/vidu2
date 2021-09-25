import random
masv = random.randint(1, 99)
masv1 = "PXU" +str(masv)
hoten = input("Nhập họ tên: ")
ngaysinh = input("Nhập ngày sinh: ")
diemquatrinh = float(input("Nhập điểm quá trình: "))
diemthi = float(input("Nhập điểm thi: "))
diemtongket = ((diemthi + diemquatrinh)/2)

print (f"""
họ tên: {hoten}
mã sv: {masv1} 
ngày sinh {ngaysinh} 
điểm quá trình: {diemquatrinh}
điểm thi: {diemthi}
điểm tổng kết: {str(diemtongket)}
        """)
