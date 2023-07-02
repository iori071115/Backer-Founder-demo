from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time 

s = Service('chromedriver')
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("detach", True)
chrome = webdriver.Chrome(service = s ,options= chrome_options )

def width_less_than_400():
    s = Service('chromedriver')
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("detach", True)
    chrome = webdriver.Chrome(service = s ,options= chrome_options )

    chrome.execute_script("window.open('https://wabay.tw/', '','width=400,height=600');")
    window_handles = chrome.window_handles
    chrome.switch_to.window(window_handles[0])
    chrome.close()
    chrome.switch_to.window(window_handles[-1])

    menu = chrome.find_element(By.CLASS_NAME, 'js-sidebar-menu-icon')
    menu.click()
    time.sleep(1)

    element = chrome.find_element(By.XPATH, '/html/body/div/div/div/nav/div/div[3]/div')
    text = element.text
    themes = text.split('\n')

    for theme in themes:
        link = chrome.find_element(By.LINK_TEXT, theme)
        link.click()
        time.sleep(1)

        ddm1 = chrome.find_element(By.ID,"type")
        try:
            typ = ddm1.find_element(By.CSS_SELECTOR,"option[selected='selected']").text
        except:
            typ = ddm1.find_element(By.CSS_SELECTOR,"option[value]").text
        
        ddm2 = chrome.find_element(By.ID,"category_id")
        category = ddm2.find_element(By.CSS_SELECTOR,"option[selected='selected']").text
        
        if typ == "全部主題" and theme == category:
            print(f"驗證 點擊分類 {theme} 與下拉選單 全部主題 + {category} 符合")
        else:
            print(f"驗證 點擊分類 {theme} 與下拉選單 全部主題 + {category} 不符合")    
        chrome.back()
        time.sleep(1)
    chrome.close()

def width_more_than_1920():
    s = Service('chromedriver')
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("detach", True)
    chrome = webdriver.Chrome(service = s ,options= chrome_options )
    chrome.set_window_size(1920,1080)
    
    chrome.get("https://wabay.tw/")
    time.sleep(1)

    element = chrome.find_element(By.XPATH,"/html/body/div/div/div/main/div/div/nav/ul" ).text
    themes = element.split('\n')
    themes.pop(0)

    for theme in themes:
        link = chrome.find_element(By.LINK_TEXT, theme)
        link.click()
        time.sleep(1)

        ddm1 = chrome.find_element(By.ID,"type")
        try:
            typ = ddm1.find_element(By.CSS_SELECTOR,"option[selected='selected']").text
        except:
            typ = ddm1.find_element(By.CSS_SELECTOR,"option[value]").text
        
        ddm2 = chrome.find_element(By.ID,"category_id")
        category = ddm2.find_element(By.CSS_SELECTOR,"option[selected='selected']").text
        
        if typ == "全部主題" and theme == category:
            print(f"驗證 點擊分類 {theme} 與下拉選單 全部主題 + {category} 符合")
        else:
            print(f"驗證 點擊分類 {theme} 與下拉選單 全部主題 + {category} 不符合")    
        chrome.back()
        time.sleep(1)
    chrome.close()