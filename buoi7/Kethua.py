class Nhanvien:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Master(Nhanvien):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age
    def printphong(self):
        print(self.age)
        print(f"Quản lý phòng: {self.phong}")

nv = Master("Nguyễn","Lĩnh",20)
nv.printname()
nv.phong = 2
nv.printphong()