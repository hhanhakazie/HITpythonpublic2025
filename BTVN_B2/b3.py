n = int(input("Nhập số nguyên: "))
bien = n
dem = 0
tong = 0

if bien == 0:
    dem ==1
    tong == 0
else:
    while bien > 0:
        chu_so = bien % 10
        tong += chu_so
        dem += 1
        bien //= 10
    
print("Số chữ số: ", dem, "Tổng chữ số: ", tong)