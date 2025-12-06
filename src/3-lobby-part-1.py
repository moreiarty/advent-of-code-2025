from utils import read_input


def main():
    battery_banks = list(
        read_input(
            "3-lobby.txt",
        )
    )

    print("no of battery banks:", len(battery_banks))

    total_max_output_joltage = 0
    for j, battery_bank in enumerate(battery_banks):
        if j == 1:
            print(battery_bank)

        first_battery_joltage = 0
        second_battery_joltage = 0

        battery_bank_length = len(battery_bank)
        for i, battery_joltage_str in enumerate(battery_bank):
            battery_joltage = int(battery_joltage_str)
            if battery_joltage > first_battery_joltage and i < battery_bank_length - 1:
                first_battery_joltage = battery_joltage
                second_battery_joltage = 0
            elif battery_joltage > second_battery_joltage:
                second_battery_joltage = battery_joltage

        max_output_joltage = int(
            str(first_battery_joltage) + str(second_battery_joltage)
        )

        if j == 1:
            print(max_output_joltage)

        total_max_output_joltage += max_output_joltage

    print("largest output joltage is", total_max_output_joltage)


if __name__ == "__main__":
    main()
