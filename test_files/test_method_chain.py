class Calc:
    def __init__(self, n):
        self.n = n

    def add(self, n):
        self.n += n
        return self

    def sub(self, n):
        self.n -= n
        return self


if __name__ == "__main__":
    num = Calc(5)
    result = num.add(5).add(5).add(5).sub(5)
    print(result.n)
