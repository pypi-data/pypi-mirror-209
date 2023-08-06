from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from bs4 import BeautifulSoup
from keras.utils import img_to_array
from keras.utils import load_img
from keras.models import load_model
from PIL import Image
from io import BytesIO
import requests
import numpy as np
import cv2
import time
import json
import os

###################################################
# V 1.5.3 By Yihuan Studio --> 2023/5/19/10:48:09  

#############################################
#  vfcCode AI model 4.1  x2859 picture
##  image enhancement algorithm V1 By Sam

def modle_setup(model_path):

    if model_path == "vfcAI-4.1" :

        current_path = os.path.abspath(os.path.dirname(__file__))
        parent_folder_path = os.path.join(current_path, '..')
        model_path = os.path.join(parent_folder_path, 'vfc_AiModel_4.1_VGG16_black.h5')

    model = load_model(model_path)
    print(model_path + " load Success")
    return model

def chrome_driver_setup():
    print("chrome_options setup")
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1280,960")
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://sai.tyai.tyc.edu.tw/online/'
    driver.get(url)
    print("chrome_options ready\n")
    return driver

def switch_frame(reset, frame, driver):
    if reset:
        driver.switch_to.default_content()
    for frame_name in frame:
        right_frame = driver.find_element(By.NAME, frame_name)
        driver.switch_to.frame(right_frame)

def vfcCodeFilter(img):
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    kernel_d = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 3))
    kernel_e = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    img = cv2.dilate(img, kernel_d)
    img = cv2.erode(img, kernel_e)

    img = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY)[1]
    return Image.fromarray(img)

def predict_image(image_path, captcha_image, model):
    image_bytes = BytesIO()
    captcha_image.save(image_bytes, format='PNG')
    image_bytes.seek(0)
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    predictions = model.predict(image)
    predicted_label = np.argmax(predictions, axis=1)[0]
    confidence = predictions[0][predicted_label]

    return predicted_label, confidence


def score_tolist(new_page_source):
    html = new_page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 提取考試科目成績
    subject_scores = []
    rows = soup.select('table.t02 tr.row')
    for row in rows:
        subject = row.select_one('td.top').text.strip()
        score = row.select_one('td.top.right span').text.strip()
        subject_scores.append({'考試科目': subject, '考試成績': score})

    # 提取總分、平均分數、排名和科別排名
    total_score = soup.select_one('table.scoreTable-inline td.score').text.strip()
    
    average_score_element = soup.select_one('table.scoreTable-inline span.unpass')
    average_score = average_score_element.text.strip() if average_score_element else "N/A"

    ranking_elements = soup.select('table.scoreTable-inline td.score')
    ranking = ranking_elements[2].text.strip() if len(ranking_elements) >= 3 else "N/A"
    department_ranking = ranking_elements[3].text.strip() if len(ranking_elements) >= 4 else "N/A"

    # 建立包含所有資訊的字典
    result = {
        '考試標題': soup.select_one('.center.pt-2 .bluetext').text.strip(),
        '學號': soup.select_one('.center.mobile-text-center .mr-3-ow:nth-of-type(1)').text.strip().replace('學號：', ''),
        '姓名': soup.select_one('.center.mobile-text-center .mr-3-ow:nth-of-type(2)').text.strip().replace('姓名：', ''),
        '班級': soup.select_one('.center.mobile-text-center .mr-3-ow:nth-of-type(3)').text.strip().replace('班級：', ''),
        '考試科目成績': subject_scores,
        '總分': total_score,
        '平均分數': average_score,
        '排名': ranking,
        '科別排名': department_ranking
    }

    return result


