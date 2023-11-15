from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re


def scrool_web(address, number_page=2):

    browers = webdriver.Firefox()
    browers.get(address)
    browers.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    ItemTargetCount = number_page

    li_names = []
    li_prices = []
    li_details = []
    li_km = []
    li_model = []
    li_year = []

    while ItemTargetCount > 0:

        ItemTargetCount -= 1
        browers.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        CarNames = browers.find_elements(By.CLASS_NAME, 'bama-ad__title')
        CarPrices = browers.find_elements(
            By.CLASS_NAME, 'bama-ad__price-holder')
        CarDetails = browers.find_elements(
            By.CLASS_NAME, 'bama-ad__detail-row')

        for i in CarNames:
            li_names.append(i.text)
        for i in CarPrices:
            li_prices.append(i.text)
        for i in CarDetails:
            li_details.append(i.text)

        time.sleep(1)

    browers.close()
    for k in li_details:
        l = k.split()
        if l[1] == 'صفر':
            try:
                li_year.append(l[0])
                li_km.append(0)
                li_model.append(l[3])
            except:
                li_model.append('ساده')
        else:
            try:
                li_year.append(l[0])
                li_km.append(l[1])
                li_model.append(l[3])
            except:
                li_model.append('ساده')

    li_names = regex_name(li_names)
    return ListToDict(li_names, li_km, li_model, li_prices, li_year)


def ListToDict(name: list, km: list, mode: list, price: list, year: list):
    list_cars = []

    for n, p, k, m, y in zip(name, price, km, mode, year):
        try:
            list_cars.append([n, p, k, m, y])
        except:
            continue

    return list_cars


def regex_name(li_names: list):
    pattern = '، (.*)'
    len_list = len(li_names)

    for i in range(len_list):
        li_names[i] = re.findall(pattern, li_names[i])[0]

    return li_names


# h = scrool_web("https://bama.ir/car/pride?seller=1")
# print(h)
