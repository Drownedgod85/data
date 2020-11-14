from cs50 import SQL
from sys import argv, exit
import csv

#Check command-line arguments
#Open CSV file given by command-line argument
#for each row, parse name
#insert each student into the students table of students.db


def partition_name(full_name):
    names = full_name.split() # "Hermione Granger" -> ["Hermione", "None", "Granger"]
    return names if len(names) >= 3 else [ names[0], None, names[1] ]
if len(argv) != 2:
    exit(1)

db = SQL("sqlite:///students.db")

csv_path = argv[1]
with open(csv_path) as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        name = row["name"]
        house = row["house"]
        birth = row["birth"]

        full = name.split()
        if len(full) == 2:
            first = full[0]
            middle = None
            last = full[1]
        if len(full) == 3:
            first = full[0]
            middle = full[1]
            last = full[2]

        db.execute("Insert INTO students(first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", first, middle, last, row["house"], int(row["birth"]))
