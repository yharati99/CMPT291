import sqlite3
conn = sqlite3.connect('uni.db')
cursor = conn.cursor()

def main():
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
        cursor.execute("CREATE TABLE Enrollment (sID INTEGER, cID INTEGER, grade TEXT NOT NULL, PRIMARY KEY (sID, cID), FOREIGN KEY (sID) REFERENCES Student(sID), FOREIGN KEY (cID) REFERENCES Course(cID))")
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
    