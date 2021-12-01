import os

os.system("python -m pip install numpy")
import numpy
def main():
    n = int(input())
    for i in range(n):
        line = input()
        c1, c2 = int(line.split(" ")[0]), int(line.split(" ")[1])
        line = input()
        c3, c4 = int(line.split(" ")[0]), int(line.split(" ")[1])
        line = input()
        f1, f2 = int(line.split(" ")[0]), int(line.split(" ")[1])

        c = [[c1, c2], [c3, c4]]
        c = numpy.matrix(c)
        c_i = numpy.linalg.inv(c)
        f = numpy.matrix([f1, f2])
        result = f * c_i
        x, y = result[0, 0], result[0, 1]
        print(round(x), round(y))


if __name__ == "__main__":
    main()
