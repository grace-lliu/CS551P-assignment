from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def before_all(context):
    # Use headless Chrome for faster testing
    options = Options()
    options.headless = True
    context.browser = webdriver.Chrome(options=options)

def after_all(context):
    context.browser.quit()
