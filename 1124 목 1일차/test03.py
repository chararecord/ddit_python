# 홀/짝을 넣으세요 >> 홀
# 나 : 홀 (짝)
# 컴 : 짝 (홀)
# 결과 : 졌음 (이겼음)
import random

a = input("홀/짝을 넣으세요 >> ")
b = random.random()
c = ""

if b < 0.5 :
    c = "홀"
else:
    c = "짝"

print("나 : {}".format(a))
print("컴 : {}".format(c))

if a == c :
    print("결과 : 이겼음")
else :
    print("결과 : 졌음")