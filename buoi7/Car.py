class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
    def old(self):
        print(f"Hãng: {self.make}")
        print(f"Phiên bản: {self.model}")
        return 2022 - self.year

mycar = Car(2021, "Mazda", "Mazda2 - Sport")
print("My car is {} year old".format(mycar.old()))

del mycar.model