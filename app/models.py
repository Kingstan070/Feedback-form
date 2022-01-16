from . import dbd
import mysql.connector

def create_db():
    '''
    To create all database if it not exist

    '''
    try:
        db = mysql.connector.connect(host= dbd.host,
                                    user = dbd.user,
                                    password = dbd.password,
                                    port = dbd.port)

        cur = db.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS CURD;")
        cur.execute("USE CURD;")

        #TABLE FOR STUDENT
        cur.execute('''
        CREATE TABLE IF NOT EXISTS STUDENTS 
        (EMAIL VARCHAR(50) PRIMARY KEY, 
        NAME VARCHAR(30) NOT NULL, 
        CLASS CHAR(10) NOT NULL, 
        SCORE INTEGER DEFAULT 0, 
        LAST_SEEN VARCHAR(24) );
        ''')

        print("Created successfully !!!!!!!!!!!!!!!!!!!!!!!!!!")
    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))
    finally:
        if db.is_connected():
            cur.close()
            db.close()
            print("MySQL connection is closed")
        

def check_emailid(email):
    '''
    Args:
        email (str) mail id
    Returns:
        tuple(boolean, string)
        1. (boolean) True if the email exist in the database of students
        and False if it dosen't and if there is any error in the database
        2. (string) name of the student

    '''
    try:
        db = mysql.connector.connect(host= dbd.host,
                                    user = dbd.user,
                                    password = dbd.password,
                                    port = dbd.port)
                                    # database= dbd.database)

        cur = db.cursor()
        cur.execute(f'USE {dbd.database};')
        # Risk of SQL Injection attacks
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!
        cur.execute(f'''SELECT * FROM STUDENTS WHERE EMAIL="{email}";''')
        # !!!!!!!!!!!!!!!!!!!
        data = cur.fetchone()
        if cur.rowcount < 0:
            result = False
        else:
            result = True

    except mysql.connector.Error as error:
        print(error)

    finally:
        if db.is_connected():
            cur.close()
            db.close()
            print("MySQL connection is closed")
        return result

def get_student_values(email):
    '''
    Args:
        email (str) the email id of the user
    Returns:
        (tuple) containing the other data
    '''
    try:
        db = mysql.connector.connect(host= dbd.host,
                                    user = dbd.user,
                                    password = dbd.password,
                                    port = dbd.port)
                                    # database= dbd.database)

        cur = db.cursor()
        cur.execute(f'USE {dbd.database};')
        # Risk of SQL Injection attacks
        cur.execute(f'''SELECT * FROM STUDENTS WHERE EMAIL="{email}";''')
        data = cur.fetchone()
    except mysql.connector.Error as error:
        print(error)
    finally:
        if db.is_connected():
            cur.close()
            db.close()
            print("MySQL connection is closed")
        return (data)