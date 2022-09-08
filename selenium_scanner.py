from selenium import webdriver
from selenium.webdriver.common.by import By
from pyfiglet import Figlet
import time

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)


# Main function to get data with site scanner, this work with selenium basic commands.
def main_func():
    try:
        f = Figlet(font='standard')
        print(f.renderText('Selenium scan'))
        driver.get('https://hackertarget.com/nmap-online-port-scanner/')
        ip = driver.find_element(By.NAME, 'theinput')
        ip.send_keys(input('Set (host or domain) to scan: ')), print('Sending command...')
        driver.find_element(By.ID, 'clickform').click(), time.sleep(5)
        scan = driver.find_element(By.ID, 'formResponse')
        print(f'\n{scan.text}')
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


main_func()


# # Headers and User-agent settings, if you need to see browser gui, set options.headless = False
# options = webdriver.ChromeOptions()
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0')
# options.add_argument('--disable-blink-features=AutomationController')
# options.headless = True
# driver = webdriver.Chrome(
#     executable_path=r'C:\Users\Levashov\PycharmProjects\pythonProject\my_modules\SeleniumChrome\chromedriver.exe',
#     options=options
# )