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


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


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
        course_id INT,
        teacher_id INT,
        semester VARCHAR(50),
        year INT,
        FOREIGN KEY (course_id) REFERENCES courses(id),
        FOREIGN KEY (teacher_id) REFERENCES teachers(id));"""
    
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

    # create tables
    if conn is not None:
        # create teachers table
        create_table(conn, teachers)

        # create subjects table
        create_table(conn, subjects)

        # create courses table
        create_table(conn, courses)

        # create classrooms table
        create_table(conn, classrooms)

        # create students table
        create_table(conn, students)

        # create enrollment table
        create_table(conn, enrollment)
        
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
