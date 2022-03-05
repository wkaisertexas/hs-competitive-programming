
def main():
    n_lines = int(input())

    total_min = 0
    total_sec = 0
    for i in range(n_lines):
        time = input()
        min, sec = time.split(":")
        total_min += int(min)
        total_sec += int(sec)

    total_min += total_sec // 60
    total_sec = total_sec% 60
    print(f"{total_min}:{total_sec:02d}")

if __name__ == "__main__":
    main()
