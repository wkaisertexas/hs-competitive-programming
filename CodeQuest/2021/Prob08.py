import math


def main():
    n = int(input())
    for i in range(n):
        line = input()
        x, y = int(line.split(" ")[0]), int(line.split(" ")[1])

        squared_sum = 0
        for j in range(x):
            line = input()
            for k in line.split(" ")[:]:
                squared_sum += abs(int(k)) ** 2

        n = math.sqrt(squared_sum)
        print("{:.2f}".format(n))


if __name__ == "__main__":
    main()
