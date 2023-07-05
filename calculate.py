import streamlit as st
from sympy import *

x, y, z = symbols("x y z")
c1 = 67.5*0.001
c2 = 25.9*0.001
c3 = 40*0.001
a = 82.03
b = 96.06
c = 110.09

st.header("计算小鼠短链脂肪酸的用量")
dosis = int(st.number_input("今天预计给每只小鼠短链脂肪酸的量(单位为ul)："))
amount = int(st.number_input("今天灌小鼠的数量(单位为只)："))

#dosis = int(input("今天预计给每只小鼠短链脂肪酸的量(单位为ul)："))
#number = int(input("今天灌小鼠的数量(单位为只)："))

# If button is pressed
if st.button("点击计算"):
  result1 = amount*solve(dosis*0.001*0.001*c1*a-x*0.001,x)[0]
  result2 = amount*solve(dosis*0.001*0.001*c2*b-y*0.001,y)[0]
  result3 = amount*solve(dosis*0.001*0.001*c3*c-z*0.001,z)[0]
  
  # Output prediction
  st.text(f"总共需要称取乙酸钠"+'{:.2f}'.format(result1)+"mg")
  st.text(f"总共需要称取丙酸钠"+'{:.2f}'.format(result2)+"mg")
  st.text(f"总共需要称取丁酸钠"+'{:.2f}'.format(result3)+"mg")
  
# print("总共需要称取乙酸钠",'{:.2f}'.format(result1),"mg")
# print("总共需要称取丙酸钠",'{:.2f}'.format(result2),"mg")
# print("总共需要称取丁酸钠",'{:.2f}'.format(result3),"mg")
