# 思路  生成浏览器 登录网址 pyautoxx.hotkey('ctrl','s') typeWrite(index) pyautoxx.hotkey(‘enter’)
#      找到下一章漫画 继续爬取
import pyautogui
from selenium import webdriver
import time

index = 71
pageSize = int(input("爬取多少章："))

#打开浏览器
webdriver = webdriver.Chrome("d://Google/chromedriver.exe")
webdriver.implicitly_wait(5)

#登录网页
webdriver.get("http://www.alimanhua.com/manhua/74/39721.html")


webdriver.execute_script("window.scrollBy(0, 800)")
for i in range(pageSize):
    #操作
    time.sleep(1)
    pyautogui.hotkey('ctrl','s')
    time.sleep(1)
    fileName = "DL{index:03d}".format(index=index)
    pyautogui.typewrite(fileName)
    time.sleep(1)
    pyautogui.hotkey('enter')

    #找到元素下一章
    webdriver.find_element_by_class_name("next").click()
    index += 1
    time.sleep(1)
    webdriver.execute_script("window.scrollBy(0, 800)")
    time.sleep(8.5)
    print(fileName+"已完成！")



# 1.元素会遮挡
# 2.未下载完，按下ctrl  + s 之前的下载会取消