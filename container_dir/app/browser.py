from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def load_cookies_whatsapp(driver):
    driver.get("https://web.whatsapp.com/")
    with open('cookies.txt') as f:
        cookies = f.read()
    for cookie in eval(cookies):
        driver.add_cookie(cookie)

def save_cookies(driver, service):
    with open('cookies.txt' + service, 'w') as f:
        f.write(str(driver.get_cookies()))

driver = webdriver.Chrome()

def load_cookies_telegram(driver):
    driver.get("https://web.whatsapp.com/")
    with open('cookies.txt') as f:
        cookies = f.read()
    for cookie in eval(cookies):
        driver.add_cookie(cookie)

def send_whatsapp_message(contact_name, message):
    load_cookies_whatsapp(driver)
    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(contact_name)
    time.sleep(2)
    contact = driver.find_element_by_xpath('//span[contains(@title,"' + contact_name + '")]')
    contact.click()
    time.sleep(2)
    input_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
    input_box.send_keys(message)
    input_box.send_keys(Keys.ENTER)
    save_cookies("whatsapp")

def send_telegram_message(contact_name, message):
    load_cookies_telegram(driver)
    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(contact_name)
    time.sleep(2)
    contact = driver.find_element_by_xpath('//span[contains(@title,"' + contact_name + '")]')
    contact.click()
    time.sleep(2)
    input_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
    input_box.send_keys(message)
    input_box.send_keys(Keys.ENTER)
    save_cookies("whatsapp")

def login_yandexdisk(driver, username, password):
    driver.get("https://disk.yandex.com/")
    
    login_button = driver.find_element(By.XPATH, '//a[@href="https://passport.yandex.com"]')
    login_button.click()
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'passp-field-login'))
    )
    
    username_input = driver.find_element(By.ID, 'passp-field-login')
    username_input.send_keys(username)
    username_input.send_keys(Keys.RETURN)
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'passp-field-passwd'))
    )
    
    password_input = driver.find_element(By.ID, 'passp-field-passwd')
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'listing-item__info')]"))
    )

def upload_file(driver, file_path):
    upload_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Upload')]")
    upload_button.click()

    file_input = driver.find_element(By.XPATH, "//input[@type='file']")
    file_input.send_keys(file_path)
    time.sleep(10)

def delete_file_yandexdisk(driver, file_name):
    file_element = driver.find_element(By.XPATH, f"//span[contains(text(), '{file_name}')]")
    file_element.click()
    delete_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Delete')]")
    delete_button.click()
    confirm_delete_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Delete')]")
    confirm_delete_button.click()
    time.sleep(5)

def move_file_yandexdisk(driver, file_name, destination_folder):
    file_element = driver.find_element(By.XPATH, f"//span[contains(text(), '{file_name}')]")
    file_element.click()

    move_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Move')]")
    move_button.click()

    destination_element = driver.find_element(By.XPATH, f"//span[contains(text(), '{destination_folder}')]")
    destination_element.click()

    confirm_move_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Move')]")
    confirm_move_button.click()

    time.sleep(5)
