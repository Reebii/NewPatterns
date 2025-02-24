from turtle import *
import colorsys

bgcolor("black")
tracer(10)  # Adjusted for better performance

def draw():
    h = 0

    for i in range(75):
        c = colorsys.hsv_to_rgb(h, 1, 1)   
        c = "#{:02x}{:02x}{:02x}".format(
            int(c[0] * 255), int(c[1] * 255), int(c[2] * 255)
        )   

        h += 0.02   

        up()
        goto(0, 0)
        down()

        color("black")
        fillcolor(c)   

        begin_fill()
        rt(98)
        circle(i, 12)
        fd(150)  #  kam hai ab spacing
        lt(29)

        for j in range(20):  #  yeh loop circle ko adjusted rakhega
            fd(i // 2)
            circle(j, 180, steps=2)

        end_fill()

draw()
done()
