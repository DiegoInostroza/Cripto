from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import string
import random

email = "d.emanu.moli@gmail.com"
password = "aaaaaaaaa"
new_password = "aaaaaaaaa"

index = email.find("@")
size = len(email)
inicio = email[0:index]
index+=1
final = email[index:size]
    

def Crear_Cuenta():
    
    driver = webdriver.Firefox(executable_path=r"C:\geko\geckodriver.exe")
    driver.get("http://www.yapo.cl")

    driver.set_window_size(1300, 700)
    driver.set_window_position(1, 1)
    
    link = driver.find_element_by_link_text("Iniciar sesión")
    link.click()
    
#Recuerda sumarle 23 por la posicion

    
    pyautogui.click(x=675, y=601)
    time.sleep(3)
    
    pyautogui.press('tab',1)
    pyautogui.press('tab',1)
    time.sleep(3)
    pyautogui.typewrite("Diego")
    time.sleep(1)
    pyautogui.press('tab',1)
    pyautogui.press('tab',1)
    
    pyautogui.press('tab',1)
    time.sleep(2)
    pyautogui.typewrite("M")
    pyautogui.press('enter')
    time.sleep(3)
    
    pyautogui.press('tab',1)
    time.sleep(2)
    
##    pyautogui.press('tab',1)
    pyautogui.typewrite("12345678")
    time.sleep(2)
    
    pyautogui.press('tab',1)
    pyautogui.typewrite(inicio)
    pyautogui.hotkey("ctrl","alt","q")
    pyautogui.typewrite(final)
    time.sleep(2)
    
    pyautogui.press('tab',1)
    pyautogui.typewrite(password)
    pyautogui.press('tab',1)
    time.sleep(0.5)
    
    pyautogui.typewrite(password)
    pyautogui.press('tab',1)

    time.sleep(2)

##Agregale 23 al eje de las y
    pyautogui.click(x=231, y=676)
    time.sleep(2)
    
    link = driver.find_element_by_id("edit_profile_btn")
    link.click()

    time.sleep(5)
    driver.close()




def Inicio_Sesión():

    driver = webdriver.Firefox(executable_path=r"C:\geko\geckodriver.exe")
    driver.get("http://www.yapo.cl")


    link = driver.find_element_by_link_text("Iniciar sesión")
    link.click()



    pyautogui.typewrite(inicio)
    pyautogui.hotkey("ctrl","alt","q")
    pyautogui.typewrite(final)
    pyautogui.press('tab',1)
    time.sleep(0.5)
    pyautogui.typewrite(password)   
    pyautogui.press('tab',1)
    time.sleep(0.5)
    pyautogui.press("enter")
    
    time.sleep(5)

    driver.close()

def Restablecer():

    driver = webdriver.Firefox(executable_path=r"C:\geko\geckodriver.exe")
    driver.get("http://www.yapo.cl")

    driver.set_window_size(1300, 700)
    driver.set_window_position(1, 1)
    
    link = driver.find_element_by_link_text("Iniciar sesión")
    link.click()
    time.sleep(1)
##Agregale 23 al eje de las y
    pyautogui.click(x=601, y=515)    
    time.sleep(3)

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)
    search = driver.find_element_by_id("email")
    search.send_keys("d.emanu.moli@gmail.com")
    time.sleep(3)
    search.send_keys(Keys.RETURN)
    
    time.sleep(3)
    
    driver.close()

def Cambiar():
    driver = webdriver.Firefox(executable_path=r"C:\geko\geckodriver.exe")
    driver.get("http://www.yapo.cl")



    link = driver.find_element_by_link_text("Iniciar sesión")
    link.click()
    time.sleep(2)

    pyautogui.write(inicio)
    pyautogui.hotkey("ctrl","alt","q")
    pyautogui.write(final)
    pyautogui.press("tab",1)
    time.sleep(0.5)
    pyautogui.write(new_password)
    time.sleep(0.5)
    pyautogui.press("tab",1)
    pyautogui.press("enter")
    time.sleep(3)
    
    link = driver.find_element_by_partial_link_text("Hola,")
    link.click()
    time.sleep(3)

    link = driver.find_element_by_id("link_profile")
    link.click()
    time.sleep(3)

    for i in range (11):
        pyautogui.press('tab',1)
        time.sleep(0.5)

    pyautogui.press("enter")
    search= driver.find_element_by_id("account_password")
    search.send_keys(password)
    pyautogui.press('tab',1)
    time.sleep(0.5)
    pyautogui.typewrite(password)
    
    for i in range(2):
        pyautogui.press('tab',1)
        time.sleep(0.5)
    
    pyautogui.press("enter")
    
    time.sleep(5)
    driver.close()

def Fuerza_Bruta():
    lenght = len(password)
    index_password = ""
    
    driver = webdriver.Firefox(executable_path=r"C:\geko\geckodriver.exe")
    driver.get("http://www.yapo.cl")

    driver.set_window_size(1300, 700)
    driver.set_window_position(1, 1)
    time.sleep(2)

    link = driver.find_element_by_link_text("Iniciar sesión")
    link.click()

    time.sleep(2)

    pyautogui.typewrite(inicio)
    pyautogui.hotkey("ctrl","alt","q")
    pyautogui.typewrite(final)
    pyautogui.press('tab',1)
    time.sleep(0.5)
       
    for i in range(100):
        index_password = ""
        for i in range(lenght):
            index_password += random.choice(string.ascii_lowercase)
        pyautogui.typewrite(index_password)
        pyautogui.press('tab',1)
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(1)

        pyautogui.click(x=678, y=484)
        pyautogui.press("left",lenght)
        time.sleep(0.5)
        pyautogui.press("delete", lenght)
    
        time.sleep(1)
    
    driver.close()    

#Crear_Cuenta()
#Inicio_Sesión()
#Cambiar()
#Restablecer()
#Fuerza_Bruta()
