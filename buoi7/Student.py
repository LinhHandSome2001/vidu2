class Student:
    def __init__(self, name="Nguyễn Hồng Lĩnh", age=21):
        self.name = name
        self.age = age
    def printInfo(self):
        print(f"Họ và tên: {self.name}")
        print(f"Tuổi: {self.age}")
        

sc = Student()
sc.printInfo()
sc.name = "Nguyễn Hồng Lĩnh"
sc.printInfo()

del sc.age