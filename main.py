from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from dotenv import find_dotenv,load_dotenv

dotenv_path=find_dotenv()
load_dotenv(dotenv_path)

USERNAME=os.getenv("username")
PASSWORD=os.getenv("password")


con=webdriver.ChromeOptions()
con.add_experimental_option("detach",True)
class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver=webdriver.Chrome(options=con)
        self.down=0
        self.up=0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go=self.driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.driver.execute_script("arguments[0].click();", go)
        sleep(60)
        self.down=self.driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up=self.driver.find_element(By.XPATH,value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.up)
        print(self.down)
    def tweet_to_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        sleep(5)
        phone=self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        phone.send_keys(USERNAME,Keys.ENTER)
        sleep(3)
        pwds=self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        pwds.send_keys(PASSWORD,Keys.ENTER)
        sleep(5)
        text=self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        text.send_keys(f"Heyy my internet provider why is my internet speed {self.up}/{self.down} when i have paid for 30/100 ")
        sleep(2)
        post=self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
        self.driver.execute_script("arguments[0].click();", post)


bot=InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_to_provider()