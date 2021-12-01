# This is a sample Python script.
def main():
    with open("") as f:
        text = f.read()

    n = text.split("\n")[0]


    text.split("\n") # Array of Strings
    text.split("\n")[1:] ## Gets the first and last elements

    line_x = [parse_line(line) for line in text.split("\n")[1:]]

    


# int int
# 1 2

def parse_line(line):
    return int(line.split(" ")[0]), int(line.split(" ")[1])


if __name__ == "__main__":
    main()
