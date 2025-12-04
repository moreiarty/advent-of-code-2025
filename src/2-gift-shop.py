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

    repeating_sequence_ranges: list[tuple[str, str]] = []

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

        first_half_start_str = start_str[:repeating_pattern_len]
        second_half_start_str = start_str[repeating_pattern_len:]
        first_half_start = int(first_half_start_str)
        second_half_start = int(second_half_start_str)
        first_half_end_str = end_str[:repeating_pattern_len]
        second_half_end_str = end_str[repeating_pattern_len:]
        first_half_end = int(first_half_end_str)
        second_half_end = int(second_half_end_str)
        sequence_start = str(max(first_half_start, second_half_start))
        sequence_end = str(min(first_half_end, second_half_end))

        repeating_sequence_ranges.append([sequence_start, sequence_end])

    for repeating_sequence_range in repeating_sequence_ranges:
        start_str, end_str = repeating_sequence_range

        start = int(start_str)
        end = int(end_str)

        print(start, end)

        for i in range(start, end + 1):
            full_num_str = str(i) * 2
            full_num = int(full_num_str)
            print(full_num)
            if full_num not in invalid_id_set:
                sum += full_num
                invalid_id_set.add(full_num)

    print("sum of invalid ids is", sum)


if __name__ == "__main__":
    main()
