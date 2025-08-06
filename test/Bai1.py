n = input("Nhap day so: ")
so = tuple(map(int, n.split()))  

count = {}
for x in so:
    count[x] = count.get(x, 0) + 1

for x in count:
    if count[x] % 5 == 0 and count[x] % 10 != 0:
        print(x, end=' ')