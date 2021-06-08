import json
import flask
from flask import request
import mysql.connector

# response.json could be '[{}, {}]'
# '{}' converted {}

# data={latitudes:(latitudes,data)}
# data={90.5678:(56.457,'This place is beautiful')}

# data = [
# {'latitude': 50.08, 'longitude': 100.03, 'info': ''}]
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def home():
    return 'home.html'


@app.route('/pin_place/store', methods=['POST'])
def read_data():
    response = request.data
    data = json.loads(response.json())
    latitudes = []
    longitudes = []
    place_input = []
    for key in data.keys():
        if key == 'latitude':
            latitudes.append(data[key])
            break
        if key == 'longitude':
            longitudes.append(data[key])
            break
        if key == 'info':
            place_input.append(data[key])
            break
    store_data(latitudes, longitudes, place_input)


def execute(sql, args):
    connection = mysql.connector.connect(host='localhost', user='root', password='Bhavya99', db='pinned_places')
    with connection.cursor() as cursor:
        cursor.execute(sql, args)
        connection.commit()
        places_id = cursor.lastrowid
        return places_id


def store_data(latitudes, longitudes, info):
    # db_connection.execute_sql('insert into maps set city=%s', user_data['city'])
    # query = "insert into table maps values(city)" % (input1)
    insert_places_query = """ INSERT INTO PLACES (latitudes, longitudes) VALUES (%d, %d)"""
    places_id = execute(insert_places_query, (latitudes, longitudes))

    if info is not None:
        insert_data_query = """ INSERT INTO DATA (places_id, info) VALUES (%s, %s) """
        execute(insert_data_query, (places_id, info))
    return 'Data stored'


@app.route('/pin_place/read', methods=['POST'])
def get_data(latitude, longitude):
    connection = mysql.connector.connect(host='localhost', user='root', password='Bhavya99')
    select_data_query = """SELECT * FROM places join data on places.places_id = data.data_id where 
                            latitudes = %s AND longitudes = %s""" % latitude % longitude

    with connection.cursor() as cursor:
        cursor.execute(select_data_query)
        result = cursor.fetchall()
        for row in result:
            print(row)

    return 'Data retrieved'
