import os

dir = os.path.dirname(__file__)
input_dir_path = os.path.join(dir, "..", "input")


def read_input(input_file: str, separator: str = "\n") -> list[str]:
    with open(os.path.join(input_dir_path, input_file), "r") as file:
        content = file.read()
        instruction_arr = content.split(separator)
        return instruction_arr
