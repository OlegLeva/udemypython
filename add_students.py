import csv


# def add_student(first_name, last_name, age):
#     with open('students.csv', 'a') as file:
#         csv_writer = csv.writer(file)
#         csv_writer.writerow([first_name, last_name, age])
#
# add_student('Oleg', 'Levitskiy', 41)

def print_students(file_name):
    with open(file_name) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for student in csv_reader:
            print(student)


print_students('students.csv')
