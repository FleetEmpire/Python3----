import turtle
t = turtle.Turtle()# 创建对象
#创建车身
t.pencolor("red")
t.speed(4)
t.up()
t.fd(100)
t.down()
t.fillcolor("red")
t.begin_fill()
t.fd(100)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(300)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(50)
t.lt(30)
t.fd(100)
t.rt(30)
t.fd(50)
t.goto(150,0)
t.end_fill()

#绘制后车轮
t.up()
t.goto(100,-90)
t.down()
t.fillcolor("black")
t.begin_fill()
t.circle(20)
t.end_fill()

#绘制前车轮
t.up()
t.goto(0,-90)
t.down()
t.fillcolor("black")
t.begin_fill()
t.circle(20)
t.end_fill()


















