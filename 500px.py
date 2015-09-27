from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import urllib.request

def download_img(url, filename):
    urllib.request.urlretrieve(url, 'images/' + str(filename) + '.jpg')
    print(url)

def goto_next_page(driver):
    next = driver.find_element_by_css_selector('a.photo_arrow.next')
    next.click()
    # use directly arrow keys?
    # ActionChains(driver).send_keys(Keys.ARROW_RIGHT)

def scrape_photos(starturl, limit):
    count = 1
    driver.get(starturl)
    while limit > 0:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        imgurl = soup.find('div', { 'class' : 'photo_wrap' }).find('img')['src']
        download_img(imgurl, count)
        goto_next_page(driver)

        limit = limit - 1
        count = count + 1
    

driver = webdriver.Firefox()
# TODO: automatically retrieve first popular photo page url
firsturl = 'https://500px.com/photo/122966791/land-of-the-living-wind-by-timothy-poulton?from=popular'
limit = 5
scrape_photos(firsturl, limit)

