import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

def connect_to_db():
    conn = sqlite3.connect('database.db')
    return conn

# def create_table():
#     try:
#         conn = connect_to_db()
#         conn.execute('''
#             CREATE TABLE users (
#                     user_id INTEGER PRIMARY KEY NOT NULL,
#                     name TEXT NOT NULL,
#                     email TEXT NOT NULL,
#                     phone TEXT NOT NULL,
#                     address TEXT NOT NULL,
#                     country TEXT NOT NULL
#             );
#         ''')
#         conn.commit()
#         print("User table created successfully")
#     except:
#         print("User table creation failed - Maybe table")
#     finally:
#         conn.close()
        



def get_data():
    # users = []
    # try:
    #     conn = connect_to_db()
    #     conn.row_factory = sqlite3.Row
    #     cur = conn.cursor()
    #     cur.execute("SELECT * FROM users")
    #     rows = cur.fetchall()
    #     # convert row objects to dictionary
    #     for row in rows:
    #         user = {}
    #         user["user_id"] = row["user_id"]
    #         user["name"] = row["name"]
    #         user["email"] = row["email"]
    #         user["phone"] = row["phone"]
    #         user["address"] = row["address"]
    #         user["country"] = row["country"]

    #         users.append(user)

    # except:
    #     users = []
    data = {}
    data["signal"] = [1,2,3,4,5,2]
    return data


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/api/signal', methods=['GET'])
def api_get_data():
    return jsonify(get_data())



if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run()