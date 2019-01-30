
import json
from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
import pandas as pd

#driver = webdriver.Firefox()


'''  
create function get_temperature, etc.
These are simple selenium find_element_by_class
exercises.
'''


def get_temperature(url,driver):
    driver.get(url)
    data = driver.find_element_by_class_name('myforecast-current-lrg')
    location_data_dict = {'Temperature': data.text}  # if you don't append the .text method you get the ID,
                                                     # not the content string!
    #print(location_data_dict)
    return location_data_dict                        #returns a dictionary key:value pair

def get_station(url,driver):
    driver.get(url)
    data = driver.find_element_by_class_name('panel-title')  # TODO: unreliable, can return the wrong panel-title
    location_data_dict = {'Station': data.text}  # if you don't append the .text method you get the ID,
                                                     # not the content string!
    #print(location_data_dict)
    return location_data_dict                        #returns a dictionary key:value pair

def get_condition_description(url,driver):
    driver.get(url)
    data = driver.find_element_by_class_name('myforecast-current')
    location_data_dict = {'Description': data.text}  # if you don't append the .text method you get the ID,
                                                     # not the content string!
    #print(location_data_dict)
    return location_data_dict                        #returns a dictionary key:value pair

'''for current condition details, 

This code uses pandas to get the weather condition details 
(humidity, dew point, etc), which are stored in a table
on the NWS website. I'm using pandas to read the page
and then grab the table. The format of the table puts
the data type (ex. humidity) in column 1 and the value
in column 2. Using the pandas transpose method to rotate
the table 90 degrees so we end up with descriptive column
headers and one row of data (var transposed_table).
Then we use  the .to_dict method and generate a dict with
the data we want in individual list objects, each with our 
type and value. This is var dict_transposed, which we
iterate to extract each key value pair into var type_data_pair
and finally convert each into a dictionary.

may need to do something for degree unicode character (\u00b0) 
in the json output.'''


def get_condition_details(url,driver):
    initial_table = get_html_table_to_dataframe(url, 0)  # pass the url and load the 0th table on the page
    transposed_table = transpose_dataframe(initial_table)
    dict_transposed = transposed_table.to_dict('list')
    # above returns one dict for 1 row in the form {0: ['Humidity', '94%'],  ...
    # the part I care about is the list within each list item...

    condition_details = {}
    for i in range(len(dict_transposed)):
        type_data_pair = (dict_transposed[i])
        condition_detail = {type_data_pair[0]: type_data_pair[1]}
        condition_details.update(condition_detail)
    return(condition_details)


def get_html_table_to_dataframe(url,table_index):
    tables = pd.read_html(url)            # Returns list of all tables on page
    current_table = tables[table_index]   # Select table of interest
    return(current_table)


def transpose_dataframe(input_df):
    df1_transposed = input_df.T # or df1.transpose()
    return(df1_transposed)


def merge_dictionaries(name, temperature, condition_details):
    all_info ={}
    all_info.update(name)
    all_info.update(temperature)
    all_info.update(condition_details)
    return all_info
'''

REFERENCE NOTES

Here is example of the NWS website's condition detail HTML table (Jan 2019)
<div id="current_conditions_detail" class="pull-left">
		    <table>
            <tbody><tr>
            <td class="text-right"><b>Humidity</b></td>
            <td>81%</td>
            </tr>
            <tr>
            <td class="text-right"><b>Wind Speed</b></td>
            <td>NA</td>
            </tr>
            <tr>
            <td class="text-right"><b>Barometer</b></td>
            <td>NA</td>
            </tr>
            <tr>
            <td class="text-right"><b>Dewpoint</b></td>
            <td>44°F (7°C)</td>
            </tr>
            <tr>
            <td class="text-right"><b>Visibility</b></td>
            <td>NA</td>
            </tr>
                        <tr>
            <td class="text-right"><b>Last update</b></td>
            <td>
                25 Jan 7:43 am PST             </td>
            </tr>
		    </tbody></table>
		</div>


'''
