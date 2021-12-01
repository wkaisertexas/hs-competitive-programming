import math
class Date:
    def __init__(self, string):
        string = string.split("-")
        self.year = int(string[0])
        self.month = int(string[1])
        self.day = int(string[2])

    def to_int(self):
        return self.year * 365 + self.month * 31 + self.day

def main():
    n = int(input())

    for i in range(n):
        line = input()
        p = int(line.split(" ")[0])
        o = int(line.split(" ")[1])

        production = {}
        for j in range(p):
            line = input()
            production[Date(line.split(" ")[0]).to_int()] = int(line.split(" ")[1])
        distribution = {}
        for j in range(o):
            line = input()
            distribution[Date(line.split(" ")[0]).to_int()] = int(line.split(" ")[1])

        k = 0
        planes = 0
        good = False

        dist_keys = [key for key in distribution.keys()]
        for x in production.keys():
            while (dist_keys)[k] <= x and not good:
                planes -= distribution[dist_keys[k]]
                k += 1
                if k == len(dist_keys):
                    good = True
            planes += production[x]

        if planes > 0:
            print ("OK")
        else:
            print("NOT OKAY")

if __name__ == "__main__":
    main()
