import dataweb as dv
import data_sql as dsql
import json


config = read_jason('pass_sql.json')

q_update = input("update list? (y/n): ")
if q_update == 'y':
    input_number_page = input(
        'please enter number page for update data(default = 2): ')

    list_cars = dv.scrool_web(
        'https://bama.ir/car/pride?seller=1', int(input_number_page))

    dsql.add_to_table(list_cars, config)


elif q_update == 'n':
    menu = input("1_GUSTE\n2_Show Cars\n")
    if menu == '1':
        cars = (dsql.read_data(config))
        pass
    else:
        cars = (dsql.read_data(config))
        for n, p, k, m, y in cars:
            print(n, m, y, k, p)


def read_jason(addres):
    config = {}
    with open(addres, "r") as handler:
        info = json.load(handler)

    config["user"] = info["user"]
    config["password"] = info["password"]
    config["host"] = info["host"]
    config["database"] = info["database"]
    return config
