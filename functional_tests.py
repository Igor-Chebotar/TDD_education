from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), )
browser.set_window_size(960, 540)
browser.get('http://localhost:8000')
assert "Congratulations!" in browser.title
