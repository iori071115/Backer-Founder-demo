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

email = ""
pw =  ""
sponsorship_amount = 1

def login():
    chrome.get("https://wabay.tw/")
    time.sleep(1)
    login = chrome.find_element(By.LINK_TEXT, "登入")
    login.click()
    time.sleep(1)
    account = chrome.find_element(By.ID,"user_email")
    password = chrome.find_element(By.ID,"user_password")
    account.send_keys(email)
    password.send_keys(pw)
    submit = chrome.find_element(By.NAME,"commit")
    submit.click()
    time.sleep(1)

    result = login = chrome.find_element(By.ID, "flash_notice").text
    if result == "成功登入了。":
        print("驗證 登入成功")
    else:
        print("驗證 登入失敗")

def go_to_project():
    chrome.get("https://wabay.tw/projects/rising-star")
    time.sleep(1)

    sponsor = chrome.find_element(By.LINK_TEXT, "贊助專案")
    sponsor.click()
    time.sleep(1)

    result = chrome.find_element(By.XPATH, "/html/body/div/div/div/main/div[1]/div/div[2]/h1").text
    if result == "《瑞星 Rising Star》韻律體操長期發展計畫":
        print("驗證 前往贊助《瑞星 Rising Star》韻律體操長期發展計畫 成功")
    else:
        print("驗證 前往贊助《瑞星 Rising Star》韻律體操長期發展計畫 失敗")

def go_to_sponsor():
    gotopage = chrome.find_element(By.CSS_SELECTOR,"a[data-pixel-event-content-name='【單筆支持】理念支持']")
    gotopage.click()
    time.sleep(1)
    
    result = chrome.find_element(By.XPATH, '//*[@id="new_transaction"]/div/div/div[1]/div/section/div[1]/div/div[2]/div[1]/h1').text
    if result == "【單筆支持】理念支持":
        print("驗證 贊助「單筆支持｜理念支持」 成功")
    else:
        print("驗證 贊助「單筆支持｜理念支持」 失敗")

def confirm_items():
    extrasupport = chrome.find_element(By.ID,"additional-support")
    extrasupport.clear()
    extrasupport.send_keys(sponsorship_amount)
    time.sleep(3)
    submit = chrome.find_element(By.NAME,"commit")
    submit.click()
    time.sleep(1)

    result = chrome.find_element(By.XPATH, '//*[@id="new_transaction"]/div/div/div[1]/section/div/div[1]/h3').text
    if result == "會員資料":
        print("驗證 確認品項 成功")
    else:
        print("驗證 確認品項 失敗")

def fill_in_the_order_info():
    pay = chrome.find_element(By.CSS_SELECTOR,"label[spec='payment-atm']")
    pay.click()
    submit = chrome.find_element(By.NAME,"commit")
    submit.click()
    time.sleep(2)

    result = chrome.find_element(By.CSS_SELECTOR, 'label[for="paytype_vacc"]').text
    if result == "ATM轉帳" :
        print("驗證 填寫訂單資料 成功")
    else:
        print("驗證 填寫訂單資料 失敗")

def confirm_the_amount_complete_the_transaction():
    result = chrome.find_element(By.XPATH, '//*[@id="order_table"]/tbody/tr[5]/td[2]').text
    if result == "NT$ " + str(sponsorship_amount) :
        bank = chrome.find_element(By.ID,"atm_BOT")
        bank.click()
        checkbox = chrome.find_element(By.NAME,"confirm_order")
        checkbox.click()
        submit = chrome.find_element(By.ID,"confirm_send_order")
        submit.click()
        time.sleep(5)
        result2 = chrome.find_element(By.XPATH, '/html/body/div/div/div/main/section/div[1]/div/aside').text     
        if result2 == "已成功完成交易":
            print("驗證 確認金額及完成交易 成功")
        else:
            print("驗證  確認金額成功 完成交易 失敗")
    else:
        print("贊助金額不正確")


def verify_v_account_number():
    v_bank = chrome.find_element(By.XPATH,"/html/body/div/div/div/main/section/div[2]/div/div[1]/div[1]").text
    v_bank = v_bank.split('\n')
    if "銀行代碼" in v_bank[0] and len(v_bank[1]) == 16:
        print("驗證 虛擬帳戶 成功\n",v_bank )
    else:
        print("驗證 虛擬帳戶 失敗")
    chrome.close()