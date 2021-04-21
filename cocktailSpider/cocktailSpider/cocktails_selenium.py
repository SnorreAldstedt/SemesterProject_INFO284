from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)

# Function that returns a list of cocktail-links from the website makemycocktail.com
# Customized specifically for https://www.makemycocktail.com/sitemap.xml, very easy to get the links from this address.
# The function could easily be customized for other purposes.
def get_cocktails(url):
    driver.get(url)
    time.sleep(2)
    links = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//*[text()[contains(.,'https://www.makemycocktail.com/cocktails/')]]")
        ))
    cocktails_selenium = []
    for l in links:
        cocktails_selenium.append(l.get_attribute("innerHTML"))
    driver.quit()
    unique_cocktails = set(cocktails_selenium)
    return unique_cocktails

#cocktails_list = set(get_cocktails('https://www.makemycocktail.com/sitemap.xml'))
