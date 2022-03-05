def main():
    n = int(input())

    player_hp = [11 + i for i in range(n)]

    i = 0
    out = 0
    out_indexes = []
    while out < len(player_hp) - 1:
        if player_hp[i] == 0:
            i += 1
            if i == len(player_hp):
                i = 0
            continue

        hp = player_hp[target(player_hp, i)] - player_hp[i]
        if hp <= 0:
            out += 1
            print(out)
            print(player_hp)
            if out == 1:
                out_indexes.append(target(player_hp,  i))
            if out == 10:
                out_indexes.append(target(player_hp,  i))
        player_hp[target(player_hp, i)] = max(0, hp)
        i += 1

        if i == len(player_hp):
            i = 0

    print(out_indexes[0] + 1)
    print(out_indexes[1])
    if i == 0:
        print(len(player_hp))
    else:
        print(i - 1)

def target(list, index):
    # Gets the maxium
    i = index + 1
    max_index = i + 1
    while i < len(list) + index:
        if list[i % len(list)] > list[max_index % len(list)]:
            max_index = i
        i += 1

    if max_index % len(list) == index:
        print("fuik1")

    return max_index % len(list)

if __name__ == "__main__":
    main()
