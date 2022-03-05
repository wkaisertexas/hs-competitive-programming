def main():
    number = input()

    numb_digits = len(number) - 1

    zeros_to_prefix = {
        0: '',
        1: 'deca',
        2: 'hecto',
        3: 'kilo',
        6: 'mega',
        9: 'giga',
        12: 'tera',
        15: 'peta',
        18: 'exa',
        21: 'zetta',
        24: 'yotta',
        27: 'bronto',
        30: 'gego'
    }

    numbers = []

    numb_to_words = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine"
    }

    #print(numb_digits)
    while numb_digits >= 0 and int(number) != 0:
        # Finds the closets number of digits
        leading_digit = int(number) // (10 ** numb_digits)

        number = str(int(number) - leading_digit * 10 **( numb_digits ))
        #print(number)
        #print(leading_digit)
        numbers.append(str(numb_to_words[leading_digit]) + " " + zeros_to_prefix[numb_digits] + "bytes")
        numb_digits = len(number) - 1
        if leading_digit == 0:
            continue

    output = ""

    # print(numbers)
    for number in numbers:
        output += number + ", "
    output = output[:-2]
    #print(output)

    # Cut out the last comma
    removed = len(output) - output[::-1].find(" ,")

    # print(removed)
    output = output[:removed - 2] + " and " + output[removed:]
    print(output)

if __name__ == "__main__":
    main()
