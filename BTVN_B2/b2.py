x =int(input("Nhập lương của ng đó: "))
if(x >= 15000000):
    print ("Thuế: ", x*0.3) 
    print("Thu nhâp: ", x - x*0.3)
elif(7000000 < x < 15000000):
    print ("Thuế: ", x*0.2) 
    print ("Thu nhâp: ", x - x*0.2)
else:
    print ("Thuế: ", x*0.1) 
    print ("Thu nhâp: ", x - x*0.1)