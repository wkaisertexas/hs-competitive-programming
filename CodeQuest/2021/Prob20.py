import math


def main():
    n = int(input())

    for i in range(n):
        line = input()
        x0 = float(line.split(' ')[0])
        y0 = float(line.split(' ')[1])
        h = float(line.split(' ')[2])
        itererations = int(line.split(' ')[3])

        for j in range(itererations):
            y0 += math.sin(x0) / x0 * h
            x0 += h
        print(round(y0, 3))


if __name__ == "__main__":
    main()
