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


def update_teachers(conn, teacher):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE teachers
              SET first_name = ? ,
                  last_name = ? ,
                  department = ?,
                  experience_years = ?,
                  contact_email = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, teacher)
    conn.commit()

def update_students(conn, student):
    """
    Update priority, begin_date, and end_date of a task
    :param conn:
    :param task: (task_id, priority, begin_date, end_date)
    :return: None
    """
    sql = ''' UPDATE students
              SET first_name = ?,
                  last_name = ?,
                  email = ?,
                  major = ?,
                  study_year = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, student)
    conn.commit()

def select_all_teachers(conn):
    """
    Query all rows in the teachers table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM teachers")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_all_students(conn):
    """
    Query all rows in the students table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_task_by_classroom_id(conn, priority):
    """
    Query enrollment by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM enrollment WHERE classroom_id=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_task_by_study_year(conn, priority):
    """
    Query students by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE study_year=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = r"/Users/sanyagupta/sqlite:db/pythonsqlite.db"
    # create a database connection
    conn = create_connection(database)


    with conn:
        update_teachers(conn, ('Ben', 'Later', 'Computer Science', 3, "ben@gmail.com", 1))
        update_students(conn, ('Annie', 'Shin', 'annieshin@edu.com', "Calculus", 2, 1))
        print("2. Query all teachers")
        select_all_teachers(conn)
        print("2. Query all students")
        select_all_teachers(conn)
        print("1. Query enrollment by classroomn_id:")
        select_task_by_classroom_id(conn, 1)
        print("2. Query enrollment by study_year:")
        select_task_by_study_year(conn, 1)




if __name__ == '__main__':
    main()