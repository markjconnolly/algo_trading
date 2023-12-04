import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

from binance.spot import Spot
def connect_to_db():
    conn = sqlite3.connect('database/ticker_data.db')
    return conn

print(connect_to_db())
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
    data = {}
    sql_max_time_spec = '''SELECT MAX(ticker_time) FROM spot_entry WHERE symbol = ?'''
    sql_data_spec = '''SELECT ticker_time, open_price FROM spot_entry WHERE symbol = ? and ticker_time > ? AND ticker_time < ?'''
    symbol = 'BTCUSDT'

    try:
        conn = connect_to_db()
        cursor = conn.cursor()

        # Get the latest time
        sql_max_time_val = (symbol,)
        cursor.execute(sql_max_time_spec, sql_max_time_val)
        max_timestamp = cursor.fetchall()
        max_timestamp = max_timestamp[0][0]

        # Get the last 10 days of data
        start_timestamp = max_timestamp - 1000*60*60
        sql_data_val = (symbol,) + (start_timestamp,) + (max_timestamp,)
        cursor.execute(sql_data_spec, sql_data_val)
        ticker_data = np.array(cursor.fetchall())
        print(ticker_data[:,0])
        data["time"] = ticker_data[:,0].tolist()
        data["signal"] = ticker_data[:,1].tolist()
    except:
        data = {}

    
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