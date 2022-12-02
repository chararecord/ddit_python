# 출력할 단수를 넣으세요 4
# 4*1 = 4
# 4*2 = 8

#나
dan = int(input("출력할 단수를 넣으세요 >> "))
sum = 0;

for i in range(1,10) :
    sum = dan * i
    print("{}*{}={}".format(dan,i,sum))
    
#################################################
#쌤

dann = input("출력할 단수를 넣으세요")
idann = int(dan)
print("{}*{}={}".format(idann,1,idann*1))
print("{}*{}={}".format(idann,2,idann*2))
print("{}*{}={}".format(idann,3,idann*3))
print("{}*{}={}".format(idann,4,idann*4))
print("{}*{}={}".format(idann,5,idann*5))
print("{}*{}={}".format(idann,6,idann*6))
print("{}*{}={}".format(idann,7,idann*7))
print("{}*{}={}".format(idann,8,idann*8))
print("{}*{}={}".format(idann,9,idann*9))