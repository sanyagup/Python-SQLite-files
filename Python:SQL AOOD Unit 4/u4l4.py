import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_teachers(conn, teacher):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    teachers_insert = ''' INSERT INTO teachers (first_name, last_name, department, experience_years, contact_email)
              VALUES(?,?,?,?,?) ''' 
    
le    cur = conn.cursor()
    cur.execute(teachers_insert, teacher)
    conn.commit()

    return cur.lastrowid

def create_subject(conn, subject):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    subjects_insert = ''' INSERT INTO subjects (name, department)
              VALUES(?,?) ''' 
    
    cur = conn.cursor()
    cur.execute(subjects_insert, subject)
    conn.commit()

    return cur.lastrowid

def create_courses(conn, courses):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    courses_insert = ''' INSERT INTO courses (name, subject_id, level)
              VALUES(?,?,?) '''
    
    cur = conn.cursor()
    cur.execute(courses_insert, courses)
    conn.commit()

    return cur.lastrowid

def create_classrooms(conn, classroom):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    classrooms_insert = '''INSERT INTO classrooms (course_id, teacher_id, semester, year)
              VALUES(?,?,?,?) '''
    
    cur = conn.cursor()
    cur.execute(classrooms_insert, classroom)
    conn.commit()

    return cur.lastrowid

def create_student(conn, student):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    students_insert = ''' INSERT INTO students (first_name, last_name, email, major, study_year)
              VALUES(?,?,?,?,?) '''
    
    cur = conn.cursor()
    cur.execute(students_insert, student)
    conn.commit()

    return cur.lastrowid

def create_enrollment(conn, enrollment):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    enrollment_insert = ''' INSERT INTO enrollment (student_id, classroom_id, grade)
              VALUES(?,?,?) '''
    
    cur = conn.cursor()
    cur.execute(enrollment_insert, enrollment)
    conn.commit()

    return cur.lastrowid


def main():
    database = r"/Users/sanyagupta/sqlite:db/pythonsqlite.db"

    teachers = """ CREATE TABLE IF NOT EXISTS teachers (id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        department VARCHAR(100),
        experience_years INT,
        contact_email VARCHAR(255));"""
    
    subjects = """CREATE TABLE IF NOT EXISTS subjects (id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        department VARCHAR(100));"""
    
    courses = """CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        subject_id INT,
        level VARCHAR(50),
        FOREIGN KEY (subject_id) REFERENCES subjects(id));"""

    classrooms = """CREATE TABLE IF NOT EXISTS classrooms (id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        subject_id INT,
        level VARCHAR(50),
        FOREIGN KEY (subject_id) REFERENCES subjects(id)
);"""
    
    students = """CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT,
      first_name VARCHAR (255) NOT NULL,
      last_name VARCHAR (255) NOT NULL,
      email VARCHAR (255) NOT NULL,
      major VARCHAR (255) NOT NULL,
      study_year INT,
      course_id INT,
      grade VARCHAR(100),
      FOREIGN KEY (course_id) REFERENCES courses(id));"""
    
    enrollment = """CREATE TABLE IF NOT EXISTS enrollment (student_id INT,
        classroom_id INT,
        grade VARCHAR(100),
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (classroom_id) REFERENCES classrooms(id));"""
    

    # create a database connection
    conn = create_connection(database)

    with conn:
        # create a new teacher
        teacher = ('Matthew', 'McLaughlin', 'Computer Science', 10, 'matthew.mclaughlin@school.edu')
        create_teachers(conn, teacher)
        teacher = ('Eleanor', 'Alexander', 'Computer Science', 8, 'eleanor.alexander@school.edu')
        create_teachers(conn, teacher)
        teacher = ('Stacy', 'Gwoc', 'Statistics', 12, 'stacy.gwoc@school.edu')
        create_teachers(conn, teacher)
        ('Emily', 'Roberts', 'Calculus', 5, 'emily.roberts@school.edu')
        create_teachers(conn, teacher)
        ('Emily', 'Lawson', 'Physics', 9, 'emily.lawson@school.edu')
        create_teachers(conn, teacher)

        # subjects
        subject = ('Computer Science', 'STEM')
        create_subject(conn, subject)
        subject = ('Statistics', 'STEM')
        create_subject(conn, subject)
        subject = ('Physics', 'STEM')
        create_subject(conn, subject)
        subject = ('Calculus', 'STEM')
        create_subject(conn, subject)

        #courses
        course = ('Computer Science A', 1, 'Introductory')
        create_courses(conn, course)
        course = ('Computer Science Principles', 1, 'Introductory')
        create_courses(conn, course)
        course = ('AP Statistics', 2, 'Advanced')
        create_courses(conn, course)
        course = ('AP Calculus AB', 2, 'Advanced')
        create_courses(conn, course)
        course = ('AP Physics 1', 3, 'Advanced')
        create_courses(conn, course)

        #classrooms
        classroom = (1, 1, 'Fall', 2023)
        create_classrooms(conn, classroom)
        classroom = (2, 2, 'Spring', 2024)
        create_classrooms(conn, classroom)
        classroom = (3, 3, 'Fall', 2023)
        create_classrooms(conn, classroom)
        classroom = (4, 4, 'Spring', 2024)
        create_classrooms(conn, classroom)
        classroom = (5, 5, 'Fall', 2023)
        create_classrooms(conn, classroom)

        #students
        student = ('Bob', 'Holland', 'bob.holland@student.school.edu', 'Computer Science', 2)
        create_student(conn, student)
        student = ('David', 'Jones', 'david.jones@student.school.edu', 'Mathematics', 3)
        create_student(conn, student)
        student = ('Billy', 'Bob', 'billy.bob@student.school.edu', 'Physics', 1)
        create_student(conn, student)
        student = ('Alice', 'Wonderland', 'alice.wonderland@student.school.edu', 'Computer Science', 4)
        create_student(conn, student)
        student = ('Charlie', 'Brown', 'charlie.brown@student.school.edu', 'Mathematics', 2)
        create_student(conn, student)


        #enrollments
        enrollment = (1, 1, 'A')
        create_enrollment(conn, enrollment)
        enrollment = (2, 3, 'B')
        create_enrollment(conn, enrollment)
        enrollment = (2, 4, 'B')
        create_enrollment(conn, enrollment)
        enrollment = (3, 1, 'B')
        create_enrollment(conn, enrollment)
        enrollment = (3, 2, 'A')
        create_enrollment(conn, enrollment) 
        enrollment = (3, 3, 'A')
        create_enrollment(conn, enrollment)
        enrollment = (3, 4, 'A')
        create_enrollment(conn, enrollment)
        enrollment = (4, 1, 'A')
        create_enrollment(conn, enrollment)
        enrollment = (4, 2, 'A')
        create_enrollment(conn, enrollment)
        enrollment = (5, 3, 'B')
        create_enrollment(conn, enrollment)
        enrollment = (5, 4, 'A')
        create_enrollment(conn, enrollment)


if __name__ == '__main__':
    main()
