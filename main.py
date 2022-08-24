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
for x in range(1, 3):

    url = 'https://www.thecrag.com/en/climbing/canada/routes?page='
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(url+str(x))

    rows = driver.find_elements(By.CSS_SELECTOR, 'tr.actionable')

    for td in rows: 
       
        states = td.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[3]/div/table/tbody/tr[2]/td/span/span[1]').text
        area = td.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[3]/div/table/tbody/tr[2]/td/span/span[2]').text
        crag = td.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[3]/div/table/tbody/tr[2]/td/span/span[3]').text
        grades  = td.find_element(By.CLASS_NAME, "pull-right").text
        routes = td.find_element(By.CLASS_NAME, "route").text
        tags = td.find_element(By.CLASS_NAME, "tags ").text

        try: 
            desc = td.find_element(By.CLASS_NAME, "markdown").text
        except:
            desc = "No description."

        spotItem = {
            'country': 'canada',
            'state': states,
            'area': area,
            'crag': crag,
            'route': {
                 'name': routes,
                'grade': grades,
                'description': desc,
                'tags': tags
            },
            'done': False,
           
        }

        time.sleep(0.03)
        spotLists.append(spotItem)




df = pd.DataFrame(spotLists)

df.to_json('spot.json', orient='records')

driver.close()

    # regions = driver.find_elements(By.XPATH, "//span[contains(@class,'crumbtrail-partial')]/span[1]")
    # for region in regions:
    #     if region.text not in spotsList:
    #         spotsList.append(region.text)
        
    