from turtle import *

args = {(-126,162):65,(-58,55):65,(-58,-48):65,(-126,-162):65,(-300,50):120}
bgcolor("red")
setup(800,500)
speed(10)

def star(tuples,size):
    up()
    color("yellow", "yellow")
    goto(tuples[0],tuples[1])
    begin_fill()
    for i in range(5):
        forward(size)
        right(144)
    end_fill()
    up()
    goto(0,0)


if __name__ == '__main__':
    
    for key,value in args.items():
        star(key,value)

 
