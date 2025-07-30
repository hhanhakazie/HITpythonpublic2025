# Nhập số lượng phần tử
n = int(input("Nhập số phần tử n: "))

# Khởi tạo list rỗng và nhập giá trị
list1 = []
for i in range(n):
    list1.append(int(input(f"Phần tử thứ {i}: ")))

# Nhập số X và đếm số lần xuất hiện
X = int(input("Nhập số X: "))
count_X = list1.count(X)
print(f"Số {X} xuất hiện {count_X} lần trong list.")

# Check list đủ dài để thay thế từ vị trí 2 đến 7
if len(list1) >= 8:
    list1[2:8] = [8, 5, 4, 0, 1, 3]
else:
    print("List không đủ dài -> thêm giá trị 0 vào cuối để đủ độ dài")
    while len(list1) < 8:
        a.append(0)
    list1[2:8] = [8, 5, 4, 0, 1, 3]

# In list sau khi thay thế
print("List sau khi thay thế:", list1)

# Tìm số lớn nhất và nhỏ nhất
print ("Số lớn nhất trong list: ", max(list1))
print ("Số nhỏ nhất trong list: ", min(list1)) 

# Nhập số Y và chèn vào đầu list
Y = int(input("Nhập số Y: "))
list1.insert(0, Y)
print("List sau khi chèn Y vào đầu:", list1)

# Kiểm tra list có sắp xếp tăng, giảm hay không
if list1 == sorted(list1):
    print("TĂNG")
elif list1 == sorted(list1, reverse=True):
    print("GIẢM")
else:
    print("NO")