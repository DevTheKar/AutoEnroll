from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

with open('data.txt', 'r') as file:
    lines = [line.strip() for line in file]


def display_text():
    text_viewer = webdriver.Chrome()
    text_viewer.get("https://large-type.com/#")
    text_elem = WebDriverWait(text_viewer, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "inputbox"))) # Input Text Box
    text_elem.clear()
    text_elem.send_keys(value.text)
    while True:
        if WebDriverWait(oasis, 60).until(EC.presence_of_element_located((By.ID, "idSIButton9"))) == True: # Check if next page loaded from 2FA
            text_viewer.close()
            return
    
    

oasis = webdriver.Chrome()


oasis.get("https://my.usf.edu/myusf/home_myusf/index")
time.sleep(5)

WebDriverWait(oasis, 60).until(EC.presence_of_element_located((By.ID, "i0116"))).send_keys(lines[0]) # Email
oasis.find_element(By.ID, "idSIButton9").click() #Next Button

time.sleep(1)
WebDriverWait(oasis, 60).until(EC.presence_of_element_located((By.ID, "i0118"))).send_keys(lines[1]) # Password
oasis.find_element(By.ID, "idSIButton9").click() # Sign In button
time.sleep(2)


value = WebDriverWait(oasis, 60).until(EC.presence_of_element_located((By.ID, "idRichContext_DisplaySign"))) # 2FA Code
display_text()

oasis.find_element(By.ID, "idSIButton9").click() #Yes Button to Do you want to reduce sign in


links = value = WebDriverWait(oasis, 60).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "kgo-publish-tile-action"))) # Pressing OASIS

for link in links:
    if link.get_attribute("href") == "https://bannersso.usf.edu/ssomanager/c/SSB":
        link.click()
        break    

handles = oasis.window_handles
oasis.switch_to.window(handles[1])

WebDriverWait(oasis, 60).until(EC.presence_of_element_located((By.LINK_TEXT, "Student"))).click() # Student Button
WebDriverWait(oasis, 60).until(EC.presence_of_element_located((By.LINK_TEXT, "Registration"))).click() # Registration Button
WebDriverWait(oasis, 60).until(EC.presence_of_element_located((By.LINK_TEXT, "Class Schedule Search"))).click() # Class Schedule Search Button


dropdown = WebDriverWait(oasis, 60).until(EC.presence_of_element_located((By.NAME, "p_term")))# Class Schedule Search Button
select = Select(dropdown)
select.select_by_value(lines[2])
oasis.find_element(By.XPATH, "//input[@type='submit' and @value='Submit']").click()
time.sleep(5)


time.sleep(5)
oasis.close()