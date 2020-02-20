class Circle:
    radius = 0

    def __init__(self,r):
        self.radius = r
    
    def circumfrence(self):
        return 3.141 * 2 * self.radius


circleA = Circle(8)
circleB = Circle(22.5)
circleC = Circle(11)

print("Circle A Circumfrance: ", circleA.circumfrence())
print("Circle B Circumfrance: ", circleB.circumfrence())
