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

spotLists = []
for x in range(1, 2):

    url = 'https://www.thecrag.com/en/climbing/canada/routes?page='
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get(url+str(x))
    # state = driver.find_elements(By.XPATH, '//*[@id="wrapper"]/div/div/div/table/tbody/tr/td/span/span[contains(@href, "/canada")]')
    grades  = driver.find_elements(By.CLASS_NAME, "pull-right")
    routes = driver.find_elements(By.CLASS_NAME, "route")
    desc = driver.find_elements(By.CLASS_NAME, "markdown")
    tags = driver.find_elements(By.CLASS_NAME, "tags")
    
    for (e, s, y, t) in zip(grades,routes, tags, desc):
    
        
        spotItem = {
            'country': 'canada',
            # 'state': g.text,
            # 'crag': g.text.split()[1],
            'spot': {
                 'name': s.text,
                'grade': e.text,
                # 'description':,
                'tags': y.text
            },
            'done': False,
           
        }


        time.sleep(0.03)
        spotLists.append(spotItem)


df = pd.DataFrame(spotLists)
print(df.head())

df.to_json('spot.json', orient='records')

driver.close()

    # regions = driver.find_elements(By.XPATH, "//span[contains(@class,'crumbtrail-partial')]/span[1]")
    # for region in regions:
    #     if region.text not in spotsList:
    #         spotsList.append(region.text)
        
    