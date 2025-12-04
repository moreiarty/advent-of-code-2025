from utils import read_input


def id_range_splitter(id_range_str: str) -> tuple[str, str]:
    return id_range_str.split("-")


def is_even(x: int) -> bool:
    return x % 2 == 0


def is_odd(x: int) -> bool:
    return not is_even(x)


def main():
    id_ranges = list(map(id_range_splitter, read_input("2-gift-shop.txt", ",")))
    # If both the start and end of a range have an odd amount of characters, then no numbers in the range
    # can possibly include a number with only a twice repeating sequence of digits
    filtered_id_ranges = list(
        filter(lambda x: is_even(len(x[0])) or is_even(len(x[1])), id_ranges)
    )

    invalid_id_set: set[int] = set()

    sum = 0

    for id_range in filtered_id_ranges:
        start_str, end_str = id_range

        start_str_len = len(start_str)
        end_str_len = len(end_str)

        start_str = "1" + "0" * (start_str_len) if is_odd(start_str_len) else start_str
        end_str = "9" * (end_str_len - 1) if is_odd(end_str_len) else end_str

        start_str_len = len(start_str)
        end_str_len = len(end_str)

        repeating_pattern_len = start_str_len // 2

        start_int = int(start_str)
        end_int = int(end_str)

        # now that we are checking for ids where they are made entirely of any length of repeating sequence, we should look at factors of the length of the start range and end range?
        # if range is 20345 - 139457
        # then we should check repeating sequences of length 1, and 5 (factors of 5, which is length of start of range)
        # and check repeating sequences of length 1, and 6, 3, 2 (factors of 6, which is length of end of range)

        # 20345 - 2034520345????

        first_half_start_str = start_str[:repeating_pattern_len]
        first_half_start = int(first_half_start_str)
        first_half_end_str = end_str[:repeating_pattern_len]
        first_half_end = int(first_half_end_str)
        sequence_start = str(first_half_start)
        sequence_end = str(first_half_end)

        # Process Repeating Sequence
        repeat_sequence_start = int(sequence_start)
        repeat_sequence_end = int(sequence_end)

        for i in range(repeat_sequence_start, repeat_sequence_end + 1):
            full_num_str = str(i) * 2
            full_num = int(full_num_str)
            if start_int <= full_num <= end_int:
                sum += full_num

    print("sum of invalid ids is", sum)


if __name__ == "__main__":
    main()
