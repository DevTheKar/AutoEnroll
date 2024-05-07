from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def display_text():
    text_viewer = webdriver.Chrome()
    text_viewer.get("https://large-type.com/#")
    time.sleep(2)
    text_elem = text_viewer.find_element(By.CLASS_NAME, "inputbox")
    text_elem.clear()
    text_elem.send_keys(value.text)
    time.sleep(30)
    text_viewer.close()
    

oasis = webdriver.Chrome()


oasis.get("https://my.usf.edu/myusf/home_myusf/index")
time.sleep(5)


elem = oasis.find_element(By.ID, "i0116")
elem.send_keys("devthakkar@usf.edu")
time.sleep(5)

next_button = oasis.find_element(By.ID, "idSIButton9")
next_button.click()
time.sleep(5)

elem = oasis.find_element(By.ID, "i0118")
elem.send_keys("Dnrnt*5475%$&%")
time.sleep(5)

sign_in_button = oasis.find_element(By.ID, "idSIButton9")
sign_in_button.click()
time.sleep(5)

value = oasis.find_element(By.ID, "idRichContext_DisplaySign")
display_text()

yes_button = oasis.find_element(By.ID, "idSIButton9")
yes_button.click()
time.sleep(5)

links = oasis.find_elements(By.CLASS_NAME, "kgo-publish-tile-action")

# Iterate through the links
for link in links:
    # Check if the link's href attribute matches the desired URL
    if link.get_attribute("href") == "https://bannersso.usf.edu/ssomanager/c/SSB":
        # Click the link
        link.click()
        break
time.sleep(20)

oasis.close()