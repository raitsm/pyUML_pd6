from abc import *
from abc import *
import turtle

class Canvas:
    def __init__(self, w, h):
        self.__visibleObjects = []   #list of shapes to draw
        self.__turtle = turtle.Turtle()
        self.__screen = turtle.Screen()
        self.__screen.setup(width = w, height = h)
        self.__turtle.hideturtle()

    def drawAll(self):
        self.__turtle.reset()
        self.__turtle.up()
        self.__screen.tracer(0)
        for shape in self.__visibleObjects: #draw all shapes in order
            shape._draw(self.__turtle)
        self.__screen.tracer(1)
        self.__turtle.hideturtle()

    def addShape(self, shape):
        self.__visibleObjects.append(shape)

    def draw(self, gObject):
        gObject.setCanvas(self)
        gObject.setVisible(True)
        self.__turtle.up()
        self.__screen.tracer(0)
        gObject._draw(self.__turtle)
        self.__screen.tracer(1)
        self.addShape(gObject)


class GeometricObject(ABC):
    def __init__(self):
        self.__lineColor = 'black'
        self.__lineWidth = 1
        self.__visible = False
        self.__myCanvas = None

    def setColor(self, color):  #modified to redraw visible shapes
        self.__lineColor = color
        if self.__visible:
            self.__myCanvas.drawAll()

    def setWidth(self, width):  #modified to redraw visible shapes
        self.__lineWidth = width
        if self.__visible:
            self.__myCanvas.drawAll()

    def getColor(self):
        return self.__lineColor

    def getWidth(self):
        return self.__lineWidth

    @abstractmethod
    def _draw(self):
        pass

    def setVisible(self, vFlag):
        self.__visible = vFlag

    def getVisible(self):
        return self.__visible

    def setCanvas(self, theCanvas):
        self.__myCanvas = theCanvas

    def getCanvas(self):
        return self.__myCanvas


# Added from the textbook
# Shape can set & get its FillColor
class Shape(GeometricObject):
    def _init_(self):
        super().__init_()
        self.__fillColor = None
        
    def setFillColor(self, aColor): 
        self.__fillColor = aColor
        if self.getVisible():
            self.getCanvas().drawAll()

    def getFillColor(self):
        return self.__fillColor


# coords parameter for Point class is a tuple (x,y)
class Point(GeometricObject):
    def __init__(self, x, y):
        super().__init__()
        # self.__x = x
        # self.__y = y
        self.__coordinates = (x,y)

    def getCoord(self):
        # return (self.__x, self.__y)
        return self.__coordinates

    def getX(self):
        # return self.__x
        return self.__coordinates[0]

    def getY(self):
        # return self.__y
        return self.__coordinates[1]
    
    def _draw(self, turtle):
        # turtle.goto(self.__x, self.__y)
       # turtle.dot(self.__lineWidth, self.__lineColor)
        turtle.goto(self.__coordinates[0], self.__coordinates[1])
        turtle.dot(self.getWidth(), self.getColor())

class Line(GeometricObject):
    def __init__(self, p1, p2):
        super().__init__()
        self.__p1 = p1
        self.__p2 = p2

    def getP1(self):
        return self.__p1

    def getP2(self):
        return self.__p2

    def _draw(self, turtle):
        turtle.color(self.getColor())
        turtle.width(self.getWidth())
        turtle.up()
        turtle.goto(self.__p1.getCoord())
        turtle.down()
        turtle.goto(self.__p2.getCoord())




class Polygon(Shape):
    # parameters: vertices (list of tuples)
    #
    def __init__(self, corners : list):
        super(Polygon,self).__init__()
        self.__corners = corners
    
    def _draw(self, turtle):
        turtle.color(self.getColor())
        turtle.width(self.getWidth())
        turtle.up()
        start_point = (self.__corners[0].getCoord())

        for c in self.__corners:
            turtle.goto(c.getCoord())
            turtle.down()
        turtle.goto(start_point)            
        turtle.up()

class Triangle(Polygon):
    def __init__(self, corners : list):
        if len(corners) != 3:
            raise ValueError("Triangle: wrong number of corners. must be three.")
        else:
            super(Triangle,self).__init__(corners)

class Rectangle(Polygon):
    pass

class Octagon(Polygon):
    pass

    



def test2():
    myCanvas = Canvas(500, 500)
    line1 = Line(Point(-100, -100), Point(100, 100))
    line2 = Line(Point(-100, 100), Point(100, -100))
    # line1.setWidth(4)    
    myCanvas.draw(line1)
    myCanvas.draw(line2)
    line1.setColor('red')
    line2.setWidth(4)
    t1 = Triangle([Point(-50,-50), Point(50,50), Point(50,0)])
    t1.setWidth(2)
    t1.setColor('yellow')
    myCanvas.draw(t1)
    turtle.done()

