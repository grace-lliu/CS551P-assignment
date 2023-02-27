import os
import threading
import time
from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from staff import app

# Use the chrome driver specific to your version of Chrome browser and put it in ./driver directory
CHROME_DRIVER = os.path.join(os.path.join(os.path.dirname(__file__), 'driver'), 'chromedriver')

chrome_options = Options()
# comment out the line below if you want to see the browser launch for tests
# possibly add time.sleep() if required
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")


def before_all(context):
    context.server = simple_server.make_server('', 5000, app)
    context.pa_app = threading.Thread(target=context.server.serve_forever)
    context.pa_app.start()

    context.browser = webdriver.Chrome(options=chrome_options, executable_path=CHROME_DRIVER)
    context.browser.set_page_load_timeout(time_to_wait=200)


def after_all(context):
    context.browser.quit()
    context.pa_app.join()
    context.server.shutdown()
