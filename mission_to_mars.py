from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

def init_browser():
        executable_path = {"executable_path": "/c/Users/ericc/bin/chromedriver"}
        return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    content = {}

    level = soup.find("div",class_="list_text")

    content["title"]  = level.find("div",class_="content_title").get_text()
    content["article"] = level.find("div",class_="article_teser_body").get_text()

    print(content)

#carousel_items

def scrape_info():
    browser = init_browser()

    url = "https://www.jpl.nasa.gov/spaceimages/"
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    content["picture"] = level.find("div", class_="carousel_items").get_text()
