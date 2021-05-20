# Amazon_scraping_and_editing_data
This class scrapes data from an Amazon prooduct, saves them to a csv and then cleans the csv using Pandas library. Some of the libraries that were used are: *Selenium, Beautiful soup, requests, csv, pandas, os, glob*.

## Class Analysis 

1) First the user inputs a search item and the amazon page opens in a Google Chrome window.  

2) Next step is to get the urls of all the pages for the item that was inserted. To do this i used Selenium. By locating the "Next" button *(driver.find_element_by_xpath)* i clicked it to navigate through all pages and for each page i got the url by using the command *driver.current_url()*. The urls were saved and stored into a list.

3) For each page using Selenium and Beautiful Soup i scraped the name, the price, the rating and the review counts for all results.
4) The data was written in a csv file using Csv Writer.
5) Next step was to automatically locate on my computer the csv that was created before. To do this i used the OS and Glob library. Using the *os.getcwd()* i grabbed the path of my current working directory (where the csv file would be saved). With the help of *os.path.join* i joined the path of the current working directory with the "*.csv" to get all the csv files in that path. 
6) Import the latest csv to pandas, clean the dataframe and save it to the final csv


