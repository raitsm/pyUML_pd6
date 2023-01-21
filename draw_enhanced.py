from abc import *
from abc import *
import turtle
import math


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

    @abstractmethod
    def _draw(self):
        pass



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
    
    def setCoordinates(self,x,y):
        self.__coordinates(x,y)
    
    def _draw(self, turtle):
        # turtle.goto(self.__x, self.__y)
       # turtle.dot(self.__lineWidth, self.__lineColor)
        turtle.goto(self.__coordinates[0], self.__coordinates[1])
        turtle.dot(self.getWidth(), self.getColor())
    
    def __eq__(self, other):
        return self.getCoord() == other.getCoord()

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
        # check if any corners are 
        t = corners[0]
        # check if all corners have different coordinates
        for i in range(1,len(corners)-1):
            if t == corners[i]:
                raise ValueError("Polygon: One or more corners have same coordinates")
            else:
                t = corners[i]
        if not self.__isconvex(corners):
            raise ValueError("Polygon: Must be a convex shape.")
        super().__init__()
        self.__corners = corners

    def __isconvex(self, corners) -> bool:
    # checks if the polygon is convex
    # not implemented yet    
        return True
    
    def _draw(self, turtle):
        # print("****")
        turtle.color(self.getColor())
        turtle.width(self.getWidth())
        turtle.up()
        k = 0
        start_point = (self.__corners[0].getCoord())
        for c in self.__corners:
            turtle.goto(c.getX(),c.getY()) # (c.getCoord())
            turtle.down()
            # turtle.dot(8,"red")
            # k += 1
            # print(k, c.getCoord())
            # print(turtle.xcor(), turtle.ycor())
        turtle.goto(self.__corners[0].getX(), self.__corners[0].getY())  #start_point)            
        # print(turtle.xcor(), turtle.ycor())
        turtle.up()

    def getAllCorners(self) -> list:
        return self.__corners
    
    def setAllCorners(self, corners : list):
        if len(corners) != len(self.__corners):
            raise ValueError("Polygon: number of corners must stay unchanged")
        self.__corners = corners        
    
    def getCornerN(self, corner_number) -> Point:
        # retrieves coordinates of a corner N for an X-corner polygon. N must be between 1 and X.
        if corner_number <= 0 or corner_number > len(self.__corners):
            raise ValueError("Polygon: corner number out of range. The values must be within 1 and "+str(len(self.__corners))+".")
        else:
            return self.__corners[corner_number-1]

    def setCornerN(self, corner_number, new_point : Point):
        # sets coordinates of a corner N for an X corner polygon. N must be between 1 and X.
        if corner_number <= 0 or corner_number > len(self.__corners):
            raise ValueError("Polygon: corner number out of range. The values must be within 1 and "+str(len(self.__corners))+".")
        else:
            self.__corners[corner_number-1] = new_point
        

class Triangle(Polygon):
    # A convenience class for Triangle
    # __init__ takes a list of three items of Point type to define a triangle

    # Limitations: 
    # a) There is no check if all three corners are on the same line
    
    def __init__(self, corners : list):
        if len(corners) != 3:
            raise ValueError("Triangle: wrong number of corners. must be three.")
        else:
            super().__init__(corners)

class Rectangle(Polygon):
    # A convenience class for rectangles
    # the __init__ takes: 
    # a) the coordinates of the lower-left corner through a Point object
    # b) width (horizontal length) and height (vertical length) of the rectangle
    # c) rotation angle (optional, 0 if not specified)
    def __init__(self, ll: Point, width : int, height : int, rotation_angle = 0):
        if width <= 0 or height <= 0:
            raise ValueError("Rectangle: Height or width cannot be zero.")
        else:
        # proceed building the rectangle
            corners = [ll]      # add lower left corner to the rectangle
            corners.append(Point(ll.getX() + width, ll.getY()))   # add lower right (x + width, same height)
            corners.append(Point(ll.getX() + width, ll.getY() + height)) # add upper right (x + width, y + height)
            corners.append(Point(ll.getX(), ll.getY() + height))
            if rotation_angle != 0:
                corners = self.__rotate(corners, rotation_angle)
            print(len(corners))
            super().__init__(corners)

    def __rotate(self, corner_array : list, angle ) -> list:
    # the rotation angle shall be specified in degrees
    # get x and y for LL corner:
        x_base = corner_array[0].getX()
        y_base = corner_array[0].getY()

        for n in range(1,len(corner_array)):
            x_current = corner_array[n].getX()
            y_current = corner_array[n].getY()
            
            r = math.sqrt((x_current - x_base)**2 + (y_current - y_base)**2)

            # calculate base angle
            if x_current == x_base:
                base_angle = 90     # straight angle
            else:
                base_angle = math.degrees(math.atan((y_current - y_base) / (x_current - x_base)))
            # the actual rotation angle will be base angle plus rotation angle            
            x_new = x_base + r * math.cos(math.radians(angle + base_angle))
            y_new = y_base + r * math.sin(math.radians(angle + base_angle))
            del corner_array[n]
            corner_array.insert(n,Point(x_new, y_new))
        return corner_array


class Octagon(Polygon):
    
    def __init__(self, corners: list):
        # check if number of corners is 8
        if (len(corners) !=8):
            raise ValueError("Rectangle: wrong number of corners. Eight corners expected.")
        else:
            super().__init__(corners)
        
