def main():
    numer, den = input().split("/")
    numer = int(numer)
    den = int(den)

    result = numer // den
    remainder = numer % den

    print(f"{result:8d} R {remainder:2d}")

    print("   ___________")
    print(f"{den}|{numer}")

    curr = numer
    i = 0
    while curr >= den:
        curr -= den

        while str(result)[0] == " ":
            if len(str(result)) == 1:
                break
            result = str(result)[1:]

        subtractor = fasdf
        print("  " + i * " " + "-" + str(number))
        print(f"   {i*' '}{asdfasdkl;fj:0.xd}")

        curr -= subtractor


if __name__ == "__main__":
    main()
