def main():
    n = int(input())
    for i in range(n):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabet = [x for x in alphabet]
        letters = {}
        for car in alphabet:
            letters[car] = 0

        total = 0
        num_sentences = int(input())
        for j in range(num_sentences):
            sentence = input()
            sentence = sentence.upper()
            for car in sentence:
                if car.isalpha():
                    letters[car] += 1
                    total += 1

        for letter in alphabet:
            print("{}: {:.2f}%".format(letter, 100 * letters[letter] / total))


if __name__ == "__main__":
    main()
