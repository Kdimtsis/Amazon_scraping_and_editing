# Amazon_scraping_and_editing_data
This class scrapes data from an Amazon prooduct, saves them to a csv and then cleans the csv using Pandas library. Some of the libraries that were used are: *Selenium, Beautiful soup, requests, csv, pandas, os, glob*.

## Class Analysis 

Τhe user inputs a search item and using Selenium the amazon page opens in a Google Chrome window.  

### Gathering the page urls

Next step is to get the urls of all the pages for the item that was inserted. To do this i used Selenium. By locating the "Next" button ***(driver.find_element_by_xpath)*** i clicked it to navigate through all pages and for each page i got the url by using the command ***driver.current_url()***. The urls were saved and stored into a list.

![image](https://user-images.githubusercontent.com/72921465/119182451-99434b00-ba7b-11eb-8ea5-a9a30e9b0265.png)

### Collecting and storing the data to a csv file
For each page using Selenium and Beautiful Soup i scraped the name, the price, the rating and the review counts for all results. The data was written in a csv file using Csv Writer

![image](https://user-images.githubusercontent.com/72921465/119183425-c0e6e300-ba7c-11eb-86e1-9e414e6372d5.png)

### Inserting the csv file into Pandas

The idea was to automatically locate on my computer the csv that was created before. To do this i combined the OS and Glob libraries. Using the ***os.getcwd()*** i grabbed the path of my current working directory (where the csv file would be saved). With the help of ***os.path.join*** i joined the path of the current working directory with the "*.csv" to get all the csv files in that path. To return the latest csv file i used ***os.path.getctime*** as a key in a max function. 

![image](https://user-images.githubusercontent.com/72921465/119183958-744fd780-ba7d-11eb-81c2-1e139a642d1b.png)

### Cleaning the csv file using Pandas

1) Keep only product rows

![image](https://user-images.githubusercontent.com/72921465/119185356-5be0bc80-ba7f-11eb-92e9-29b6d8a47e18.png)

2) Extract only digits from "Price" and "Review Counts" columns

![image](https://user-images.githubusercontent.com/72921465/119186134-533cb600-ba80-11eb-92cf-104aad2fcbd8.png)

3) Change column types

![image](https://user-images.githubusercontent.com/72921465/119186030-34d6ba80-ba80-11eb-99f9-fb73461900ac.png)

4) Sort the dataframe

![image](https://user-images.githubusercontent.com/72921465/119186183-6780b300-ba80-11eb-90a3-e2901b835fd6.png)

5) Export the dataframe to a new csv file. The "path" is the current working directory

![image](https://user-images.githubusercontent.com/72921465/119186328-9b5bd880-ba80-11eb-9963-67b484023595.png)

