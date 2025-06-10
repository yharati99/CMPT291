# Youssef El-Harati
# 3122914

import sqlite3
conn = sqlite3.connect('uni.db')
cursor = conn.cursor()

def main():
    create_tables()
    print_menu()
    while True:
        choice = input("Please enter your choice (1-8): ")
        if choice == '1':
            insert_student()
        elif choice == '2':
            enroll_student()
        elif choice == '3':
            unenroll_student()
        elif choice == '4':
            update_student_record()
        elif choice == '5':
            see_courses()
        elif choice == '6':
            see_student_enrollments()
        elif choice == '7':
            see_course_enrollment_count()
        elif choice == '8':
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def create_Student_table():
    try:
        cursor.execute("CREATE TABLE Student (sID INTEGER PRIMARY KEY, fName TEXT NOT NULL, lName TEXT NOT NULL, major TEXT NOT NULL)")
        cursor.execute("INSERT INTO Student VALUES (1, 'Alice', 'Johnson', 'Computer Science')")
        cursor.execute("INSERT INTO Student VALUES (2, 'Bob', 'Smith', 'Business')")
        cursor.execute("INSERT INTO Student VALUES (3, 'Carol', 'Lee', 'Computer Science')")
        cursor.execute("INSERT INTO Student VALUES (4, 'David', 'Kim', 'Mathematics')")
        cursor.execute("INSERT INTO Student VALUES (5, 'Eva', 'Brown', 'Psychology')")
        cursor.execute("INSERT INTO Student VALUES (6, 'Alice', 'White', 'Mathematics')")
        
        # Commit transaction
        conn.commit()
        print("Transaction successful")
    except sqlite3.Error as e:
        # Rollback in case of error
        conn.rollback()
        print(f"Transaction failed: {e}")
    finally:
        # perhaps close the connection.
        pass
    
def create_Course_table():
    try:
        cursor.execute("CREATE TABLE Course (cID INTEGER PRIMARY KEY, title TEXT NOT NULL, credits INTEGER NOT NULL)")
        cursor.execute("INSERT INTO Course VALUES (101, 'Intro to Programming', 4)")
        cursor.execute("INSERT INTO Course VALUES (102, 'Marketing Fundamentals', 3)")
        cursor.execute("INSERT INTO Course VALUES (103, 'Data Structures', 4)")
        cursor.execute("INSERT INTO Course VALUES (104, 'Statistics I', 3)")
        cursor.execute("INSERT INTO Course VALUES (105, 'Intro to Psychology', 3)")
        # Commit transaction
        conn.commit()
        print("Transaction successful")
    except sqlite3.Error as e:
        # Rollback in case of error
        conn.rollback()
        print(f"Transaction failed: {e}")
    finally:
        # perhaps close the connection.
        pass

def create_Enrollment_table():
    try:
        cursor.execute("CREATE TABLE Enrollment (sID INTEGER, cID INTEGER, grade TEXT, PRIMARY KEY (sID, cID), FOREIGN KEY (sID) REFERENCES Student(sID), FOREIGN KEY (cID) REFERENCES Course(cID))")
        cursor.execute("INSERT INTO Enrollment VALUES (1, 101, 'A')")
        cursor.execute("INSERT INTO Enrollment VALUES (1, 103, 'B')")
        cursor.execute("INSERT INTO Enrollment VALUES (2, 102, 'B')")
        cursor.execute("INSERT INTO Enrollment VALUES (2, 104, 'A')")
        cursor.execute("INSERT INTO Enrollment VALUES (3, 101, 'A')")
        cursor.execute("INSERT INTO Enrollment VALUES (3, 103, 'A')")
        cursor.execute("INSERT INTO Enrollment VALUES (3, 104, 'B')")
        cursor.execute("INSERT INTO Enrollment VALUES (4, 104, 'C')")
        cursor.execute("INSERT INTO Enrollment VALUES (5, 105, 'A')")
        cursor.execute("INSERT INTO Enrollment VALUES (6, 104, 'A')")
        cursor.execute("INSERT INTO Enrollment VALUES (6, 101, 'A')")
        # Commit transaction
        conn.commit()
        print("Transaction successful") 
    except sqlite3.Error as e:
        # Rollback in case of error
        conn.rollback()
        print(f"Transaction failed: {e}")
    finally:
        # perhaps close the connection.
        pass

def create_tables():
    create_Student_table()
    create_Course_table()
    create_Enrollment_table()
    
def print_menu():
    print("\nWelcome to the Cool University.\n")
    print("Enter the number of your choice:\n")
    print('"I would like to ..."')
    print("1. Insert a student")
    print("2. Enroll a student")
    print("3. Unenroll a student")
    print("4. Update a student record")
    print("5. See all the courses")
    print("6. See a student's enrollments")
    print("7. See how many are enrolled in a course")
    print("8. Exit\n")
    
