from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome()

#Opening the website
website = "https://www.wikipedia.org/"
browser.get(website)
#Changing the search language to English
languageSelection = browser.find_element(By.XPATH, "//select[@id = 'searchLanguage']")
languageSelection.click()
englishOption = browser.find_element(By.XPATH, "//option[@lang= 'en']")
browser.execute_script("arguments[0].scrollIntoView();", englishOption)
englishOption.click()
#Finding the search box area and sending the search input in
searchBox = browser.find_element(By.XPATH, "//input[@id = 'searchInput']")
searchBox.send_keys('Mustafa Kemal Ataturk')
#Clicking the search button
searchButton = browser.find_element(By.XPATH, "//button[@type = 'submit']")
searchButton.click()
#Getting the page source in html and extracting the number of headlines out by using the BeautifulSoup class in python
sourceHtml = browser.page_source
sourceText = BeautifulSoup(sourceHtml, 'html.parser')
sourceText.prettify()
headlines = sourceText.find_all("span",{"class": "mw-headline"})

for headline in headlines:
    print(headline.get('id'))

time.sleep(5)
browser.close()