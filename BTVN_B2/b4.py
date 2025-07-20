n = int(input("Nhập số N xu bạn có: "))
chai_bia = n // 28
dem = chai_bia

while dem >= 3:
    doi_duoc = dem // 3
    chai_bia += doi_duoc
    dem = dem % 3 + doi_duoc
print ("Số chai bia có thể mua được: ", chai_bia)     