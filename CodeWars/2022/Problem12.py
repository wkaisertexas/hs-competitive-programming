import math
def main():
    n_lines = int(input())

    req = input().split(' ')
    has = input().split(' ')

    # Find the max number of stuff he can build
    max_numb = max([math.ceil(int(has[i]) / int(req[i])) for i in range(len(has))])

    output = ""
    for i in range(len(has)):
        output += str(int(req[i]) * max_numb - int(has[i]))
        output += " "
    print(output[:-1])

if __name__ == "__main__":
    main()
