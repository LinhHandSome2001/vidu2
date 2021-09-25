sanpham = {
    "thuonghieu": "Apple",
    "sacnhanh": True,
    "namsx": 2021,
    "mausac": ["Do", "Vang","Den"]
}

print(sanpham)
print(sanpham["thuonghieu"])
print(sanpham.keys())

sanpham.update({"thuonghieu": "lenovo"})
sanpham.update({"cannag": "1.2kg"})
print(sanpham)