from turtle import *
bgcolor("black")
color = ["red","yellow","blue","white","green","purple"]
for i in range(10,300,7):
    pencolor(color[i%6])
    fd(i)        
    lt(216)  
