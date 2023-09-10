from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

class FormAutomation:
    def automation(self,year,idpr,idver,nos,data1,sport):
        web = webdriver.Chrome() #chrome driver 115 and above does not require you to mention path in this
        url = os.getenv('weburl')
        web.get(url)
        time.sleep(2)
        filepath = os.getenv('data_file_path')
        dataframe1 = pd.read_excel(filepath)
        r = pd.DataFrame()
        X = []
        for i in range(nos):
            X.append(data1[i][0])

        for x in X:
            r = pd.concat([r, dataframe1[dataframe1['roll'] == x]])
        print(r)
        i = 0
        for index, row in r.iterrows():

            try:
                roll = row['roll']
                name = row['name']
                gr = row['gr']
                gt = web.find_element(by=By.XPATH,
                                      value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
                gt.send_keys(sport)
                # //*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input
                n = web.find_element(by=By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
                n.send_keys(name)
                y = web.find_element(by=By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
                y.send_keys(year)
                idv = web.find_element(by=By.XPATH,
                                       value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
                idv.send_keys(idver)
                idp = web.find_element(by=By.XPATH,
                                       value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
                idp.send_keys(idpr)
                if data1[i][1] == 1:
                    p = "Paid"
                else:
                    p = "Not Paid"
                pds = web.find_element(by=By.XPATH,
                                       value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
                pds.send_keys(p)
                c = web.find_element(by=By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
                c.send_keys(gr)
                submit = web.find_element(by=By.XPATH,
                                          value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
                submit.click()
                sar = web.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
                sar.click()
            except:
                print("element not found")

            i += 1