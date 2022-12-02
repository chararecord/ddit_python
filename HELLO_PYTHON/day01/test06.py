# 가위/바위/보를 넣으세요
# 나 : 가위
# 컴 : 가위
# 결과 : 비김

#나
from random import random

me = input("가위/바위/보를 입력하세요 >> ")
com1 = ["가위", "바위", "보"]
rst = ""

com2 = com1[int(random()*3)]

if (me == "가위" and com2 == "바위") or (me == "바위" and com2 == "보") or (me == "보" and com2 == "가위") :
    rst = "컴퓨터승리"
elif me == com2 :
    rst = "비김"
else :
    rst = "나의승리"

print("나 >> ", me)
print("컴 >> ", com2)
print("결과는? ", rst)

###########################################################
#쌤
mine = input("가위/바위/보를 입력하세요 >> ")
com = ""
result = ""

rnd = random.random()

if com == "가위" and mine == "가위" : result = "비김"
if com == "바위" and mine == "바위" : result = "비김"
if com == "보" and mine == "보" : result = "비김"

if com == "가위" and mine == "바위" : result = "이김"
if com == "바위" and mine == "보" : result = "이김"
if com == "보" and mine == "가위" : result = "이김"

if com == "가위" and mine == "보" : result = "짐"
if com == "바위" and mine == "가위" : result = "짐"
if com == "보" and mine == "바위" : result = "짐"

print("나 >> ", mine)
print("컴 >> ", com)
print("결과는? ", result)