from test_files.test import test_method_1, test_method_2


class MiddleMan:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def cool_method(self):
        test_method_1(self.a, self.b)

    def cooler_method(self):
        test_method_2(self.a, self.b, self.c, self.a)

    def other_method(self):
        temp = self.a + self.b
        print(temp)
