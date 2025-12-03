from utils import read_input


def main():
    instruction_arr = read_input("1-secret-entrance.txt")
    pos = 50
    zero_encounters = 0
    for instruction in instruction_arr:
        direction = int("+1" if instruction[:1] == "R" else "-1")
        magnitude = int(instruction[1:])
        delta = magnitude * direction
        # right of 0: 2 , distance is -2 or +98
        # left of 0: 98, distance is +2 or -98
        divisor = 100 * direction

        revs = delta // divisor
        zero_encounters += revs

        remainder_delta = delta % divisor
        end_pos_raw = pos + remainder_delta
        end_pos = end_pos_raw % 100
        print(
            pos,
            instruction,
            end_pos,
            end_pos_raw,
            revs,
            zero_encounters,
        )

        if (
            (remainder_delta > 0 and pos != 0 and end_pos_raw > 100)
            or (remainder_delta < 0 and pos != 0 and end_pos_raw < 0)
            or end_pos == 0
        ):
            zero_encounters += 1

        pos = end_pos

    print("password is", zero_encounters)


if __name__ == "__main__":
    main()
