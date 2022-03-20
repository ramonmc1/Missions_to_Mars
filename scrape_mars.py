# Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import html5lib
import time

def scrape_info():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://redplanetscience.com/'
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')
    # Retrieve all elements that contain book information
    news_title = soup.find('div', class_='content_title').text
    news_article = soup.find('div', class_='article_teaser_body').text

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    time.sleep(1)
    html = browser.html
    soup = bs(html,'html.parser')

    image_loc = soup.find('div', class_='floating_text_area')
    image = image_loc.find('a')['href']

    feat_image_url = 'https://spaceimages-mars.com/'+image


    url = 'https://galaxyfacts-mars.com'
    mars_table = pd.read_html(url)


    df2 = mars_table[0]
    df_clean = df2.rename(columns={0:" ", 1:"Mars", 2:"Earth"}).set_index(" ")
    tclass = ['table-striped', 'bg-info', 'table-md']
    mars_table_html = df_clean.to_html(header=False, classes = tclass)
    
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    time.sleep(1)
    html = browser.html
    soup = bs(html,'html.parser')

    results = soup.find_all('div', class_='item')


    # Loop through returned results
    img_dict = []
    for result in results:

        title = result.find('h3').text
        link = result.find('a')['href']
        img_url = url+link
        resp = requests.get(img_url)
        result = bs(resp.content,'html.parser')
        img_link = result.find('img', class_='wide-image')['src']
        img_dict.append({'title': title,
                    'img_url': url+img_link})

    mars_dict = {"feature_title": news_title,
                 "feature_news": news_article,
                 "feat_image": feat_image_url,
                 "mars_info": mars_table_html,
                 "images_dict":img_dict
                }
    
    browser.quit()
    return mars_dict



