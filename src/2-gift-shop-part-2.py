from utils import read_input
from typing import TypedDict, Optional


def is_even(x: int) -> bool:
    return x % 2 == 0


def is_odd(x: int) -> bool:
    return not is_even(x)


def id_range_splitter(id_range_str: str) -> tuple[str, str]:
    return id_range_str.split("-")


def create_processable_sub_ranges(id_range: tuple[str, str]) -> list[tuple[str, str]]:
    start_str, end_str = id_range

    start_str_len = len(start_str)
    end_str_len = len(end_str)

    sub_ranges: list[tuple[str, str]] = []

    if start_str_len < end_str_len:
        sub_ranges.append([start_str, "9" * start_str_len])
        sub_ranges.extend(
            create_processable_sub_ranges(["1" + "0" * start_str_len, end_str])
        )
    elif start_str_len > end_str_len:
        raise Exception("Start range was bigger than end range somehow?")
    else:
        # when both start of range and end of range have same no of digits.
        sub_ranges.append([start_str, end_str])

    return sub_ranges


cached_factors = dict()


# this function caches the outputs factors in a variable because many ranges will have a previously encountered number length
def get_factors_of_number(input: int) -> list[int]:
    cached = cached_factors.get(input)
    factors = []

    if cached is not None:
        return cached

    for i in range(1, input + 1):
        if input % i == 0:
            factors.append(i)

    cached_factors[input] = factors
    return factors


def main():
    id_ranges_split = list(map(id_range_splitter, read_input("2-gift-shop.txt", ",")))

    print(id_ranges_split)

    ranges_broken_down = [
        sub_range
        for sub_range_set in list(map(create_processable_sub_ranges, id_ranges_split))
        for sub_range in sub_range_set
    ]

    invalid_id_sum = 0

    for invalid_id_range in ranges_broken_down:
        start_str, end_str = invalid_id_range

        start = int(start_str)
        end = int(end_str)

        # we can assume same length of numbers as that is what create_processable_sub_ranges does
        num_length = len(start_str)

        # find all the different permutations of repeating sequences possible

        # exclude the length itself from the list of factors, as a string of this length cannot repeat and still be within the range
        factors = list(
            filter(lambda x: x != num_length, get_factors_of_number(num_length))
        )

        num_set: set[int] = set()
        for length_of_repeating_sequence in factors:
            number_of_repetitions = num_length // length_of_repeating_sequence

            start_repeating_range = int(start_str[:length_of_repeating_sequence])
            end_repeating_range = int(end_str[:length_of_repeating_sequence])

            for i in range(start_repeating_range, end_repeating_range + 1):
                invalid_id = int(str(i) * number_of_repetitions)

                if start <= invalid_id <= end:
                    num_set.add(invalid_id)

        invalid_id_sum += sum(num_set)

    print("invalid id sum is", invalid_id_sum)

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


if __name__ == "__main__":
    main()
