def decode(message):
    first_4 = message[:4]

    first = add_ordinals(message[0], message[-1])
    second = add_ordinals(message[1], message[0])
    third = add_ordinals(message[2], message[1])
    fourth = add_ordinals(message[3], message[2])

    fifth = add_ordinals(message[-4], message[-5])
    sixth = add_ordinals(message[-3], message[-4])
    seventh = add_ordinals(message[-2], message[-3])
    eight = add_ordinals(message[-1], message[-2])

    new_message = ""

    new_message += convert_to_char(first)
    new_message += convert_to_char(second)
    new_message += convert_to_char(third)
    new_message += convert_to_char(fourth)
    new_message += convert_to_char(fifth)
    new_message += convert_to_char(sixth)
    new_message += convert_to_char(seventh)
    new_message += convert_to_char(eight)

    return new_message

def add_ordinals(ord1, ord2):
    sum = ord(ord1) + ord(ord2)

    while sum < 97:
        sum += ord(ord2)
    return sum

def convert_to_char(num):
    while num > 122:
        num -= 26
    return chr(num)

def main():
    message = input()
    sig = input()

    decoded = decode(message)
    if decoded == sig:
        print(f"{sig} equals {sig}")
        print("Gru")
    else:
        print(f"{decoded} does not equal {sig}")
        print("Not Gru")

if __name__ == "__main__":
    main()