def insert_student():
    sID = input("Please enter the student's ID: ")
    fName = input("Enter student's first name: ")
    lName = input("Enter student's last name: ")
    major = input("Enter student's major: ")
    cursor.execute("INSERT INTO Student VALUES (?, ?, ?, ?)", (sID, fName, lName, major))
    conn.commit()
    print(f"Student {fName} {lName} added successfully.")
    print("\nPress 1 to return to the main menu")
    print("Press 2 to exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        print_menu()
    elif choice == '2':
        exit_program()

def enroll_student():
    sID = input("Please enter the student's ID: ")
    cID = input("Please enter the course ID: ")
    
    cursor.execute("SELECT * FROM Student WHERE sID = ?", (sID,))
    if not cursor.fetchone():
        print(f"ERROR Student with ID {sID} does not exist.")
        print("\nPress 1 to return to the main menu")
        print("Press 2 to exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print_menu()
        elif choice == '2':
            exit_program()
        return
    
    cursor.execute("SELECT * FROM Course WHERE cID = ?", (cID,))
    if not cursor.fetchone():
        print(f"ERROR Course with ID {cID} does not exist.")
        print("\nPress 1 to return to the main menu")
        print("Press 2 to exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print_menu()
        elif choice == '2':
            exit_program()
        return
    
    cursor.execute("INSERT INTO Enrollment VALUES (?, ?, ?)", (sID, cID, None))
    conn.commit()
    print(f"Student with ID {sID} enrolled in course {cID}.")
    print("\nPress 1 to return to the main menu")
    print("Press 2 to exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        print_menu()
    elif choice == '2':
        exit_program()

def unenroll_student():
    sID = input("Please enter the student's ID: ")
    cID = input("Please enter the course ID: ")
    
    cursor.execute("SELECT * FROM Enrollment WHERE sID = ? AND cID = ?", (sID, cID))
    if not cursor.fetchone():
        print(f"ERROR Student with ID {sID} is not enrolled in course {cID}.")
        print("\nPress 1 to return to the main menu")
        print("Press 2 to exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print_menu()
        elif choice == '2':
            exit_program()
        return
    
    cursor.execute("DELETE FROM Enrollment WHERE sID = ? AND cID = ?", (sID, cID))
    conn.commit()
    print(f"Student with ID {sID} unenrolled from course {cID}.")
    print("\nPress 1 to return to the main menu")
    print("Press 2 to exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        print_menu()
    elif choice == '2':
        exit_program()

def update_student_record():
    sID = input("Enter the student's ID whose record you want to update: ")
    cursor.execute("SELECT * FROM Student WHERE sID = ?", (sID,))
    
    if not cursor.fetchone():
        print(f"ERROR Student with ID {sID} does not exist.")
        print("\nPress 1 to return to the main menu")
        print("Press 2 to exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print_menu()
        elif choice == '2':
            exit_program()
        return
    
    print("Which attribute of the student do you want to update?")
    print("1. The student's ID")
    print("2. The student's first name")
    print("3. The student's last name")
    print("4. The student's major")
    
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        new_sID = input("Enter the new student ID: ")
        cursor.execute("UPDATE Student SET sID = ? WHERE sID = ?", (new_sID, sID))
        conn.commit()
    elif choice == '2':
        new_fName = input("Enter the new first name: ")
        cursor.execute("UPDATE Student SET fName = ? WHERE sID = ?", (new_fName, sID))
        conn.commit()
    elif choice == '3':
        new_lName = input("Enter the new last name: ")
        cursor.execute("UPDATE Student SET lName = ? WHERE sID = ?", (new_lName, sID))
        conn.commit()
    elif choice == '4':
        new_major = input("Enter the new major: ")
        cursor.execute("UPDATE Student SET major = ? WHERE sID = ?", (new_major, sID))
        conn.commit()
    else:
        print("Invalid choice.")
        print("\nPress 1 to return to the main menu")
        print("Press 2 to exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print_menu()
        elif choice == '2':
            exit_program()
        return
        
    print("Student record updated successfully.")
    print("\nPress 1 to return to the main menu")
    print("Press 2 to exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        print_menu()
    elif choice == '2':
        exit_program()

def see_courses():
    cursor.execute("SELECT * FROM Course")
    courses = cursor.fetchall()
    
    print("\nAvailable Courses:")
    for course in courses:
        print(f"Course ID: {course[0]}, Title: {course[1]}, Credits: {course[2]}")
    
    print("\nPress 1 to return to the main menu")
    print("Press 2 to exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        print_menu()
    elif choice == '2':
        exit_program()

def see_student_enrollments():
    sID = input("Please enter the student's ID: ")
    cursor.execute("SELECT * FROM Enrollment WHERE sID = ?", (sID,))
    enrollments = cursor.fetchall()
    
    if not enrollments:
        print(f"ERROR Student with ID {sID} has no enrollments.")
        print("\nPress 1 to return to the main menu")
        print("Press 2 to exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print_menu()
        elif choice == '2':
            exit_program()
        return
    
    print(f"\nEnrollments for Student ID {sID}:")
    for enrollment in enrollments:
        print(f"Course ID: {enrollment[1]}, Grade: {enrollment[2]}")
    
    print("\nPress 1 to return to the main menu")
    print("Press 2 to exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        print_menu()
    elif choice == '2':
        exit_program()

def see_course_enrollment_count():
    cID = input("Please enter the course ID: ")
    cursor.execute("SELECT COUNT(*) FROM Enrollment WHERE cID = ?", (cID,))
    count = cursor.fetchone()[0]
    
    if count == 0:
        print(f"ERROR No students are enrolled in course with ID {cID}.")
    else:
        print(f"There are {count} students enrolled in course with ID {cID}.")
    
    print("\nPress 1 to return to the main menu")
    print("Press 2 to exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        print_menu()
    elif choice == '2':
        exit_program()

def exit_program():
    print("\nGoodbye!")
    conn.close()
    exit()
        
main()