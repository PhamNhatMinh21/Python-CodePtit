class Rectangle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color.capitalize()
    def check(self):
        if self.x <= 0 or self.y <= 0:
            return 0
        return 1
    def __str__(self):
        if self.check() == 1:
            return f'{(self.x + self.y) * 2} {self.x * self.y} {self.color}'
        else:
            return 'INVALID'
a = input().split()
rec = Rectangle(int(a[0]), int(a[1]), (a[2]))
print(rec)
