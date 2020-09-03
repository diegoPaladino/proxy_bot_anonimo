#proxy_anonimous_bot
#not sucessful
#link of hide my name = https://hidemy.name/en/proxy-list/?type=s#list
#link of ip check: https://www.myip.com


import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

PROXY = '169.57.157.148:80'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={PROXY}')

# driver = webdriver.Chrome(
#     ChromeDriverManager().install(), options=chrome_options)
# driver = webdriver.Chrome('C://Users//diego//OneDrive//Desktop//DESKTOP//PROGRAMAS//WEB_DRIVERS//CHROME_DRIVER//chromedriver.exe')
# driver = 'C://Users//diego//OneDrive//Desktop//DESKTOP//PROGRAMAS//WEB_DRIVERS//MOZILA_DRIVER//geckodriver.exe'
driver = 'C://Users//diego//OneDrive//Desktop//DESKTOP//PROGRAMAS//WEB_DRIVERS//MOZILA_DRIVER'
driver = webdriver.Firefox()
driver.get('https://https://www.myip.com/')
time.sleep(100)