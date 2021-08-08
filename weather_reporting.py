import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions  
import time
import json

'''
Phase1
Creating a Selenium driver instance and configuring with wait of 5 seconds post testing(manual) the UI data source.
Function 'get_weather_data_from_UI' takes a list of cities and on lopping:
    1. Identify the location searchbox and waits for it to become clickable, enter the location and clicks on the most relevant result(first).
    2. Explicitly waits for 2 second as it was found that on changing the city, the page data was taking time in refreshing, hence the wait.
    3. Finding the current weather data + I've also added the realFeel and min. temp along with Humidity.
    4. Stores the weather data in dict() to be used later for comparison.
'''

def get_weather_data_from_UI(cities):
    city_data = dict()
    driver = webdriver.Chrome()
    delay = 5#seconds
    driver.get('https://weather.com/')

    for i in range(len(cities)):
        weather_details = list()
        try:
            wait = WebDriverWait(driver, delay)
            wait.until(EC.element_to_be_clickable((By.ID, 'LocationSearch_input')))
            driver.find_element_by_id("LocationSearch_input").clear()
            driver.find_element_by_id("LocationSearch_input").send_keys(cities[i].lower())
            wait.until(EC.element_to_be_clickable((By.ID, 'LocationSearch_listbox-0')))
            time.sleep(2)

            driver.find_element_by_id('LocationSearch_listbox-0').click()
            current_temp = int(driver.find_element_by_class_name('CurrentConditions--tempValue--1RYJJ').text[:-1])
            realFeel = int(driver.find_element_by_class_name('TodayDetailsCard--feelsLikeTempValue--3eUBp').text[:-1])
            temp_min = int(driver.find_element_by_class_name('WeatherDetailsListItem--wxData--2bzvn').text[-3:-1])
            humidity = int(driver.find_element_by_xpath('//*[@id="todayDetails"]/section/div[2]/div[3]/div[2]/span').text[-3:-1])
            
            weather_details.append((current_temp, realFeel, temp_min, humidity))

            city_data[cities[i]] = weather_details
            print(f'For {cities[i]}:\nTemp: {current_temp} | Feels like: {realFeel} | Lowest: {temp_min} | Humidty: {humidity}\n')

        except exceptions.ElementNotInteractableException as e:
            print(e)
        except exceptions.StaleElementReferenceException as e:
            print(e)
        except exceptions.TimeoutException as e:
            print(f'Timed out for the City: {cities[i]}')
        except exceptions.NoSuchElementException as e:
            print(e)

    driver.close()
    return city_data


'''
Phase 2:
Here's I've used the current weather API (from https://openweathermap.org/current) with Units set as Metrics for comparison.
This Phase involves:
    1. Hitting the current weather API.
    2. Parsing the data from the response in accordance to the same metrics using in Phase1.
    3. Storing the data in another dict() to be used for comparison later.
'''

def get_weather_data_from_API(cities):
    API_key = 'f447d3ce3da49085a0f1834d64964e0d'
    city_data = dict()

    for i in range(len(cities)):
        weather_details = list()
        city = cities[i]
        try:
            URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_key}'
            response = requests.get(URL)
            response_json = json.loads(response.text)
            current_temp = round(int(response_json['main']['temp']))
            realFeel = round(int(response_json['main']['feels_like']))
            temp_min = round(int(response_json['main']['temp_min']))
            humidity = round(int(response_json['main']['humidity']))
        
            weather_details.append((current_temp, realFeel, temp_min, humidity))
            city_data[cities[i]] = weather_details
            print(f'For {city}:\nTemp: {current_temp} | Feels like: {realFeel} | Lowest: {temp_min} | Humidty: {humidity}\n')
        
        except KeyError:
            print(f'KeyError: {city} not found')    
    return city_data


'''
Phase3 partI:
Now that we've got the functions capable of capture the data through UI Automation & API calls respectively, we'll not compare the data sources.
Function 'compare_data' takes is invoked with the list of the cities and does the following:
    1. Calls 'get_weather_data_from_API' & 'get_weather_data_from_UI' to get the data in the form of dict()s.
    2. Loops over the cities and parse each paramter.
    3. Compare the same paramter for each city and makes and makes an observation basis of their difference.
    4. Logs the output based on observable gradient between the paramters used.
'''


def compare_data(*args):
    cities = args[0]
    API_data = get_weather_data_from_API(cities)
    UI_data = get_weather_data_from_UI(cities)

    for city in API_data.keys():
        try:
            api = API_data[city]
            ui = UI_data[city]

            api_current_temp = api[0][0]
            ui_current_temp = ui[0][0]
            api_realFeel = api[0][1]
            ui_realFeel = ui[0][1]
            api_lowest_temp = api[0][2]
            ui_lowest_temp = ui[0][2]
            api_humidity = api[0][3]
            ui_humidity = ui[0][3]

            observation = list()
            
            difference_in_current_temp = api_current_temp - ui_current_temp
            difference = abs(api_current_temp - ui_current_temp)
            if difference_in_current_temp > 0:
                statement = f'Current temperature from API data({api_current_temp}C) is {difference}degree higher than the temperature from UI data for {city}.'
            elif difference_in_current_temp < 0:
                statement = f'Current temperature from API data({api_current_temp}C) is {abs(difference)}degree lower than the temperature from UI data for {city}.'
            else:
               statement = f'Current temperature from API data is exactly the same as the temperature from UI data for {city}.'
            observation.append(statement)

            difference_in_realFeel = api_realFeel - ui_realFeel
            difference = abs(api_realFeel - ui_realFeel)
            if difference_in_realFeel > 0:
                statement = f'Real Feel temperature from API data({api_realFeel}C) is {difference}degree higher than the temperature from UI data for {city}.'
            elif difference_in_realFeel < 0:
                statement = f'Real Feel temperature from API data({api_realFeel}C) is {difference}degree lower than temperature from UI data for {city}.'
            else:
               statement = f'Real Feel temperature from API data is exactly the same as the temperature from UI data for {city}.'
            observation.append(statement)

            difference_in_lowest = api_lowest_temp - ui_lowest_temp
            difference = abs(api_lowest_temp - ui_lowest_temp)
            if difference_in_lowest > 0:
                statement = f'Lowest temperature from API data({api_lowest_temp}C) is {difference}degree higher than the temperature from UI data for {city}.'
            elif difference_in_lowest < 0:
                statement = f'Lowest temperature from API data({api_lowest_temp}C) is {difference}degree lower than temperature from UI data for {city}.'
            else:
               statement = f'Lowest temperature from API data is exactly the same as the temperature from UI data for {city}.'
            observation.append(statement)

            difference_in_humidity = api_humidity - ui_humidity
            difference = abs(api_humidity - ui_humidity)
            if difference_in_humidity > 0:
                statement = f'Humidity from API data({api_humidity}%) is {difference}% higher than the humidity from UI data for {city}.'
            elif difference_in_humidity < 0:
                statement = f'Humidity from API data({api_humidity}%) is {difference}% lower than humidity from UI data for {city}.'
            else:
               statement = f'Humidity from API data is exactly the same as the humidity from UI data for {city}.'
            observation.append(statement)
            
            print(f'{observation[0]}\n{observation[1]}\n{observation[2]}\n{observation[3]}\n')

        except KeyError:
            print(f'{city} is missing from UI data')


if __name__ == '__main__':
    compare_data(['Delhi', 'Chandigarh', 'Indore', 'Mumbai', 'Kolkata', 'Texas', 'newyork', 'Shahjahanpur'])



