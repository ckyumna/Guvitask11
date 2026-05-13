import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_launch():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.guvi.in/")
    return driver

def test_login_positive():
    driver = test_launch()

    login = driver.find_element(By.XPATH, "//button[@id='login-btn']")
    login.click()
    time.sleep(5)

    #validate url
    assert driver.current_url == "https://www.guvi.in/sign-in/?sourceUri=http%3A%2F%2Fwww.guvi.in%2F"

    username=driver.find_element(By.XPATH, "//input[@type='email']")
    password=driver.find_element(By.XPATH, "//input[@type='password']")

    #validate username and password fields
    assert username.is_displayed()
    assert username.is_enabled()
    assert password.is_displayed()
    assert password.is_enabled()

    #entering valid email and password
    username.send_keys("yumnack1@gmail.com")
    password.send_keys("yumnack123")

    submit=driver.find_element(By.XPATH, "//a[@id='login-btn']")

    #validate submit button

    assert submit.is_displayed()
    assert submit.is_enabled()
    submit.click()

    driver.quit()

def test_login_negative():
        driver = test_launch()
        login = driver.find_element(By.XPATH, "//button[@id='login-btn']").click()

        time.sleep(5)

        username = driver.find_element(By.XPATH, "//input[@type='email']")
        password = driver.find_element(By.XPATH, "//input[@type='password']")


        # entering invalid email and password
        username.send_keys("yumna@gmail.com")
        password.send_keys("yumnack1236789")

        submit = driver.find_element(By.XPATH, "//a[@id='login-btn']")

        submit.click()


        driver.quit()



