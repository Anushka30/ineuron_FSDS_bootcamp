import mysql.connector
from mysql.connector import Error
import pandas as pd
import logging

logging.basicConfig(filename='logfile.log', level=logging.INFO, format="%(levelname)s:%(asctime)s:%(name)s:%(message)s")

try:
    connection = mysql.connector.connect(host='localhost',
                                         user="root",
                                         password='root123',
                                         db='ineuron')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        logging.info(f"Connected to MySQL Server version: {db_Info}")
        cursor = connection.cursor(buffered=True)
        cursor.execute("show databases;")
        record = cursor.fetchone()
        logging.info(f"You're connected to database: {record[0]}")
        data = pd.read_csv('E:\\Python_Work\\Python_Exercise\\Python_Exercise\\ineuron\\Python\\bank\\bank-full.csv',
                           sep=";")

        # creating column list for insertion
        cols = "`,`".join([str(i) for i in data.columns.tolist()])

        # Insert DataFrame records one by one.
        for i, row in data.iterrows():
            sql = "INSERT INTO `bank_details` (`" + cols + "`) VALUES (" + "%s," * (len(row) - 1) + "%s)"
            cursor.execute(sql, tuple(row))
            # the connection is not autocommit by default, so we must commit to save our # changes
            connection.commit()

        sql = "select count(*) from bank_details"
        cursor.execute(sql)
        rec = cursor.fetchall()
        if rec == 0:
            logging.error(f"Records are not inserted: {rec}")
        logging.info(f"Records inserted successfully in table 'bank_details': {rec[0][0]}")

except Error as e:
    logging.error(f"Error while connecting to MySQL: {e}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        logging.info("MySQL connection is closed")
