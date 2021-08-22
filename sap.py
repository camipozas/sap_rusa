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
user_name = env("user_name")  # => 'sloria'
password = env("password")  # => raises error if not set
driver_path = env("driver_path",'chromedriver.exe')  # => raises error if not set

driver = webdriver.Chrome(driver_path)


#   Ingresar a SAP
driver.get("https://dims4prdci.dimerc.cl:8001/sap/bc/ui5_ui5/ui2/ushell/shells/abap/FioriLaunchpad.html?sap-client=300&sap-language=ES#Customer-manageLineItems?sap-ui-tech-hint=GUI")
element = driver.find_element_by_id("USERNAME_FIELD-inner")
element.send_keys(user_name)
element = driver.find_element_by_id("PASSWORD_FIELD-inner")
element.send_keys(password)
element.send_keys(Keys.RETURN)

#   Ingresar a la transaccion
driver.implicitly_wait(20)
driver.switch_to.frame("application-Customer-manageLineItems")
driver.switch_to.frame("ITSFRAME1")

# Llenar datos
soc1 = 2100
soc2 = 2200
element = driver.find_element_by_id("M0:46:::2:34")
element.send_keys(soc1)
element = driver.find_element_by_id("M0:46:::2:59")
element.send_keys(soc2)
ayer = datetime.today() - timedelta(days=1)
d1 = ayer.strftime("%d.%m.%Y")
element = driver.find_element_by_id("M0:46:::12:34")
element.click()
element.clear()
element.send_keys(d1)
element = driver.find_element_by_id("M0:50::btn[8]")
element.click()

#   Descargar
try:
    element = WebDriverWait(driver, 600).until(
    EC.presence_of_element_located((By.ID, "M0:46:::1:0_l")) #This is a dummy element
    )
    print("hola")
    element = driver.send_keys(Keys.LEFT_SHIFT + Keys.F4)
    print("hola")
    element = driver.find_element_by_id("PromptDialogOk")
    element.click()
finally:
    driver.quit()