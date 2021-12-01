import math
def main():
    n = int(input())
    for i in range(n):
        numb_asteroids = int(input())

        points = {}
        for j in range(numb_asteroids):
            line = input()
            x, y = int(line.split(" ")[0]), int(line.split(" ")[1])
            dist = math.sqrt(x * x + y * y)
            points[dist] = (x, y)

        for j in sorted(points.keys()):
            print(points[j][0], points[j][1])


if __name__ == "__main__":
    main()
