def caeser(char, shift, direction):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    loc = alphabet.find(char.upper())

    if direction == 1:
        # to the left
        loc = (loc - shift + 26) % 26
    else:
        # to the right
        loc = (loc + shift + 26) % 26
    return alphabet[loc]


def main():
    n = int(input())
    for i in range(n):
        cypher = input()

        shift = [int(x) for x in input().split(" ")]
        dir = [int(x) for x in input().split(" ")]

        shift_key = 0
        dir_key = 0

        new_string = ""
        for char in cypher:
            if char.isalpha():
                new_string += caeser(char, shift[shift_key], dir[dir_key])
                dir_key += 1
                shift_key += 1
                if dir_key == len(dir):
                    dir_key = 0
                if shift_key == len(shift):
                    shift_key = 0
            else:
                new_string += char
        print(new_string.lower())


if __name__ == "__main__":
    main()
