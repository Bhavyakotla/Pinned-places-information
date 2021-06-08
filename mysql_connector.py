import mysql.connector


def sql_database():
    connection = mysql.connector.connect(host='localhost', user='root', password='Bhavya99')
    create_db_query = "CREATE DATABASE pinned_places"
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)


def sql_table():
    create_places_table_query = """ CREATE TABLE places(
                                    places_id INT AUTO_INCREMENT PRIMARY KEY, 
                                    latitudes float(10,6),
                                    longitudes float(10,6))"""
    execute(create_places_table_query)

    create_description_table_query = """ CREATE TABLE data(
                                        data_id INT PRIMARY KEY,
                                        info VARCHAR(200),
                                        FOREIGN KEY(data_id) REFERENCES PLACES(places_id))"""
    execute(create_description_table_query)


def execute(query):
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='Bhavya99',
                                         db='pinned_places')
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()


sql_table()
