students = {}  # dictionary to store student data

def login():
  # admin login function
  username = input("Enter username: ")
  password = input("Enter password: ")
  if username == "admin" and password == "admin123":
    return True
  else:
    print("Invalid login credentials.")
    return False

def add_student(name, grades):
  # function to add a student to the system
  students[name] = grades

def remove_student(name):
  # function to remove a student from the system
  if name in students:
    del students[name]
  else:
    print("Student does not exist.")

def average_grades(name):
  # function to calculate the average grades of a student
  if name in students:
    grades = students[name]
    avg = sum(grades) / len(grades)
    return avg
  else:
    print("Student does not exist.")

def menu():
  # menu to allow the user to select an option
  print("1. Add a student")
  print("2. Remove a student")
  print("3. Calculate average grades")
  choice = input("Enter your choice: ")
  if choice == "1":
    # add a student
    name = input("Enter student name: ")
    grades = []
    grade = input("Enter a grade (enter 'done' when finished): ")
    while grade != "done":
      grades.append(float(grade))
      grade = input("Enter a grade (enter 'done' when finished): ")
    add_student(name, grades)
  elif choice == "2":
    # remove a student
    name = input("Enter student name: ")
    remove_student(name)
  elif choice == "3":
    # calculate average grades
    name = input("Enter student name: ")
    avg = average_grades(name)
    if avg:
      print("Average grades:", avg)

if login():  # only allow access if login is successful
  while True:
    menu()  # display menu and handle user selection
    repeat = input("Do you want to perform another action (y/n)? ")
    if repeat == "n":
      break
