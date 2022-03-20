{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup as bs\n",
    "import requests\n",
    "import pymongo\n",
    "from splinter import Browser\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import html5lib\n",
    "import time\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 99.0.4844\n",
      "Get LATEST chromedriver version for 99.0.4844 google-chrome\n",
      "Driver [/Users/ramon/.wdm/drivers/chromedriver/mac64/99.0.4844.51/chromedriver] found in cache\n"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://redplanetscience.com/'\n",
    "browser.visit(url)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hear Audio From NASA's Perseverance As It Travels Through Deep Space\n",
      "The first to be rigged with microphones, the agency's latest Mars rover picked up the subtle sounds of its own inner workings during interplanetary flight.\n"
     ]
    }
   ],
   "source": [
    "html = browser.html\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup = bs(html, 'html.parser')\n",
    "# Retrieve all elements that contain book information\n",
    "#articles = soup.find_all('section', class_='image_and_description_container')\n",
    "news_title = soup.find('div', class_='content_title').text\n",
    "news_article = soup.find('div', class_='article_teaser_body').text\n",
    "\n",
    "print(news_title)\n",
    "print(news_article)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://spaceimages-mars.com/image/featured/mars1.jpg\n"
     ]
    }
   ],
   "source": [
    "url = 'https://spaceimages-mars.com/'\n",
    "browser.visit(url)\n",
    "\n",
    "html = browser.html\n",
    "soup = bs(html,'html.parser')\n",
    "\n",
    "image_loc = soup.find('div', class_='floating_text_area')\n",
    "image = image_loc.find('a')['href']\n",
    "\n",
    "feat_image_url = 'https://spaceimages-mars.com/'+image\n",
    "\n",
    "print(feat_image_url)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                         0                1                2\n",
       " 0  Mars - Earth Comparison             Mars            Earth\n",
       " 1                Diameter:         6,779 km        12,742 km\n",
       " 2                    Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       " 3                   Moons:                2                1\n",
       " 4       Distance from Sun:   227,943,824 km   149,598,262 km\n",
       " 5          Length of Year:   687 Earth days      365.24 days\n",
       " 6             Temperature:     -87 to -5 °C      -88 to 58°C,\n",
       "                       0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:          2 ( Phobos & Deimos )\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url = 'https://galaxyfacts-mars.com'\n",
    "tables = pd.read_html(url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method DataFrame.to_html of                                                    \n",
       "                                                   \n",
       "Equatorial Diameter:                       6,792 km\n",
       "Polar Diameter:                            6,752 km\n",
       "Mass:                 6.39 × 10^23 kg (0.11 Earths)\n",
       "Moons:                        2 ( Phobos & Deimos )\n",
       "Orbit Distance:            227,943,824 km (1.38 AU)\n",
       "Orbit Period:                  687 days (1.9 years)\n",
       "Surface Temperature:                   -87 to -5 °C>"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df2 = tables[1]\n",
    "df_new = df2.reset_index(drop=True).loc[:6]\n",
    "df_clean = df_new.rename(columns={0:\" \"})\n",
    "df_new2 = df_clean.set_index(' ').rename(columns={1:\" \"})\n",
    "table_html = df_new2.to_html\n",
    "table_html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://marshemispheres.com/'\n",
    "browser.visit(url)\n",
    "\n",
    "html = browser.html\n",
    "soup = bs(html,'html.parser')\n",
    "\n",
    "results = soup.find_all('div', class_='item')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Loop through returned results\n",
    "img_dict = []\n",
    "for result in results:\n",
    "\n",
    "    title = result.find('h3').text\n",
    "    link = result.find('a')['href']\n",
    "    img_url = url+link\n",
    "    resp = requests.get(img_url)\n",
    "    result = bs(resp.content,'html.parser')\n",
    "    img_link = result.find('img', class_='wide-image')['src']\n",
    "    img_dict.append({'title': title,\n",
    "                'img_url': url+img_link})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': 'https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': 'https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': 'https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': 'https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'}]"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "img_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.quit()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initialize PyMongo to work with MongoDBs\n",
    "conn = 'mongodb://localhost:27017'\n",
    "client = pymongo.MongoClient(conn)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define database and collection\n",
    "db = client.m_to_m\n",
    "collection = db.articles\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# URL of page to be scraped\n",
    "url = 'https://redplanetscience.com/'\n",
    "\n",
    "# Retrieve page with the requests module\n",
    "response = requests.get(url)\n",
    "# Create BeautifulSoup object; parse with 'html.parser'\n",
    "soup = BeautifulSoup(response.text, 'html.parser')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(soup.prettify())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Retrieve the parent divs for all articles\n",
    "results = soup.find_all('div' , id='news')\n",
    "results\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Display the MongoDB records created above\n",
    "articles = db.articles.find()\n",
    "for article in articles:\n",
    "    print(article)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# loop over results to get article data\n",
    "for result in results:\n",
    "    # scrape the article header \n",
    "    news_title = result.find('div', class_='article-item__headline')\n",
    "    \n",
    "    # scrape the article subheader\n",
    "    news_article = result.find('div', class_='article_teaser_body')\n",
    "\n",
    "    # print article data\n",
    "    print('-----------------')\n",
    "    print(news_title)\n",
    "    print(news_article)\n",
    "\n",
    "\n",
    "    # Dictionary to be inserted into MongoDB\n",
    "#    post = {\n",
    " #       'header': header,\n",
    " #       'subheader': subheader,\n",
    " #       'date': date,\n",
    "#    }\n",
    "\n",
    "    # Insert dictionary into MongoDB as a document\n",
    "#    collection.insert_one(post)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.7.11 64-bit ('PythonData': conda)",
   "language": "python",
   "name": "python3711jvsc74a57bd06efafaceeed34646fc4061b0225acd948a8d502b8ea2a460a635beb303574f84"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
