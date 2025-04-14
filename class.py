class Point:
    def move(self):
        print('move')
    def draw(self):
        print("draw")


point1 = Point()
print(point1.draw())
point1.x = 100
print(point1.x)
