class Cyclomatic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def test_function(self):
        if self.a == 1:
            return self.a
        if self.a == 1 and self.b == 1 or self.c == 1 and self.c != 0:
            return self.a
        elif self.b == 1 or self.c == 1:
            return self.b
        elif self.c == 1 or self.a == 1:
            return self.c

        for i in range(0, 10):
            if i == 1:
                print(i)
            elif i == 2:
                print(i)
            elif i == 3:
                print(i)
            elif i == 4:
                print(i)
            elif i == 5:
                print(i)
            elif i == 6:
                print(i)
            elif i == 7:
                print(i)
            elif i == 8:
                print(i)
            elif i == 9:
                print(i)
            elif i == 10:
                print(i)

        for i in range(0, 10):
            if i == 1:
                print(i)
            elif i == 2:
                print(i)
            elif i == 3:
                print(i)
            elif i == 4:
                print(i)
            elif i == 5:
                print(i)
            elif i == 6:
                print(i)
            elif i == 7:
                print(i)
            elif i == 8:
                print(i)
            elif i == 9:
                print(i)
            elif i == 10:
                print(i)
