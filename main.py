from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

urls = ["https://devthekar.github.io/AutoEnrollFrontend/", "https://devthekar.github.io/AutoEnrollFrontend/incorrectemail", "https://devthekar.github.io/AutoEnrollFrontend/incorrectpassword"]
counter = 0

def login_to_application():
    global urls, counter
    user_input = webdriver.Chrome()
    user_input.maximize_window()
    user_input.get(urls[counter])
    email = WebDriverWait(user_input, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "email"))).text # User email
    password = user_input.find_element(By.CLASS_NAME, "password").text
    semester = user_input.find_element(By.CLASS_NAME, "semester").get_attribute("value")
    course_name = user_input.find_element(By.CLASS_NAME, "coursename").text
    crn = user_input.find_element(By.CLASS_NAME, "crnnumber").text
    user_input.close()
    return email, password, semester, course_name, crn


def display_text(value):
    text_viewer = webdriver.Chrome()
    text_viewer.maximize_window()
    text_viewer.get("https://large-type.com/#")
    text_elem = WebDriverWait(text_viewer, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "inputbox"))) # Input Text Box
    text_elem.clear()
    text_elem.send_keys(value)
    WebDriverWait(oasis, 60).until(EC.visibility_of_element_located((By.ID, "idSIButton9")))
    text_viewer.close()



def navigate_to_oasis(email, password):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    oasis = webdriver.Chrome(options=chrome_options)
    oasis.get("https://my.usf.edu/myusf/home_myusf/index")
    WebDriverWait(oasis, 60).until(EC.presence_of_element_located((By.ID, "i0116"))).send_keys(email) # Email
    oasis.find_element(By.ID, "idSIButton9").click() #Next Button
    time.sleep(1)
    global counter
    
    # Check if there's an error message for incorrect username
    try:
        error_message = oasis.find_element(By.ID, "usernameError")
        counter = 1
        oasis.quit()  # Close the browser
        return None
    except NoSuchElementException:
        WebDriverWait(oasis, 60).until(EC.presence_of_element_located((By.ID, "i0118"))).send_keys(password) # Password
        oasis.find_element(By.ID, "idSIButton9").click() # Sign In button
        
        # Check if there's an error message for incorrect password
        try:
            error_message = oasis.find_element(By.ID, "passwordError")
            counter = 2
            oasis.quit()  # Close the browser
            return None
        except NoSuchElementException:
            time.sleep(2)
            return oasis


def find_and_register_class(oasis, semester, course_name, crn):
    links = WebDriverWait(oasis, 60).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "kgo-publish-tile-action"))) # Pressing OASIS
    for link in links:
        if link.get_attribute("href") == "https://bannersso.usf.edu/ssomanager/c/SSB":
            link.click()
            break    

    handles = oasis.window_handles
    oasis.switch_to.window(handles[1])

    WebDriverWait(oasis, 600).until(EC.presence_of_element_located((By.LINK_TEXT, "Student"))).click() # Student Button
    WebDriverWait(oasis, 60).until(EC.presence_of_element_located((By.LINK_TEXT, "Registration"))).click() # Registration Button
    WebDriverWait(oasis, 60).until(EC.presence_of_element_located((By.LINK_TEXT, "Class Schedule Search"))).click() # Class Schedule Search Button

    dropdown = WebDriverWait(oasis, 60).until(EC.presence_of_element_located((By.NAME, "p_term")))# Class Schedule Search Button
    select = Select(dropdown)
    select.select_by_value(semester) # Semester
    oasis.find_element(By.XPATH, "//input[@type='submit' and @value='Submit']").click()

    WebDriverWait(oasis, 60).until(EC.presence_of_element_located((By.NAME, "sel_title"))).send_keys(course_name) # Class name
    oasis.find_element(By.NAME, "open_only").click()
    time.sleep(2)
    oasis.find_element(By.NAME, "SUB_BTN").click() #Submit search
    time.sleep(1.5)

    total_seats = 0

    while True:
        table_data = oasis.find_elements(By.CLASS_NAME, "dddefault")
        count = 0
        crn_counter = 1
        seats_counter = 13
        for data in table_data:
            if count == crn_counter:
                if data.text == crn:
                    crn_counter += 20
                else:
                    continue
            if count == seats_counter:
                total_seats = int(data.text)
                seats_counter += 20
                break
            count += 1
        if total_seats > 0:
            print("class added")
            break
        else:
            oasis.refresh()
            print("no seats")
            continue

    courses = oasis.find_elements(By.NAME, "sel_crn")
    for course in courses:
        if course.get_attribute("value") == f"{crn} {semester}":
            course.click()
    time.sleep(1)

    buttons = oasis.find_elements(By.NAME, "ADD_BTN")
    for button in buttons:
        if button.get_attribute("value") == "Register":
            button.click()
            break
    time.sleep(3)
    oasis.close()



if __name__ == "__main__":
    while True:
        email, password, semester, course_name, crn = login_to_application()
        oasis = navigate_to_oasis(email, password)
        if oasis is not None:
            value = WebDriverWait(oasis, 60).until(EC.presence_of_element_located((By.ID, "idRichContext_DisplaySign"))) # 2FA Code
            display_text(value.text)
            oasis.find_element(By.ID, "idSIButton9").click() #Yes Button to Do you want to reduce sign in
            find_and_register_class(oasis, semester, course_name, crn)
            break
        else:
            continue