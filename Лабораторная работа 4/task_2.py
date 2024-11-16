import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME, 'r') as csv_file:
        data = [row for row in csv.DictReader(csv_file)]

    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(data, json_file, indent=4)

