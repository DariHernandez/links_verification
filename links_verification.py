#! python3
# Auto play 2048 game

import logging, time, requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable()

url = 'https://platzi.com/'

browser = webdriver.Chrome()
browser.get(url)

print ('Searching links...')

#Whait five seconds
time.sleep(5)

#Find link elements
my_element_CSS = 'a[href]'
elemLinks = browser.find_elements_by_css_selector(my_element_CSS)

#Save link in a list
for elemLink in elemLinks:  
    link = elemLink.get_attribute('href')
    try: 
        res = requests.get(link)
        res.raise_for_status()
        print ('Functional link: ' + link)
    except Exception as exc:
        print ('\tNOT FUNCTIONAL LINK: ' + link + '\t The problem was: %s' % (exc))
    
browser.close()
