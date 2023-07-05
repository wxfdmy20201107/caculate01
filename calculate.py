from sympy import *

x, y, z = symbols("x y z")
c1 = 67.5*0.001
c2 = 25.9*0.001
c3 = 40*0.001
a = 82.03
b = 96.06
c = 110.09

#请输入短链脂肪酸的量（单位为ul）
dosis = int(input("今天预计给每只小鼠短链脂肪酸的量（单位为ul）："))
number = int(input("今天灌小鼠的数量（单位为只）："))
result1 = number*solve(dosis*0.001*0.001*c1*a-x*0.001,x)[0]
result2 = number*solve(dosis*0.001*0.001*c2*b-y*0.001,y)[0]
result3 = number*solve(dosis*0.001*0.001*c3*c-z*0.001,z)[0]
print("总共需要称取乙酸钠",'{:.2f}'.format(result1),"mg")
print("总共需要称取丙酸钠",'{:.2f}'.format(result2),"mg")
print("总共需要称取丁酸钠",'{:.2f}'.format(result3),"mg")
