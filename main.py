from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
# import sqlite3


# conn = sqlite3.connect("ClimbSpot.db")
# c = conn.cursor()

# c.execute('''CREATE TABLE Spot(grade TEXT, name TEXT, description TEXT, tags TEXT)''')
spotsList = []

for x in range(1, 9):

    url = 'https://www.thecrag.com/en/climbing/canada/quebec/quebec-city/routes/?sortby=at,desc&page='
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get(url+str(x))
    

    grades  = driver.find_elements(By.CLASS_NAME, "pull-right")
    routes = driver.find_elements(By.CLASS_NAME, "route")
    # desc = driver.find_elements(By.CLASS_NAME, "markdown")
    tags = driver.find_elements(By.CLASS_NAME, "tags")

    for (e, s, r) in zip(grades,routes,tags):
        spotItem = {
            'Grade': e.text,
            'Name': s.text,
            'Tags': r.text,
        }

        spotsList.append(spotItem)
        time.sleep(0.03)
        



df = pd.DataFrame(spotsList)
print('Lenght on the list: ',len(spotsList))
print(df.head())

df.to_csv('spots.csv')

driver.close()

    # regions = driver.find_elements(By.XPATH, "//span[contains(@class,'crumbtrail-partial')]/span[1]")
    # for region in regions:
    #     if region.text not in spotsList:
    #         spotsList.append(region.text)
        
    