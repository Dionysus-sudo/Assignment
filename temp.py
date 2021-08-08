API_data = {'Delhi': [(31, 38, 31, 79)], 'Chandigarh': [(31, 34, 31, 54)], 'Indore': [(25, 25, 25, 81)], 'Mumbai': [(30, 37, 29, 74)], 'Kolkata': [(30, 37, 30, 89)], 'Texas': [(24, 25, 21, 73)], 'Shahjahanpur': [(33, 40, 33, 59)]} 
UI_data = {'Delhi': [[33, 43, 26, 69]]  ,'Chandigarh': [[33, 43, 26, 69]], 'Indore': [[23, 23, 25, 91]], 'Mumbai': [[30, 37, 27, 77]], 'Kolkata': [[30, 38, 28, 83]], 'Texas': [[27, 31, 27, 83]], 'Shahjahanpur': [[32, 43, 26, 80]]}

def compare_data(API_data, UI_data):

    for city in API_data.keys():
        try: #handles in case data not returned for a particular city from the UI.
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
            
            #Making observation on the variance in the two data sources for current temperature.
            difference_in_current_temp = api_current_temp - ui_current_temp
            difference = abs(api_current_temp - ui_current_temp)
            if difference_in_current_temp > 0:
                statement = f'Current temperature from API data({api_current_temp}C) is {difference}degree higher than the temperature from UI data for {city}.'
            elif difference_in_current_temp < 0:
                statement = f'Current temperature from API data({api_current_temp}C) is {abs(difference)}degree lower than the temperature from UI data for {city}.'
            else:
               statement = f'Current temperature from API data is exactly the same as the temperature from UI data for {city}.'
            observation.append(statement)

            #Making observation on the variance in the two data sources for realFeel temperature.
            difference_in_realFeel = api_realFeel - ui_realFeel
            difference = abs(api_realFeel - ui_realFeel)
            if difference_in_realFeel > 0:
                statement = f'Real Feel temperature from API data({api_realFeel}C) is {difference}degree higher than the temperature from UI data for {city}.'
            elif difference_in_realFeel < 0:
                statement = f'Real Feel temperature from API data({api_realFeel}C) is {difference}degree lower than temperature from UI data for {city}.'
            else:
               statement = f'Real Feel temperature from API data is exactly the same as the temperature from UI data for {city}.'
            observation.append(statement)

            #Making observation on the variance in the two data sources for Lowest temperature.
            difference_in_lowest = api_lowest_temp - ui_lowest_temp
            difference = abs(api_lowest_temp - ui_lowest_temp)
            if difference_in_lowest > 0:
                statement = f'Lowest temperature from API data({api_lowest_temp}C) is {difference}degree higher than the temperature from UI data for {city}.'
            elif difference_in_lowest < 0:
                statement = f'Lowest temperature from API data({api_lowest_temp}C) is {difference}degree lower than temperature from UI data for {city}.'
            else:
               statement = f'Lowest temperature from API data is exactly the same as the temperature from UI data for {city}.'
            observation.append(statement)

            #Making observation on the variance in the two data sources for Humidity temperature.
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


#compare_data(API_data, UI_data)

api_current_temp = 31
ui_current_temp = 26

print(abs((api_current_temp - ui_current_temp)) * 100/(api_current_temp))