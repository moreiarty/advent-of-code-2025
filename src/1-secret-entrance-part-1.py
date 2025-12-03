from utils import read_input


def main():
    instruction_arr = read_input("1-secret-entrance.txt")
    start_pos = 50
    zero_count = 0
    for instruction in instruction_arr:
        direction_str = instruction[:1]
        direction = "+" if direction_str == "R" else "-"
        delta = int(direction + instruction[1:])

        start_pos = (start_pos + delta) % 100
        if start_pos == 0:
            zero_count += 1
    print("password is", zero_count)


if __name__ == "__main__":
    main()
