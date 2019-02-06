# nws_python_scraper

Dependencies:  
selenium = "\*"  
pandas = "\*"  
lxml = "\*"

A scraper for National Weather Service website using Python, Selenium and Pandas.
This program reads ```cities.json``` as input. This file includes an arbitrary city name
and the URL pointing to the desired page on the National Weather Service site.

The sample includes 3 cities and URLs: Kailua HI, San Francisco and Chicago.

<i>To run the script:</i><br>
```python nws_scraper.py <enter>```
  
After a moment, you'll see Firefox launch and step through each URL, and about 9 pieces of data are scraped (the number of table rows can vary). Some data is scraped using selenium webdriver commmands such as driver.find_element_by_class_name.

For NWS data stored in a table, I read the table into a pandas dataframe, transposed it to rotate the keys into the column header and then further processed the data to utlimately get everything into a single python dictionary for each city.

The final data is converted back into the json format and written to a time-stamped file and also echoed to the console.

sample input file:
```
{
		"Name": "Chicago, IL",
		"NWS_URL": "https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.XEo_f8aIbM0"
}
```
sample Chicago output during the arctic vortex of January 2019
```
{
    "Name": "Chicago, IL",
    "Temperature": "-13\u00b0F",
    "Humidity": "60%",
    "Wind Speed": "W 20 mph",
    "Barometer": "30.30 in (1029.8 mb)",
    "Dewpoint": "-23\u00b0F (-31\u00b0C)",
    "Visibility": "10.00 mi",
    "Wind Chill": "-39\u00b0F (-39\u00b0C)",
    "Last update": "30 Jan 3:53 pm CST"
}
```
