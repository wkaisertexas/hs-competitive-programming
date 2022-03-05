def main():
    lines = input()

    output = ""

    for code in lines.split(","):
        line = input()
        code = code.replace("[", "").replace("]", "")

        for op in code.split(";"):
            if op.find("-") > 0:
                start = op.split("-")[0]
                start = int(start)
                end = op.split("-")[1]
                end = int(end)
                output += line[start - 1:end]
            elif op.find("-") == 0:
                output += line[int(op)]
            else:
                if int(op) == 0:
                    continue
                output += line[int(op) - 1]

    print(output)




if __name__ == "__main__":
    main()
