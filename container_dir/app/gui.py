import time
import pyautogui
import os


def send_whatsapp_message(contact_phone, message, attachment) -> bool:
    os.system('open whatsapp-desktop')
    search_box_location = pyautogui.locateCenterOnScreen('gui_images/new_contact_whatsapp.png')
    if search_box_location is None:
        return False
    pyautogui.click(search_box_location)
    pyautogui.write(contact_phone)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    input_box_location = pyautogui.locateCenterOnScreen('inputbox_whatsapp.png')
    if input_box_location is None:
        return False
    pyautogui.click(input_box_location)
    pyautogui.write(message)
    pyautogui.press('enter')
    return True


def send_telegram_message(contact, message, attachment) -> bool:
    os.system('open telegram')
    search_box_location = pyautogui.locateCenterOnScreen('gui_images/new_contact_whatsapp.png')
    if search_box_location is None:
        return False
    pyautogui.click(search_box_location)
    pyautogui.write(contact)
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(1)

    input_box_location = pyautogui.locateCenterOnScreen('inputbox_telegram.png')
    if input_box_location is None:
        return False
    pyautogui.click(input_box_location)
    pyautogui.write(message)
    pyautogui.press('enter')
    return True
