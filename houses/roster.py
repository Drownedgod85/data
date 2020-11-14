# TODO
# Check command-line arguments
# Query database for all students in house
# print out each student's full name and birth year
# Students should be sorted alphabetically by last name, then first name

from cs50 import SQL
from sys import argv, exit
import csv

if len(argv) != 2:
    exit(1)

house = argv[1]
db = SQL("sqlite:///students.db")
query = db.execute("SELECT first, middle, last, house, birth FROM students WHERE house = ? ORDER BY last, first", house)

for row in query:
    if ['middle'] != ' ':
        print(f'{row["first"]} {row["last"]}, born {row["birth"]}')
    else:
        print(f'{row["first"]} {row["middle"]} {row["last"]}, born {row["birth"]}')
