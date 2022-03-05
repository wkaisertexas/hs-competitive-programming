def main():

    line = input()
    while line != "END":
        ending_punc = line[-1]

        vowels = "aeiou"
        final = ""
        for word in line[:-1].split(" "):
           # print(word[0])
            if vowels.find(word[0].lower()) != -1:
                final += word+"-m"
            else:
                final += word[1:] + word[0] + "-squeak"
            final += " "
        print(final[:-1 ] + ending_punc)
        line = input()


if __name__ == "__main__":
    main()
