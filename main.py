from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from datetime import datetime,timedelta
from environs import Env
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



env = Env()
env.read_env()  # read .env file, if it exists
# required variables
user_name = env("user_name")  
password = env("password") 
driver_path = env("driver_path",'chromedriver.exe')  

def descarga(soc):
    driver = webdriver.Chrome(driver_path) # Abrimos en Chrome

    #   Ingresar a SAP
    driver.get("https://dims4prdci.dimerc.cl:8001/sap/bc/ui5_ui5/ui2/ushell/shells/abap/FioriLaunchpad.html?sap-client=300&sap-language=ES#Customer-manageLineItems?sap-ui-tech-hint=GUI")
    element = driver.find_element_by_id("USERNAME_FIELD-inner")
    element.send_keys(user_name)
    element = driver.find_element_by_id("PASSWORD_FIELD-inner")
    element.send_keys(password)
    element.send_keys(Keys.RETURN)

    #   Ingresar a la transaccion
    driver.implicitly_wait(20)
    driver.switch_to.frame("application-Customer-manageLineItems") # Frames SAP
    driver.switch_to.frame("ITSFRAME1")

    # Llenar datos
    element = driver.find_element_by_id("M0:46:::2:34") # Sociedad
    element.send_keys(soc)
    #element = driver.find_element_by_id("M0:46:::2:59")
    #element.send_keys(soc2)
    ayer = datetime.today() - timedelta(days=1)
    d1 = ayer.strftime("%d.%m.%Y")
    element = driver.find_element_by_id("M0:46:::12:34")    # Fecha
    element.click()
    element.clear()
    element.send_keys(d1)
    element = WebDriverWait(driver, 10000).until(
    EC.presence_of_element_located((By.ID, "M0:50::btn[8]")) #This is a dummy element
    )
    element = driver.find_element_by_id("M0:50::btn[8]")    # Ejecutar
    element.click()

    
    #   Descargar
    #   Esperar a que se procesen los datos, si se demora más de 1000 segundos, falla.
    element = WebDriverWait(driver, 10000).until(
    EC.presence_of_element_located((By.ID, "M0:46:::1:0_l")) #This is a dummy element
    )
    # Scrollbar, mapeo para extraer datos
    element = driver.find_element_by_id("RCua2FioriToolbar-moreButton")
    element.click()

    element = driver.find_element_by_id("wnd[0]/mbar/menu[0]-BtnChoiceMenu")
    element.location_once_scrolled_into_view
    element.click()

    element = driver.find_element_by_id("wnd[0]/mbar/menu[0]/menu[3]")
    element.click()


    element = driver.find_element_by_id("wnd[0]/mbar/menu[0]/menu[3]/menu[1]")
    element.click()

    driver.implicitly_wait(10)

    #   Espera a que se abra dialogo
    WebDriverWait(driver, 600).until(
    EC.presence_of_element_located((By.ID, "PromptDialogOk-cnt"))
    )
    button = driver.find_element_by_id("PromptDialogOk")
    
    #   No se por qué pero con dos click funciona
    try:
        button.click()
        button.click()
    except:
        try:
            driver.implicitly_wait(10)
            button = driver.find_element_by_id("PromptDialogOk")
            button.click()
            button.click()
        except:
            print('error')
    finally:
        driver.quit()


#   Extracción para todas las sociedades
sociedades = [2000,2100,2200,3000,3100]

for i in sociedades:
    descarga(i)
