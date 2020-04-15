import config
import time
#from prettytable import PrettyTable
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#x = PrettyTable(["S.No", "TestCase", "Status"])
#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver= webdriver.Firefox()
#driver= webdriver.Chrome(r"C:\Users\deepa\Desktop\Automation_Framework\chromedriver.exe")
def OpenURL(driver): 
    driver.get(config.URL)
    element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.ID,"remember")))
    #x.add_row(["1","Site Launch Succesfully","PASS"])

def LoginToPage(driver):
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
        #x.add_row(["2","Login to Site Succesfully","PASS"])
    except Exception as e:
        print("[LoginToPage]Exception is :"+str(e))
        #x.add_row(["2","Login to Site"+str(e),"FAIL"])

def CloseBrowser(driver):
    ele = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID,"logo")))
    driver.quit()

def ChangeLanguage(driver):
    try:
        element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,config.dropdown)))
        driver.find_element_by_xpath(config.dropdown).click()
        driver.find_element_by_link_text("Japanese").click()
        alt = driver.switch_to.alert #Create the Alert object
        alt.accept()
        jp = driver.find_element_by_xpath(config.JHelp).text
        #jp = driver.find_element_by_link_text("ヘルプ")
        print(jp)#.get_attribute("text"))
    except Exception as e:
        print("[ChangeLanguage]Exception is :"+str(e))
    time.sleep(3)
    try:
        element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,config.dropdown)))
        driver.find_element_by_xpath(config.dropdown).click()
        driver.find_element_by_link_text("English").click()
        alt = driver.switch_to.alert #Create the Alert object
        alt.accept()
        en = driver.find_element_by_xpath(config.EHelp).text
        print(en)#.get_attribute("text"))
        #x.add_row(["3","Language changes Succesfully","PASS"])
    except Exception as e:
        print("[ChangeLanguage]Exception is :"+str(e))
        #x.add_row(["3","Language changes Succesfully"+str(e),"FAIL"])
    

def tab_clickable(driver):
    try:
        element = WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,config.Dashboard)))
        print(element)
        time.sleep(15)
        at=driver.find_element_by_xpath(config.Alert)
        print(at.is_enabled())
        dt=driver.find_element_by_xpath(config.Dashboard)
        print(dt.is_enabled())
        vt=driver.find_element_by_xpath(config.Variables)
        print(vt.is_enabled())
        nt=driver.find_element_by_xpath(config.Notificaton)
        print(nt.is_enabled())
        tt=driver.find_element_by_xpath(config.Tests)
        print(tt.is_enabled())
        #x.add_row(["4","All Tabs are enabled and clickable ","PASS"])
        #print(at.get_attribute('text')+""+at.is_enabled(),dt.get_attribute('text')+""+dt.is_enabled(),vt.get_attribute('text')+""+vt.is_enabled(),tt.get_attribute('text')+""+tt.is_enabled(),nt.get_attribute('text')+""+nt.is_enabled())
    except Exception as e:
        print("[tab_clickable]Exception is :"+str(e))
       # x.add_row(["4","[tab_clickable]Exception is :"+str(e),"FAIL"])
    
def GotoClient(driver):
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
      #  x.add_row(["5","Verify the client details Succesfully","PASS"])
    except Exception as e:
        print("[GotoClient]Exception is :"+str(e))
     #   x.add_row(["5","[GotoClient]Exception is :"+str(e),"FAIL"])
    #print(x)

#OpenURL()
#LoginToPage()
#ChangeLanguage()
#tab_clickable()
#GotoClient()
#CloseBrowser()