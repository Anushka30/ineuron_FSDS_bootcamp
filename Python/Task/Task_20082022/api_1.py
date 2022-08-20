from flask import Flask
from flask import request
from flask import jsonify
import dbconnection
import logging

app = Flask(__name__)
logging.basicConfig(filename="logfile.log", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")


@app.route("/insert", methods=["GET", "POST"])
def insertDb():
    ns = dbconnection.db_insert()
    if ns:
        return jsonify({"message": "Inserted data successfully"})
    return jsonify({"message": "Data not inserted successfully"})


@app.route("/insert_new", methods=["POST"])
def insert_new():
    try:
        con = dbconnection.db_connection()
        cursor = con.cursor()
        if request.method == "POST":
            name = request.json['name']
            roll_no = request.json['roll_no']
            query = "INSERT INTO student (name, roll_no) VALUES (%s, %s)"
            val = (name, roll_no)
            cursor.execute(query, val)
        con.commit()
        logging.info("Student data is inserted in the database successfully.")
        cursor.close()
        con.close()
        return jsonify({"message": "Inserted data successfully"})
    except Exception as err:
        logging.error(f"Insert error: {err}")
        return jsonify({"message": "Data not inserted successfully"})


@app.route("/fetch", methods=["GET"])
def fetch_data():
    ob = dbconnection.fetch_data()
    if request.method == "GET":
        if len(ob) == 0:
            logging.info("Table is empty.")
            return jsonify({"message": "Table is empty"})
        logging.info(f"Data is :{ob}")
        return jsonify({"message": ob})


@app.route("/fetchone/<string:name>", methods=["GET"])
def fetchOnerec(name):
    ob = dbconnection.fetch_data()
    if request.method == "GET":
        if len(ob) == 0:
            logging.info("Table is empty.")
            return jsonify({"message": "Table is empty"})
        for i in ob:
            if name in i:
                logging.info(f"Data is :{i}")
                return jsonify({"message": i})
            logging.info(f"{name} data is not available in database")
            return jsonify({"message": f"{name} data is not available in database"})


@app.route("/fetchdel/<string:name>", methods=["DELETE"])
def deleteOne(name):
    try:
        ob = dbconnection.delete_data(name)
        return jsonify({"message": f"Record deleted {ob}"})
    except Exception as err:
        return jsonify({"message": err})


@app.route("/update/<int:roll_no>", methods=['PUT'])
def editOne(roll_no):
    new_rec = request.get_json()
    ob = dbconnection.update_data(name=new_rec['name'], roll_no=roll_no)
    return jsonify({"message": f"Updated: {ob}"})


if __name__ == '__main__':
    app.run(debug=True)
