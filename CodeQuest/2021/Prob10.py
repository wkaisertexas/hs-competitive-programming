def main():
    n = int(input())
    for i in range(n):
        line = input()

        function = line.split(" ")[0]
        if function == "formatHeight":
            print(f"{int(line.split(' ')[1])}\'{int(line.split(' ')[2])}\"")
        elif function == "formatDate":
            numbs = line.split(' ')[1:]
            y, m, d = int(numbs[0]), int(numbs[1]), int(numbs[2])
            print(f"{y}{format(m, '02d')}{format(d, '02d')}")
        else:

            res = ""
            words = line.split(" ")[1:]
            for word in words:
                res += word + ","
            print(res[:-1])


if __name__ == "__main__":
    main()
