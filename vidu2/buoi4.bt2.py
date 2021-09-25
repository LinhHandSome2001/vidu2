import random
danhsach = {}

for i in range(10):
    so = random.randint(1, 10)
    danhsach.update({str(i + 1) : so})
    i += 1 

print(danhsach)