def getGrades(username, password, driver, model):
     
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"

    loginScess = False

    while True:
        vfc = ""
        captcha_element = driver.find_element(By.XPATH, '//img[@id="imgvcode"]')

        src = captcha_element.get_attribute('src')
        print('Image source:', src)

        screenshot_path = 'captcha.png'
        driver.save_screenshot(screenshot_path)
        location = captcha_element.location
        size = captcha_element.size
        captcha_image = Image.open(screenshot_path)
        captcha_image = captcha_image.crop((location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']))
        width, height = captcha_image.size

        part_width = width // 4
        captcha_images = []
        for i in range(4):
            left = i * part_width
            right = (i + 1) * part_width
            part = captcha_image.crop((left, 0, right, height))
            part = vfcCodeFilter(part)
            part_path = f'captcha_part{i}.png'
            part.save(part_path)
            captcha_images.append(part_path)

        confidence_threshold_low = 50
        confidence_threshold_medium = 80
        
        confidence = [0, 0, 0, 0]
        count = 0

        for captcha_image_path in captcha_images:
            predicted_label, predicted_confidence = predict_image(captcha_image_path, captcha_image, model)
            vfc += str(predicted_label)
            predicted_confidence = predicted_confidence * 100
            confidence[count] = predicted_confidence
            count += 1

            if predicted_confidence < confidence_threshold_low:
                print(f"{RED}驗證碼: {predicted_label} 置信度: {predicted_confidence} %{RESET}")
            elif predicted_confidence < confidence_threshold_medium:
                print(f"{YELLOW}驗證碼: {predicted_label} 置信度: {predicted_confidence} %{RESET}")
            else:
                print(f"{GREEN}驗證碼: {predicted_label} 置信度: {predicted_confidence} %{RESET}")

        allConfidence = confidence[0] * confidence[1] * confidence[2] * confidence[3] * 0.000001
        print("驗證碼影像辨識:" + str(vfc) + "  本次準確率:" + str(allConfidence) + " %")

        vcode = vfc
        # login
        username_element = driver.find_element(By.ID, 'Loginid')
        username_element.send_keys(username)
        password_element = driver.find_element(By.ID, 'LoginPwd')
        password_element.send_keys(password)
        vcode_element = driver.find_element(By.ID, 'vcode')
        vcode_element.send_keys(vcode)
        login_button = driver.find_element(By.ID, 'btnLogin')
        login_button.click()

        try:
            alert = Alert(driver)
            popup_text = alert.text
            print(popup_text)
            alert.dismiss()
            if popup_text == "帳號或密碼錯誤,請重新登入!":
                username = input("請輸入帳號 >> ")
                password = input("請輸入密碼 >> ")
            # input()

        except:
            print(f"{GREEN}密碼正確.{RESET}")
            break


    print(f"{GREEN}驗證碼正確.{RESET}")
    # 進入成績查詢頁面
    # 切換到左測選單
    switch_frame(False, ["left"], driver)
    student_data_link = driver.find_element(By.ID, 'lnkStudentData')  # 按鈕名稱 "學生 xxx 的資料"
    student_data_link.click()
    # 尋找按鈕名稱 "查詢學生資料"
    button_name = '查詢學生資料'
    button_elements = driver.find_elements(By.CSS_SELECTOR, 'td.SubMenuItem') 
    for button in button_elements:
        button_text = button.text
        if button_text == button_name:
            button.click()
            break

    # 切換到框架"right"的框架"right_below"
    switch_frame(True, ["right", "right_below"], driver)
    # 找到查詢資料按鈕
    button = driver.find_element(By.CSS_SELECTOR, "button[onclick*='window.open']")
    button.click()
    # 切換到框架"right"的框架"right_below"
    switch_frame(True, ["right", "right_top"], driver)
    # 找到各式成績查詢按鈕
    button = driver.find_element(By.XPATH, "//img[@title='各式成績查詢']")
    button.click()
    exam = '[111下] 111下第1次段考'
    # 選擇彈出選擇考試的選單
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[-1])  # 切换到最新打开的窗口
    # 等待下拉框載入完成
    ddl_exam_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ddlExamList')))
    # 創建 Select 對象
    select = Select(ddl_exam_list)
    # 選擇下拉選單中的選項
    select.select_by_visible_text(exam)
    # 切换回原始窗口
    driver.switch_to.window(window_handles[0])

    # 成績讀取
    # 切换到右侧框架
    switch_frame(True, ["right", "right_below"], driver)
    # 獲取新窗口的頁面內容(成績表格)
    new_page_source = driver.page_source
    # print(new_page_source)
    # driver.quit()
    # 成績表格分析
    result = score_tolist(new_page_source)
    loginScess = True

    driver.delete_all_cookies()
    driver.refresh()
    return result


# model = modle_setup("vfcAI-4.1")

# driver = chrome_driver_setup()

# print(getGrades("013333","B123742969",driver,model))























