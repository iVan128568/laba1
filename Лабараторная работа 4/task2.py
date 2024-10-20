# TODO импортировать необходимые молули
from csv import DictReader
from json import dump

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as inp, open(OUTPUT_FILENAME, 'w') as oup:
        dump(list(DictReader(inp)), oup, indent=4)


    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")



