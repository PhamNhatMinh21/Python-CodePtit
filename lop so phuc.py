class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
    def __add__(self, x):
        return SoPhuc(self.thuc + x.thuc, self.ao + x.ao)
    def __mul__(self, x):
        thuc = self.thuc * x.thuc - self.ao * x.ao
        ao = self.thuc * x.ao + self.ao * x.thuc
        return SoPhuc(thuc, ao)
    def __pow__(self, power):
        thuc = self.thuc**2 - self.ao**2
        ao = 2 * self.thuc * self.ao
        return SoPhuc(thuc, ao)

    def __str__(self):
        if self.ao >= 0:
            return f"{self.thuc} + {self.ao}i"
        else:
            return f"{self.thuc} - {-self.ao}i"
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    x = SoPhuc(a, b)
    y = SoPhuc(c, d)
    C = (x + y) * x
    D = (x + y) ** 2
    print(f'{C}, {D}')