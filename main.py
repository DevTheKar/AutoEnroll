from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


oasis.find_element(By.ID, "i0116").send_keys("devthakkar@usf.edu") # Email
time.sleep(5)

oasis.find_element(By.ID, "idSIButton9").click() #Next Button
time.sleep(5)

oasis.find_element(By.ID, "i0118").send_keys("Dnrnt*5475%$&%") # Password
time.sleep(5)

oasis.find_element(By.ID, "idSIButton9").click() # Sign In button
time.sleep(5)

value = oasis.find_element(By.ID, "idRichContext_DisplaySign")
display_text()

oasis.find_element(By.ID, "idSIButton9").click() #Yes Button to Do you want to reduce sign in
time.sleep(5)

links = oasis.find_elements(By.CLASS_NAME, "kgo-publish-tile-action")

for link in links:
    if link.get_attribute("href") == "https://bannersso.usf.edu/ssomanager/c/SSB":
        link.click()
        break    
time.sleep(15)

handles = oasis.window_handles
oasis.switch_to.window(handles[1])
oasis.find_element(By.LINK_TEXT, "Student").click() # Student Button
time.sleep(1.5)
oasis.find_element(By.LINK_TEXT, "Registration").click() # Student Button
time.sleep(1.5)
oasis.find_element(By.LINK_TEXT, "Class Schedule Search").click() # Student Button
time.sleep(1.5)

time.sleep(5)
oasis.close()