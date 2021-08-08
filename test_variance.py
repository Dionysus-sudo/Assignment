from weather_reporting import get_weather_data_from_API, get_weather_data_from_UI

'''
Phase3 partII:
This script compares the data captured via API againt that of UI automation and and asserts if the variance is in the acceptable range.
Function 'compare_data' does the following:

    1. Accepts the argument in the form of Configurable JSON input with following parameters:
        i. 'City': A list of city names.
        ii. 'Variance': an acceptable % of deviation between the API & UI data.
        iii. 'validate_variance_for': the parameter you want to target and supply a degree of variance to.
             Acceptable inputs for 'validate_variance_for' are:
                a. current_temp: current temperature of a city.
                b. realFeel: Feels like temperature of a city.
                c. min_temp: minimum forcasted temperature.
                d. humidity: as the name reflects, the humidity observed.

    2. Parse the cities, variance and validate_variance for and loop over the cities.
    3. Obtain the requested paramter's value and compare the deviance found between the two datasets.
    4. Calculate the percentage deviation against the acceptable Variance and assert the result to make observation.
'''

def compare_data(*args):
    cities = args[0]['City']
    variance = args[0]['Variance']
    validate_for = args[0]['validate_variance_for']
    API_data = get_weather_data_from_API(cities) 
    UI_data = get_weather_data_from_UI(cities)
        
    for city in cities:
        if city in API_data.keys() and city in UI_data.keys():
            api = API_data[city]
            ui = UI_data[city]
            
            if validate_for == 'current_temp':
                api_current_temp = api[0][0]
                ui_current_temp = ui[0][0]
                try:
                    assert abs((api_current_temp - ui_current_temp)) * 100 /(api_current_temp) <= variance, f'Current Temperature difference between API_data({api_current_temp}C) & UI data({ui_current_temp}C) in {city} is beyond the acceptable variance of {variance}%.'
                    print(f'Success: Comparison of {validate_for} in {city} is in acceptable variance of variance {variance}%.')
                except AssertionError as e:
                    print(e)
            
            if validate_for == 'realFeel':
                api_realFeel = api[0][1]
                ui_realFeel = ui[0][1]
                try:
                    assert abs((api_realFeel - ui_realFeel)) * 100 / (api_realFeel) <= variance, f'Real Feel Temperature difference between API_data({api_realFeel}C) & UI data({ui_realFeel}C) in {city} is beyond the acceptable variance of {variance}%.'
                    print(f'Success: Comparison of {validate_for} in {city} is in acceptable variance of variance {variance}%.')
                except AssertionError as e:
                    print(e)
            
            if validate_for == 'min_temp':
                api_min_temp = api[0][2]
                ui_min_temp = ui[0][2]
                try:
                    assert abs((api_min_temp - ui_min_temp)) * 100 / (api_min_temp) <= variance, f'Difference between Minumum Temperature API_data({api_min_temp}C) & UI data({ui_min_temp}C) in {city} is beyond the acceptable variance of {variance}%.'
                    print(f'Success: Comparison of {validate_for} in {city} is in acceptable variance of variance {variance}%.')
                except AssertionError as e:
                    print(e)

            
            if validate_for == 'humidity':
                api_humidity = api[0][3]
                ui_humidity = ui[0][3]
                try:
                    assert abs((api_humidity - ui_humidity)) * 100 / (api_humidity) <= variance, f'Real Feel Humidity difference between API_data({api_humidity}%) & UI data({ui_humidity}%) in {city} is beyond the acceptable variance of {variance}%.'
                    print(f'Success: Comparison of {validate_for} in {city} is in acceptable variance of variance {variance}%.')
                except AssertionError as e:
                    print(e)
    return

if __name__ == '__main__':
    compare_data({'City' : ['Delhi', 'Chandigarh', 'Indore', 'Mumbai', 'Kolkata', 'Texas', 'Shahjahanpur'],
'Variance' : 4, 'validate_variance_for': 'current_temp'
})



