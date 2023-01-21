import turtle
import draw_enhanced as draw
import math


def main():

    # draw the all shapes to test their behaviour
    
    shape_list = []         # a list to collect all the shapes. 
    myCanvas = draw.Canvas(500, 500)
    
    line1 = draw.Line(draw.Point(-100, -100), draw.Point(100, 100))
    line1.setWidth(4)
    shape_list.append(line1)

    line2 = draw.Line(draw.Point(-100, 100), draw.Point(100, -100))
    shape_list.append(line2)


    t1 = draw.Triangle([draw.Point(-50,-50), draw.Point(-20,50), draw.Point(80,50)])
    t1 = draw.Triangle([draw.Point(-150,-50), draw.Point(0,50), draw.Point(50,0)])
    t1.setWidth(2)
    t1.setColor('green')
    shape_list.append(t1)

    t1 = draw.Triangle([draw.Point(50,-50), draw.Point(150,-50), draw.Point(50,-20)])
    t1.setWidth(2)
    t1.setColor('red')
    shape_list.append(t1)
        
    r1 = draw.Rectangle(draw.Point(0,0),25,150,75)
    r1.setWidth(2)
    r1.setColor('blue')
    shape_list.append(r1)
  
    r2 = draw.Rectangle(draw.Point(100,0),100,140)
    shape_list.append(r2)
    
    o1 = draw.Octagon([draw.Point(-200,30),draw.Point(-140,80),draw.Point(150,30),draw.Point(200,0),
                       draw.Point(160,-60),draw.Point(0,-30),draw.Point(-150,0),draw.Point(-200,20)])
    o1.setWidth(3)
    o1.setColor('yellow')

    shape_list.append(o1)
    
    # draw all shapes in the list   
    for sh in shape_list:
        myCanvas.draw(sh)

    line1.setColor('red')
    line2.setWidth(4)
    line2.setColor('green')
    turtle.done()

    return

if __name__ == "__main__":
    main()
  