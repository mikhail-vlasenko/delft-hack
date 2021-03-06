from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import preferences.price as price

import preferences.parse_utils as parse_utils

countries = parse_utils.import_csv()
actual_data = price.save(countries)

with open('data/religion.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|')
    for row in actual_data:
        print(row)
        writer.writerow([row[0], row[1]])

print(actual_data)

# source_city = "Amsterdam"
# num_people = 1
# budget = 1000000
# # dest_city = "New York"
# travel_time = 8
# climate = "warm"
# type = "city"
# driver = webdriver.Chrome()
# driver.get("https://www.google.com/travel/explore")
# element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "SD4Ugf"))
#     )
# city_selector = driver.find_element(by=By.CLASS_NAME, value="SD4Ugf")
# filter_selector = driver.find_element(by=By.CLASS_NAME, value="o1mPMd bwFTlc EA71Tc")
# filters = filter_selector
# cities = city_selector.find_elements(By.XPATH, ".//li")\
# # for city in cities:
# #     inner_city = city.find_element(by=By.XPATH, value="./div[1]/div[2]")
# #     name = inner_city.find_element(by=By.XPATH, value="./div[1]/h3")
# #     avg_flight_price = inner_city.find_element(by=By.XPATH, value="./div[2]/div/div/span")
# #     avg_hotel_price = inner_city.find_element(by=By.XPATH, value="./div[2]/div[2]/span")
# #     avg_flight_time = inner_city.find_element(by=By.XPATH, value="./div[2]/div[1]/div[2]/span[3]")
# #     print(name.text, avg_flight_price.text, avg_hotel_price.text, avg_flight_time.text)
# #
# # print(len(cities))
# # print(elem.find_elements_by_css_selector("*"))
# driver.close()

