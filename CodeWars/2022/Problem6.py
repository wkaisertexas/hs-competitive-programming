import sys

def main():
    f = open('input.txt', 'r')
    lines = f.readlines()

    i = 0
    while i < len(lines) - 2:
        p = int(lines[i])
        r = float(lines[i + 1])
        t = int(lines[i + 2])
        print(f"{p * r * t:.2f}")
        i += 3

if __name__ == "__main__":
    main()
