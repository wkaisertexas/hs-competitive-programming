def main():
    n = int(input())
    for x in range(n):
        line = input()
        style = line.split(" ")[1]
        number = line.split(" ")[0]

        if style == "PARENTHESES":
            print(f"({number[0:3]}) {number[3:6]}-{number[6:]}")
        elif style == "DASHES":
            print(f"{number[0:3]}-{number[3:6]}-{number[6:]}")
        else:
            print(f"{number[0:3]}.{number[3:6]}.{number[6:]}")


if __name__ == "__main__":
    main()
