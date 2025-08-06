list = input("Nhap chuoi ki tu: ").split()

chuoi_kt = set()
for tu in list:
    for kt in tu:
        chuoi_kt.add(kt)

print(chuoi_kt)