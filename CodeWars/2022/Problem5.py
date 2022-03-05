def main():
    decimal = str(input())
    number = float(decimal)

    last = int(decimal[-1])
    if last == 7:
        number += 0.02
    elif last % 2 == 1:
        number -= 0.09
    elif last > 7:
        number -= 4
    elif last < 4:
        number += 6.78

    print(f"{number:.2f}")



if __name__ == "__main__":
    main()
