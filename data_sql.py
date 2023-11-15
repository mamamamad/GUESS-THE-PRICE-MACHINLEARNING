import mysql.connector

# config = {'user': 'root',
#               'password': 'Mohammad22.',
#               'host': 'localhost',
#               'database': 'cars'}


def add_to_table(list_cars: list, config: dict):

    cnx = mysql.connector.connect(**config)

    add_car = (
        "INSERT INTO car""(Name_car, Price, Km, Model, Year_car)""VALUES(%s,%s,%s,%s,%s)")
    cursor = cnx.cursor()

    for i in list_cars:

        cursor.execute(add_car, tuple(i))

    cnx.commit()
    cursor.close()
    cnx.close()


def read_data(config: dict):
    cnx = mysql.connector.connect(**config)
    add_car = (
        "SELECT * FROM car")
    cursor = cnx.cursor()
    cursor.execute(add_car)
    record = cursor.fetchall()
    
    

    cursor.close()
    cnx.close()
    return record