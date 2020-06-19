from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

chrome_option = Options()
chrome_option.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_option)

#driver = webdriver.Chrome()

def tear(b):
    soup = BeautifulSoup(b, "html.parser")
    div = soup.find_all('div', {'class':'user-details'})
    links = []
    for ele in div:
        f = str(ele.find_all('a'))
        f = f[10:]
        x = f.index('>')
        f = f[:x-1]
        links += ["http://www.stackoverflow.com" + f]
    return links

file = open('source.txt', 'a')

page = 1838 #start
while page<=333769: #333769 total
    chrome_option = Options()
    chrome_option.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_option)
    driver.get("https://stackoverflow.com/users?page=" +str(page)+ "&tab=Reputation&filter=year")
    source = driver.page_source
    link = tear(source)
    for i in link:
        file.write(i+'\n')
    driver.close()
    page += 1
    driver.quit()
