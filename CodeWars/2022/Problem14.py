def main():
    translations = open("translations.txt").read()
    translations = translations.split("\n")[3:]
    y= {}
    n={}
    for line in translations:
        if line.split(":")[0] == 'Y':
            y[line.split(":")[1]] = line.split(":")[2]
        else:
            n[line.split(":")[1]] = line.split(":")[2]

    installed = input()
    so = input() == "YES"

    line = input()
    while line != "END":
        name = line.split(":")[0]
        message = line[line.index(":") + 2:]

        if name == installed:
            print(line)
        else:
            if so:

                # How to slip up the message into parts......
                yes = [message.find(yes) if message.find(no) > 0 for yes in y.keys()]
                no = [message.find(no) if message.find(no) > 0 for no in n.keys()]

                final_splitter = yes + no
                sorted(final_splitter)

                ## Split the message into these...


                if message in y.keys():
                    message = y[message]
                elif message in n.keys():
                    message = n[message]
            else:
                if message in n.keys():
                    message = n[message]
            print(name + ": " + message)
        line = input()


if __name__ == "__main__":
    main()
