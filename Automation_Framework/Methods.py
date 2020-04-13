import config
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver= webdriver.Firefox()
#driver= webdriver.Chrome(r"C:\Users\deepa\Desktop\Automation_Framework\chromedriver.exe")
def OpenURL(): 
    driver.get(config.URL)
    element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.ID,"remember")))

def LoginToPage():
    try:
        driver.implicitly_wait(10)
        u_id=driver.find_element_by_xpath(config.userid)
        p_id=driver.find_element_by_xpath(config.pasid)
        btn_id=driver.find_element_by_xpath(config.btnid)
        rem_id=driver.find_element_by_xpath(config.rememid)
        driver.implicitly_wait(5)
        u_id.send_keys(config.Loginid)
        p_id.send_keys(config.Password)
        rem_id.click()
        btn_id.click()
    except Exception as e:
        print("Exception is :"+str(e))

def CloseBrowser():
    ele = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID,"logo")))
    driver.quit()

def ChangeLanguage():
    try:
        element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,config.dropdown)))
        driver.find_element_by_xpath(config.dropdown).click()
        driver.find_element_by_link_text("Japanese").click()
        alt = driver.switch_to.alert #Create the Alert object
        alt.accept()
        jp = driver.find_element_by_link_text("ヘルプ").text
        print(jp)
    except Exception as e:
        print("Exception is :"+str(e))
    time.sleep(3)
    try:
        element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,config.dropdown)))
        driver.find_element_by_xpath(config.dropdown).click()
        driver.find_element_by_link_text("English").click()
        alt = driver.switch_to.alert #Create the Alert object
        alt.accept()
        en = driver.find_element_by_link_text("Help").text
        print(en)
        if en not in jp :
        print("Both are diffent language")
    except Exception as e:
        print("Exception is :"+str(e))
    

def tab_clickable():
    try:
        element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,config.Dashboard)))
        print(element)
        time.sleep(15)
        at=driver.find_element_by_xpath(config.Alert)
        dt=driver.find_element_by_xpath(config.Dashboard)
        vt=driver.find_element_by_xpath(config.Variables)
        nt=driver.find_element_by_xpath(config.Notificaton)
        tt=driver.find_element_by_xpath(config.Tests)
        print(at.get_attribute('text'),dt.get_attribute('text'),vt.get_attribute('text'),tt.get_attribute('text'),nt.get_attribute('text'))
    except Exception as e:
        print("Exception is :"+str(e))
    
def GotoClient():
    try:
        element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,config.dropdown)))
        driver.find_element_by_xpath(config.dropdown).click()
        driver.find_element_by_xpath(config.client).click()
        WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,config.c_details)))
        #details=driver.find_element_by_xpath(config.c_details)
        name=driver.find_element_by_xpath(config.c_name).text
        desc=driver.find_element_by_xpath(config.c_des).text
        date1=driver.find_element_by_xpath(config.s_date).text
        date2=driver.find_element_by_xpath(config.e_date).text
        MLT=driver.find_element_by_xpath(config.MLT).text
        MVT=driver.find_element_by_xpath(config.MVT).text
        sce=driver.find_element_by_xpath(config.scenerios).text
        MTS=driver.find_element_by_xpath(config.MTS).text
        print(name,desc,date1,date2,MLT,MVT,sce,MTS)
    except Exception as e:
        print("Exception is :"+str(e))


OpenURL()
LoginToPage()
#ChangeLanguage()
#tab_clickable()
#GotoClient()
#CloseBrowser()