from selenium import  webdriver
driver=webdriver.Chrome(r"C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.com/")
driver.get_screenshot_as_file("screen.jpg")
driver.close()
