import data_sql as data
from sklearn import tree
import json


def read_jason(addres):
    config = {}
    with open(addres, "r") as handler:
        info = json.load(handler)

    config["user"] = info["user"]
    config["password"] = info["password"]
    config["host"] = info["host"]
    config["database"] = info["database"]
    return config


def awnser_price():
    new_car = []
    name = input("please enter name: ")
    km = input("please enter km: \n(karkarde = 1):")
    year = input("please enter year: ")
    model = input(
        "please enter model: \n(se = 0, sx = 1, dande = 2, sade = 3, ex = 4 , sl = 5 , el = 6 ):")
    new_car.append([name, km, model, year])

    return new_car


def inpout_data(cars):
    li = []
    li_out = []

    for n, p, k, m, y in cars:
        li.append([n, k, m, y])
        li_out.append(p)

    return (li, li_out)


config = read_jason("pass_sql.json")


def learn():

    cars = data.read_data(config)
    x, y = inpout_data(cars)

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(x, y)

    new_car = awnser_price()
    awnser = clf.predict(new_car)

    return awnser
