PRAGMA foreign_keys = ON;

CREATE TABLE 'Building' (
  'bNumber' INTEGER PRIMARY KEY NOT NULL,
  'StreetNum' TEXT NOT NULL,
  'StreetName' TEXT NOT NULL,
  'City' TEXT NOT NULL,
  'Province' TEXT NOT NULL,
  'PostalCode' TEXT NOT NULL
);

CREATE TABLE 'Department' (
  'DeptName' TEXT PRIMARY KEY NOT NULL,
  'Budget' REAL,
  'bNumber' INTEGER NOT NULL,
  FOREIGN KEY ('bNumber') REFERENCES 'Building'('bNumber')
);

CREATE TABLE 'Instructor' (
  'InstructorID' INTEGER PRIMARY KEY NOT NULL,
  'fName' TEXT NOT NULL,
  'lName' TEXT NOT NULL,
  'Salary' REAL NOT NULL,
  'DeptName' TEXT NOT NULL,
  'Role' TEXT NOT NULL,
  FOREIGN KEY ('DeptName') REFERENCES 'Department'('DeptName')
);

CREATE TABLE 'Course' (
  'CourseID' TEXT PRIMARY KEY NOT NULL,
  'Title' TEXT NOT NULL,
  'Credits' INTEGER NOT NULL,
  'DeptName' TEXT NOT NULL,
  FOREIGN KEY ('DeptName') REFERENCES 'Department'('DeptName')
);

CREATE TABLE 'Classroom' (
  'ClassID' TEXT PRIMARY KEY NOT NULL,
  'RoomNumber' TEXT NOT NULL,
  'Capacity' INTEGER,
  'bNumber' INTEGER NOT NULL,
  FOREIGN KEY ('bNumber') REFERENCES 'Building'('bNumber')
);

CREATE TABLE 'Student' (
  'StudentID' INTEGER PRIMARY KEY,
  'fName' TEXT NOT NULL,
  'lName' TEXT NOT NULL,
  'GPA' REAL,
  'StudentType' TEXT,
  'Thesis' TEXT
);

CREATE TABLE 'TimeSlot' (
  'SlotID' INTEGER PRIMARY KEY NOT NULL,
  'Day' TEXT NOT NULL,
  'StartTime' TEXT NOT NULL,
  'EndTime' TEXT NOT NULL
);

CREATE TABLE 'Section' (
  'SectionCode' TEXT PRIMARY KEY NOT NULL,
  'Semester' TEXT NOT NULL,
  'Year' INTEGER NOT NULL,
  'CourseID' TEXT NOT NULL,
  'InstructorID' INTEGER NOT NULL,
  'ClassID' TEXT NOT NULL,
  'StudentID' INTEGER NOT NULL,
  'SlotID' INTEGER NOT NULL,
  FOREIGN KEY ('InstructorID') REFERENCES 'Instructor'('InstructorID'),
  FOREIGN KEY ('CourseID') REFERENCES 'Course'('CourseID'),
  FOREIGN KEY ('ClassID') REFERENCES 'Classroom'('ClassID'),
  FOREIGN KEY ('StudentID') REFERENCES 'Student'('StudentID'),
  FOREIGN KEY ('SlotID') REFERENCES 'TimeSlot'('SlotID')
);

CREATE TABLE 'Enrollment' (
  'StudentID' INTEGER NOT NULL,
  'SectionCode' TEXT NOT NULL,
  'Grade' TEXT,
  PRIMARY KEY ('SectionCode', 'StudentID'),
  FOREIGN KEY ('StudentID') REFERENCES 'Student'('StudentID'),
  FOREIGN KEY ('SectionCode') REFERENCES 'Section'('SectionCode')
);