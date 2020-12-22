#! python3
# Auto play 2048 game

import logging, time, requests, sys
from selenium import webdriver

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable()

url = ''

# Red the terminal
helpMenssage = 'Write the url to verify links (example: python3 main.py "https://github.com/")'
if len(sys.argv) == 2:  
    url = sys.argv[1]
else: 
    print (helpMenssage)
    sys.exit()

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
