def main():
    n = int(input())

    for i in range(n):
        line = input()
        h = int(line.split(" ")[0])
        w = int(line.split(" ")[1])
        matrix = []
        for j in range(h):
            line = input()
            row = []
            for k in range(len(line.split(","))):
                row.append(line.split(",")[k])
            matrix.append(row)
        ## Prints Stuff
        print_string = ""
        for j in range(len(matrix[0])):
            for k in range(len(matrix)):
                print_string += matrix[k][j] + ","
            print(print_string[:-1])
            print_string = ""


if __name__ == "__main__":
    main()
