from selenium import webdriver
import time
import json

try:
    url = "https://lc.multicampus.com/safetyedu-samsung/#/login"  # 접속하고자하는 url
    setting = json.load(open('setting.json', 'r'))  # id, pw
    driverPath = "chromedriver.exe"  # Chrome Driver path
    driver = webdriver.Chrome(driverPath)  # Open Chrome
    driver.get(url)
    time.sleep(7)

    # 로그인
    driver.find_element_by_xpath("//input[@placeholder='Knox ID를 입력하세요.']").send_keys(setting['id'])
    driver.find_element_by_xpath("//input[@placeholder='비밀번호를 입력해주세요.']").send_keys(setting['pw'])
    driver.find_element_by_xpath("//button[.='LOGIN']").click()
    time.sleep(5)

    # 학습 하기
    driver.find_element_by_xpath("//button[.='학습하기']").click()
    time.sleep(3)

    # 이어 학습
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element_by_xpath("//a[@id='btnNextLrn']").click()
    time.sleep(3)
    while True:
        driver.switch_to.window(driver.window_handles[2])
        # 다음 동영상 클릭 시도
        try:
            driver.find_element_by_xpath("//span[@class='btn--control__txt' and .='다음']").click()
        except Exception as e:
            print(e)
        time.sleep(0.5)
        # 스킵 실패인 경우 확인
        try:
            driver.find_element_by_xpath("//button[@class='o-button o-button--alert o-button--primary']").click()
        except Exception as e:
            print(e)
        time.sleep(3)

except Exception as e:
    print(e)
