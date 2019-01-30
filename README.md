# nws_python_scraper
A scraper for National Weather Service website using Python, Selenium and Pandas
This program reads cities.json as input. This file includes an arbitray city name
and the URL pointing to the desired page on the National Weather Service site.

The sample input file includes 3 cities, Kailua HI, San Francisco, CA and Chicago, IL.

<i>To run the script:</i><br>
python nws_scraper.py <enter>
  
After a moment, you'll see Firefox launch and  step through three different URLs.
At each URL, about 9 pieces of data are scraped. Some data is scraped using 
selenium webdriver commmands such as driver.find_element_by_class_name.
For weather data stored in a table, I used a pandas dataframe to grab the table,
transpose it to get the keys into the column header and then further
processed the data to utlimately get everything into a dictionary for each city.

The final data was converted back into the json format and written to a time-stamped
file, as well as echoed to the console.
