class Circle:
    ID = 0
    radius = 0
    color = ""
    display = True

##Constructor
    def __init__(self,id,r,c,d):
        self.ID = id
        self.radius = r
        self.color = c
        self.display = d
### Method ( function.. )
    def circumfrence(self):
        return 3.141 * 2 * self.radius


circle1 = Circle(1,10,"blue",True)
circle2 = Circle(2,16,"red",True)
circle3 = Circle(3,223,"pink",False)


print("Circumfrence of Circle 1 is :", circle1.circumfrence())
print("Circumfrence of Circle 2 is :", circle2.circumfrence())
print("Circumfrence of Circle 3 is :", circle3.circumfrence())


