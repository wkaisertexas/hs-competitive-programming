def main():
    max = 0
    n = int(input())
    for x in range(n):
        line = input()
        for num in line.split(" "):
            if int(num) > max:
                max = int(num)
        print(max)
        max = 0


if __name__ == "__main__":
    main()