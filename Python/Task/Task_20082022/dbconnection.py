import mysql.connector as connector
from mysql.connector import Error, errorcode
import logging
import pandas as pd

logging.basicConfig(filename="logfile.log", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")


def db_connection():
    try:
        con = connector.connect(host='localhost',
                                user="root",
                                password='root123',
                                db='ineuron')

        logging.info("DB Connected Successfully")
        return con
    except Error as err:
        if err.errno == errorcode.ER_DBACCESS_DENIED_ERROR:
            logging.error(f"Error while connecting to MySQL: {err}")


def table_create():
    try:
        con = db_connection()
        tableName = "CREATE TABLE if not exists Student(Name VARCHAR(255),Roll_no int);"

        cursor = con.cursor()
        cursor.execute(tableName)
        logging.info("Student table is created in the database")
        cursor.close()
    except Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            logging.error(f"Table already exists: {err}")
    finally:
        con.close()
        logging.info("database connection closed successfully.")


def db_insert():
    try:
        table_create()
        con = db_connection()
        cursor = con.cursor()
        student_data = {"name": ["Ram", "Shyam", "Anil", "Anju", "Anjali", "Sunil"],
                        "Roll_no": [101, 102, 103, 104, 105, 106]}
        data = pd.DataFrame(student_data)
        cols = "`,`".join([str(i) for i in data.columns.tolist()])

        # Insert DataFrame records one by one.
        for i, row in data.iterrows():
            sql = "INSERT INTO `Student` (`" + cols + "`) VALUES (" + "%s," * (len(row) - 1) + "%s)"
            cursor.execute(sql, tuple(row))
            # the connection is not autocommit by default, so we must commit to save our # changes
            con.commit()
            logging.info("Student data is inserted in the database successfully.")
        return True
    except Error as err:
        if err.errno == errorcode.ER_INSERT_INFO:
            logging.error(f"Insert error: {err}")
    finally:
        cursor.close()
        con.close()
        logging.info("database connection closed successfully.")


def fetch_data():
    try:
        con = db_connection()
        cursor = con.cursor()
        query = "select * from Student"
        cursor.execute(query)
        rec = cursor.fetchall()
        logging.info("Student data is fetched from the database successfully.")
        if len(rec) != 0:
            return rec
    except Error as err:
        if err.errno == errorcode.ER_SP_FETCH_NO_DATA:
            logging.error(f"Fetch error: {err}")
    finally:
        cursor.close()
        con.close()
        logging.info("database connection closed successfully.")


def delete_data(name):
    try:
        con = db_connection()
        cursor = con.cursor()
        rc = len(fetch_data())
        logging.info(f"{rc} total records before deleting")
        query = f"""DELETE  FROM student WHERE name = %s"""
        cursor.execute(query, (name,))
        logging.info(f"{cursor.rowcount} total records deleted")
        con.commit()
        logging.info("record deleted from the database successfully.")
        logging.info(f"{cursor.rowcount} record(s) deleted")
        rc_del = cursor.rowcount
        return rc_del
    except Error as err:
        logging.error(f"Delete error: {err}")
    finally:
        cursor.close()
        con.close()
        logging.info("database connection closed successfully.")


def update_data(name, roll_no):
    try:
        con = db_connection()
        cursor = con.cursor()
        sql = "UPDATE student SET name = %s WHERE roll_no = %s"
        val = (name, roll_no)
        cursor.execute(sql, val)
        con.commit()
        logging.info("record updated in database successfully.")
        rc = fetch_data()
        for i in rc:
            if name in i:
                logging.info(f"Updated Data is :{i}")
                return i
    except Error as err:
        logging.error(f"update error: {err}")
    finally:
        cursor.close()
        con.close()
        logging.info("database connection closed successfully.")
