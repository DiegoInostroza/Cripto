from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import string
import random

email = "d.emanuel.mol@gmail.com"
password = "aaaaaaaa"
new_password = "aaaaaaaa"

def Crear_Cuenta():
    

    driver = webdriver.Firefox(executable_path=r"C:\geko\geckodriver.exe")
    driver.get("http://www.eljueves.es")

    driver.set_window_size(1300, 700)
    driver.set_window_position(1, 1)
    time.sleep(2)

    link = driver.find_element_by_link_text("Iniciar sesión")
    link.click()
    time.sleep(2)

    link = driver.find_element_by_link_text("Regístrate")
    link.click()
    time.sleep(1)

    search = driver.find_element_by_id("email")
    search.send_keys(email)
    search.send_keys(Keys.RETURN)
    time.sleep(0.5)

    search = driver.find_element_by_id("password")
    search.send_keys(password)
    search.send_keys(Keys.RETURN)
    time.sleep(0.5)

    search = driver.find_element_by_id("password-confirm")
    search.send_keys(password)
    search.send_keys(Keys.RETURN)
    time.sleep(0.5)

    for i in range(5):
        pyautogui.press("tab",1)
        time.sleep(0.5)
        
    
    pyautogui.click(x=855, y=611)
    time.sleep(1)
    
    pyautogui.click(x=855, y=652)
    time.sleep(1)

    pyautogui.click(x=952, y=514)
    time.sleep(2)

    pyautogui.click(x=640, y=537)
    '''        
    link = driver.find_element_by_id("accept")
    link.click()
    time.sleep(1)

    link = driver.find_element_by_id("newsletter_opt_in")
    link.click()
    time.sleep(1)
    '''
    
    time.sleep(5)
    driver.close()

def Inicio_Sesion():

    driver = webdriver.Firefox(executable_path=r"C:\geko\geckodriver.exe")
    driver.get("http://www.eljueves.es")

    link = driver.find_element_by_link_text("Iniciar sesión")
    link.click()

    search = driver.find_element_by_id("email")
    search.send_keys(email)
    search.send_keys(Keys.RETURN)


    search = driver.find_element_by_id("password")
    search.send_keys(password)
    search.send_keys(Keys.RETURN)
    time.sleep(1)


    pyautogui.press('tab',1)
    pyautogui.press("enter")

    time.sleep(5)

    driver.close()

def Restablecer():
    
    driver = webdriver.Firefox(executable_path=r"C:\geko\geckodriver.exe")
    driver.get("http://www.eljueves.es")

    link = driver.find_element_by_link_text("Iniciar sesión")
    link.click()
    time.sleep(3)

    link = driver.find_element_by_id("password")
    link.click()

    for i in range(3):
        pyautogui.press("tab",1)
        time.sleep(0.5)

    pyautogui.press("enter")
    time.sleep(3)

    search = driver.find_element_by_id("email")
    search.send_keys("d.emanuel.mol@gmail.com")
    time.sleep(2)
    pyautogui.press("tab",1)
    pyautogui.press("enter")

    time.sleep(5)
    driver.close()
    
    
def Cambio():

    driver = webdriver.Firefox(executable_path=r"C:\geko\geckodriver.exe")
    driver.get("http://www.eljueves.es")


    link = driver.find_element_by_link_text("Iniciar sesión")
    link.click()

    search = driver.find_element_by_id("email")
    search.send_keys(email)
    search.send_keys(Keys.RETURN)


    search = driver.find_element_by_id("password")
    search.send_keys(password)
    search.send_keys(Keys.RETURN)
    time.sleep(3)

    pyautogui.press('tab',1)
    pyautogui.press("enter")
    
    time.sleep(3)
    driver.refresh()
    time.sleep(8)
    link = driver.find_element_by_link_text("Usuario")
    link.click()
    time.sleep(3)


    driver.set_window_size(1300, 700)
    driver.set_window_position(1, 1)
    time.sleep(2)
    

    pyautogui.click(x=51, y=353)
    time.sleep(1)

    for i in range(6):
        pyautogui.press("tab",1)
        time.sleep(0.5)
    
    pyautogui.press("enter")
    time.sleep(3)

    '''
    search = driver.find_element_by_id("password")
    search.send_keys(password)
    search.send_keys(Keys.RETURN)
    time.sleep(1)

    search = driver.find_element_by_id("password-confirm")
    search.send_keys(password)
    search.send_keys(Keys.RETURN)
    time.sleep(1)
    '''
    for i in range(3):
        pyautogui.press("tab",1)
        time.sleep(0.5)

    pyautogui.typewrite(password)
    pyautogui.press("tab",1)
    time.sleep(2)
    
    pyautogui.typewrite(password)
    pyautogui.press("tab",1)
    time.sleep(2)
    pyautogui.press("enter")


    time.sleep(3)
    driver.close()


def Fuerza_Bruta():
    lenght = len(password)
    
    driver = webdriver.Firefox(executable_path=r"C:\geko\geckodriver.exe")
    driver.get("http://www.eljueves.es")
    URL = driver.current_url
    time.sleep(1)

    link = driver.find_element_by_link_text("Iniciar sesión")
    link.click()


    search = driver.find_element_by_id("email")
    search.send_keys(email)
    search.send_keys(Keys.RETURN)

    
    NEW_URL = driver.current_url
    index = NEW_URL[0:44]

    for i in range(100):

        index_password = ""
        
        for i in range(lenght):
            index_password += random.choice(string.ascii_lowercase)
    
        time.sleep(1)
        
        search = driver.find_element_by_id("password")
        search.send_keys(index_password)
        search.send_keys(Keys.RETURN)
        pyautogui.press('tab',1)
        time.sleep(0.5)
        
        pyautogui.press("enter")
        time.sleep(2)

        URL = driver.current_url
        
        if (index not in URL):
            driver.back()
            time.sleep(1)
            
        elif(index in URL):
            driver.find_element_by_id("password").clear()
            time.sleep(1)
            
    driver.close()  
    


#Crear_Cuenta()
#Inicio_Sesion()
#Restablecer()
#Cambio()
Fuerza_Bruta()

