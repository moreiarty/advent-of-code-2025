from utils import read_input
from functools import reduce


no_of_batteries_to_select_in_each_bank = 12


def main():
    battery_banks = list(
        read_input(
            "3-lobby.txt",
        )
    )

    print("no of battery banks:", len(battery_banks))

    total_max_output_joltage = 0

    for b, battery_bank in enumerate(battery_banks):
        selected_joltages = [0] * no_of_batteries_to_select_in_each_bank

        battery_bank_length = len(battery_bank)
        for i, battery_joltage_str in enumerate(battery_bank):
            battery_joltage = int(battery_joltage_str)
            for j, selected_joltage in enumerate(selected_joltages):
                if battery_joltage > selected_joltage and i < battery_bank_length - (
                    no_of_batteries_to_select_in_each_bank - 1
                ):
                    selected_joltages = (
                        selected_joltages[:j]
                        + [battery_joltage]
                        + [0] * ((no_of_batteries_to_select_in_each_bank - 1) - j)
                    )
                    break
                elif (
                    battery_joltage > selected_joltage
                    and j
                    > i
                    - battery_bank_length
                    + (no_of_batteries_to_select_in_each_bank - 1)
                ):
                    selected_joltages = (
                        selected_joltages[:j]
                        + [battery_joltage]
                        + [0] * ((no_of_batteries_to_select_in_each_bank - 1) - j)
                    )
                    break

        print(selected_joltages)
        max_output_joltage = int(
            reduce(lambda prev, curr: prev + str(curr), selected_joltages, "")
        )
        print(max_output_joltage)
        total_max_output_joltage += max_output_joltage

    print("largest output joltage is", total_max_output_joltage)


if __name__ == "__main__":
    main()
