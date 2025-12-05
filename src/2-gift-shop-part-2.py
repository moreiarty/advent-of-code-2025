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
        # break it up into ranges by digit numbers: 20345 - 99999, 100000 - 139457

        # 100000 - 139457 has 6 digits, factors are 1, 2, and 3
        # repeating sequence of 3: 100100, 101101,...139139 (sequence is created by looping from 100 - 139)
        # repeating sequence of 2: 101010, 111111,...131313 (sequnce is created by looping from 10 - 13)
        # repeating sequence of 1: 111111 (sequence is created from looping through 1 - 1)

        # another range example: 459 - 20 345 952 becomes 459 - 999, 1000 - 9999, 10000 - 99999, 100000 - 999999, 1 000 000 - 9 999 999, 10 000 000 - 20 345 952
        # For each new range, build repeating sequences of a length for all factors of the number of digits in each sub range.
        # 459 - 999 has 3 digits, 3 has factors 1 and 3, we rule out 3 because you can't repeat a sequence of length 3 in this number range.
        # So the invalid IDs here include 444, 555, 666, 777, 888, 999. If we restrict to the range, it's 555, 666, 777, 888, 999

        # 1000 - 9999 has 4 digits, 4 has factors 1 and 4, 2 and 2. we rule out 4. so we get 1 and 2.
        # So the invalid Ids here include repeating sequences of length 1: 1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999
        # repeating sequences of length 2: 1010, 1111, 1212, 1313....9797, 9898, 9999,

        # 10000 - 99999 has 5 digits, 5 has factors 1 and 5, we rule out 5 so we're left with 1
        # 11111, 22222, 33333, 44444, 55555, 66666, 77777, 88888, 99999

        # 100000 - 999999 has 6 digits, 6 has factors 1 and 6, 2 and 3. We rule out 6, so we get 1, 2, and 3
        # Invalid ids include repeating sequences of 3, twice: 100100, 101101, 102102...998998, 999999
        # repeating sequences of 2, three times: 101010, 111111, 121212...989898, 999999

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
