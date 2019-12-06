def multiply(x):
    def calculate(y):
        return x * y
    return calculate


if __name__ == '__main__':
    double = multiply(2)
    triple = multiply(3)
    print(double, triple)
    print(f'A double of 7 is {double(7)}')
    print(f'A triple of 3 is {triple(3)}')
