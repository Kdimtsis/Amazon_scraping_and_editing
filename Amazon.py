from bs4 import BeautifulSoup as bs
import requests
import re
import time
from csv import writer
import glob
import pandas as pd
import os

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class amazon():

    # GET THE WORKING DIRECTORY PATH
    path = os.getcwd()

    def __init__(self):
        self.name = "Amazon"
        self.url = "https://www.amazon.com/s?k="


    def item_link(self):

        search_item = input("What do you want to search for? ")
        link = self.url + str(search_item)
        return link

    def all_pages(self):

        """RETURNS A LIST WITH THE LINKS OF ALL PAGES"""
        url = self.item_link()

        driver = webdriver.Chrome()
        driver.get(url)
        wait = WebDriverWait(driver, 10)

        link_lst = []
        while True:
            try:
                element_present = EC.presence_of_element_located((By.XPATH, """//li[@class="a-last"]"""))
                wait.until(element_present)
            except TimeoutException:
                print("Loading took too much time!")
                url_link = driver.current_url
                link_lst.append(url_link)
                break
            else:
                element_present = driver.find_element_by_xpath("""//li[@class="a-last"]""")
                url_link = driver.current_url
                link_lst.append(url_link)
                element_present.click()

        driver.close()
        return link_lst

    def page_details(self):

        """RETURNS A LIST OF TUPLES WITH DETAILS FOR EVERY PRODUCT IN EVERY PAGE"""

        link_list = self.all_pages()
        driver = webdriver.Chrome()
        items_list = []

        # FOR EVERY PAGE LINK
        for link in link_list:

            # START DRIVER
            driver.get(link)

            # GET FULL PAGE SOURCE
            page_source = driver.page_source
            soup = bs(page_source, "html.parser")

            # FINDS EVERY PRODUCT
            items = soup.find_all(class_="s-result-item")

            for item in items:

                # IM INTERESTED ONLY IN PRODUCTS THAT HAVE A PRICE, WHICH MEANS THEY ARE AVAILABLE
                price = item.find("span", "a-offscreen")
                if price:
                    try:
                        title = item.find("span", "a-size-medium").text.strip()
                    except:
                        title = "No title available"
                    price = item.find("span", "a-offscreen").text.replace("$", "").strip()
                    try:
                        rating = item.find("span", "a-icon-alt").text.replace(" out of 5 stars", "/5")
                    except:
                        rating = "No rating"
                    try:
                        review_count = item.find("span", "a-size-base").text
                    except:
                        review_count = "No reviews"


                    items_list.append((title,price,rating,review_count))
        driver.close()
        return items_list

    def write_to_csv(self):

        # LIST OF TUPLES WITH THE DATA WE EXTRACTED
        lst = self.page_details()

        # WRITE TO CSV
        with open("Amazon_data.csv", "w", newline="", encoding="utf-8") as file:
            csv_writer = writer(file)

            # WRITE THE HEADERS FIRST
            csv_writer.writerow(["Name", "Price", "Rating", "Review Counts"])

            # EVERY ROW ITS A TUPLE WITH TITLE,PRICE,RATING,REVIEW COUNTS SO IT WILL MATCH THE HEADERS
            for row in lst:
                csv_writer.writerow(row)

        return "Csv file is ready"

    def latest_csv(self):

        """FUNCTION THAT RETURNS THE LATEST CSV FILE CREATED IN CURRENT PATH"""

        self.write_to_csv()

        # CURRENT FILEPATH
        file_path = self.path

        # ONLY CSV FILES
        types = "*.csv"

        # JOIN THE CURRENT FILEPATH WITH *.CSV WHICH WILL GET ALL CSV
        all_csv = os.path.join(file_path, types)

        # WITH GLOB.GLOB IT RETURNS ALL CSV
        csv_files = glob.glob(all_csv)

        # OS.PATH.GETCTIME RETURNS THE LATEST
        latest_csv = max(csv_files, key=os.path.getctime)

        return latest_csv

    def clean_csv(self):

        """FUNCTION THAT CLEANS THE CSV FILE"""

        # OPEN THE CSV I CREATED WITH PANDAS
        table = pd.read_csv(self.latest_csv())

        table = table[table["Name"] != "No title available"]

        # EXTRACT ONLY DIGITS FROM PRICE COLUMN
        table["Price"] = table["Price"].str.replace(",", "").str.extract(r"(\d+.\d+)")


        table["Rating"] = table["Rating"].str.replace("/5", "")

        # EXTRACT ONLY DIGITS FROM REVIEWS COLUMN
        table["Review Counts"] = table["Review Counts"].str.replace(",", "").str.extract(r"(\d+)")

        # DROP NULL VALUES
        table.dropna(inplace=True)

        # TURN COLUMNS INTO NUMERIC TYPES
        table["Price"] = table["Price"].astype("float")
        table["Rating"] = table["Rating"].astype("float")
        table["Review Counts"] = table["Review Counts"].astype("int")

        # RENAME COLUMNS
        table.rename(columns={"Rating": "Rating (/5)"}, inplace=True)

        # SORT COLUMNS FIRST BY HIGHEST RATING THEN WITH MOST REVIEWS AND LOWEST PRICE
        table.sort_values(["Rating (/5)", "Review Counts", "Price"], ascending=[False, False, True], inplace=True)

        # SAVE DATAFRAME TO A NEW CSV FILE
        path = self.path
        name = "Edited_amazon_data.csv"
        new_name = os.path.join(path, name)
        table.to_csv(new_name, index=False)


if __name__ = "__main__:
    amazon().clean_csv()
