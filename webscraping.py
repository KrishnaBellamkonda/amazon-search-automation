import selenium
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

import re
import pprint

from utils import chromePath, argsort, reviewsRegex, n_cheapest_products, n_sizebase_products, int_argsort, delay
from xpaths import *

import json 
from time import sleep
from pathlib import Path

# Opening Web Browser 
def scrape_and_print(keywords, json_path, run_pages=False):

    print()
    # Website URL 
    baseURL = "https://www.amazon.in/"
    keywordsString = "+".join(keywords)
    amazonSearchQuery = "https://www.amazon.in/s?k={}&ref=nb_sb_noss_2".format(keywordsString)

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])    

    with webdriver.Chrome(chromePath, options=options) as driver:
        # print(amazonSearchQuery)
        driver.get(amazonSearchQuery)

        products = driver.find_elements_by_xpath(productElementXPath)


        # Data Extraction 
        titles = []
        prices = []
        links = []

        titles.extend(driver.find_elements_by_xpath(titleXPath))
        prices.extend(driver.find_elements_by_xpath(priceXPath))
        links.extend(driver.find_elements_by_xpath(linksXPath))
        
        load_time = 8

        if run_pages:
            for i in range(run_pages):              
                try:
                    #myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, nextButtonXPath)))
                    wait = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, nextButtonXPath)))
                    nextButtonLink = driver.find_element_by_xpath(nextButtonXPath).get_attribute('href')
                    driver.get(nextButtonLink)
                    print(baseURL+nextButtonLink)
                    print ("Page is ready!")
                except TimeoutException:
                    print("Page couldn't be loaded")
                    break
                except StaleElementReferenceException:
                    print("Stale Website")
                    break
                else:
                    titles.extend(driver.find_elements_by_xpath(titleXPath))
                    prices.extend(driver.find_elements_by_xpath(priceXPath))
                    links.extend(driver.find_elements_by_xpath(linksXPath))
        else:
            pass



        print(titles)
        #reviews = driver.find_elements_by_xpath(reviewsXPath)
        #sizeBases = driver.find_elements_by_xpath(sizeBaseXPath)
        
        print("-"*10, "Scrape Data", "-"*10)
        print("Titles:", len(titles))
        print("Prices:", len(prices))
        print("Links:", len(links))
        print("-"*40)
        print()


        # Products 
        products = []

        id=0
        for (title, price, link) in zip(titles, prices, links):
            # Data Section 
            data = {}
            try:
                data["title"] = title.text
                data["price"] = float(price.text.replace(",", ""))
                data["link"] = link.get_attribute('href')
                data["id"] = id
                id+=1
                products.append(data)

            except StaleElementReferenceException:
                pass
            #data["sizebase"] = int(sizebase.text.replace(",", ""))
        

        # Sort datapoints on basis of price 
        prices_array = [obj["price"] for obj in products]
        #sizebases_array = [obj["sizebase"] for obj in products]

        price_sorted_indices = argsort(prices_array)
        #sizebases_sorted_indices = int_argsort(sizebases_array)


        price_sorted_products = [products[index] for index in price_sorted_indices]
        #sizebases_sorted_products = [products[index] for index in sizebases_sorted_indices]
        #sizebases_sorted_products.reverse()
        
        

        # Print the three cheapest products 
        print("-"*10, "CHEAPEST PRODUCTS", "-"*10)
        
        for index, product in enumerate(price_sorted_products[:n_cheapest_products]): 
            link = product["link"]

            # Open new tab
            driver.execute_script("window.open('');")
            sleep(1)
            driver.switch_to.window(driver.window_handles[index+1])
            sleep(1)
            driver.get(link)
            
            print(pprint.pformat(product))
            print()

        print("\n \n \n")

        with open(json_path, "w") as fp:
            json.dump(products, fp)
        
        sleep(40)