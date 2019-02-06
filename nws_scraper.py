import json
import nws_scraper_utils
from selenium import webdriver
import time

time_stamp = time.strftime("%Y%m%d-%H%M%S")
time_stamp_filename = time_stamp + '_nws_log.json'

driver = webdriver.Firefox()

'''--------- Define CityCurrentStats class --------'''

class CityObject:
    def __init__(self, name, url, driver):
        self.name = {'Name': name}
        self.url = {'URL' : url}
        self.temperature = nws_scraper_utils.get_temperature(url, driver)
        self.condition_description = nws_scraper_utils.get_condition_description(url, driver)
        self.station = nws_scraper_utils.get_station(url, driver)
        self.condition_details = nws_scraper_utils.get_condition_details(url, driver)

def main():

    ''' read the user input file in json format and convert to dict name:url'''
    try:
        data_input_file = 'cities.json'  # read user input file
        with open(data_input_file) as json_data:  # This returns a list of dictionaries
            cities = json.load(json_data)
    except FileNotFoundError:
        print('quitting, can\'t input file ', data_input_file)
        exit()


    '''for each dict in list , create a CityObject and populate it from NWS data'''
    for city_pair in cities:                # This iterates and returns individual dictionaries from the list
        name = (city_pair['Name'])          # and we extract the value from each key here...
        url = (city_pair['NWS_URL'])
        city = CityObject(name,url,driver)         # create a City Object
        all_info = nws_scraper_utils.merge_dictionaries(city.name, city.temperature, city.condition_details)


        # Finally, append each city dictionary to json file
        # with a time-stamped filename
        final_output_json = json.dumps(all_info, indent = 4)
        # Open new json file if not exist it will create
        fp = open(time_stamp_filename, 'a')  # append
        # write to json file
        fp.write(final_output_json)
        print(final_output_json)
    # close the output file once IN THE OUTER LOOP
    fp.close()

    driver.close()
    driver.quit()


if __name__ == "__main__":
    main()