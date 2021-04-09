# Amazon_scraping_and_editing_data
Libraries that were used: Selenium, Beautiful soup, requests, csv, pandas, os, glob,

This code scrapes data from Amazon prooducts, saves it to csv and then cleans the csv.

1) The user enters a search item
2) Using Selenium it scrapes the name, the price, the rating and the review counts for all results for all pages.
3) Creates a csv that stores the data
4) Using OS and Glob module it finds the latest csv file that created in the current working directory
5) Import the latest csv to pandas, clean the dataframe and save it to the final csv
