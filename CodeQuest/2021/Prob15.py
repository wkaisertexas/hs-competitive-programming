import math


def check_good(cloud_thickness, speed, angle):
    if cloud_thickness > 1000:
        return False
    NS = speed * math.sin(math.radians(angle))
    WE = speed * math.cos(math.radians(angle))
    if abs(NS) > 40 or abs(WE) > 20:
        return False
    return True


def main():
    n = int(input())
    for i in range(n):
        n_times = int(input())
        bad = True
        for j in range(n_times):
            line = input()
            cloud_thickness = int(line.split(" ")[2])
            speed = float(line.split(" ")[3])
            angle = int(line.split(" ")[4])

            if check_good(cloud_thickness, speed, angle):
                print(line[:line.find(":") + 3])

                for k in range(j + 1, n_times):
                    input()
                bad = False
                break
        if bad:
            print("ABORT LAUNCH")


if __name__ == "__main__":
    main()
