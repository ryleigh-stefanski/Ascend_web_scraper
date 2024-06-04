import requests
import re
import selenium
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
	
def scroll_to_bottom(driver):
	elem = driver.find_element(By.TAG_NAME, "html")
	elem.send_keys(Keys.END)
	time.sleep(wait_for_load_time)
	
	#return i = -1 if element found
def check_for_element(driver, i):
	while(i < max_elements_checked):	
		xpath =  "/html/body/div[5]/div/div[2]/div[3]/a[%s]/div/div/div[2]/div[2]" % i
		print("Checking Element #%s..." % i)
		try:
			ele = driver.find_element(By.XPATH, xpath).get_attribute("innerHTML") #gets element that contains text
			#ele.find_element(By.LINK_TEXT, search_key)
			if (ele.find(search_key) != -1):
				print("\nElement Found at Position #%s" % i)
				return -1
				break
			else:
				i += 1
		except:
			print("XPATH failed on element #%s" % i)


search_key = 'Cream'
max_scrolls_to_bottom = 10
max_elements_checked = 125
wait_for_load_time = .25

#selenium bypass age check

try:
	print("Accessing Webpage Via Selenium...")
	driver = webdriver.Chrome()
	driver.get("https://letsascend.com/menu/pa-scranton-menu-med/categories/flower")
	assert "medical Flower" in driver.title
	print("Success")
except:
	print("Failed")

#bypass age check
try:
	print("Bypassing Age Check...")
	driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/button[2]/div[1]').click()
	print("Success")
except:
	print("Failed")


#load all elements
refreshes = max_scrolls_to_bottom

while(refreshes > 0):
	scroll_to_bottom(driver)
	refreshes -= 1
	
check_for_element(driver, 1)	
