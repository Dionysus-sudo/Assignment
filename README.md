
# Weather Reporting

This project demonstrates the usage of Selenium Webdriver Automation and a REST API to obtain the live weather data for any City and their comparison.
Observations were made on the basis of acceptable deviance among the same paramets in the two difference source.







## Project Structure

This project contains 'weather_reporting.py' which compares the data from API and UI and another file 'test_variance' which accepts % of variance and logs the observations on comparison to the data sources.

## Install Depedencies

Targeted website: https://weather.com/

requirements.txt https://github.com/Dionysus-sudo/Assignment/blob/main/requirements.txt

Install all with: 

```bash
  pip install -r requirements.txt
```
or 

Install selenium using the below command

```bash
  pip install selenium
```

Install requests using the below command

```bash
  pip install requests
```





## Usage/Examples

```python
from weather_reporting import get_weather_data_from_API, get_weather_data_from_UI

if __name__ == '__main__':
    compare_data({'City' : ['Delhi', 'Chandigarh', 'Indore', 'Mumbai', 'Kolkata', 'Texas', 'Shahjahanpur'],
'Variance' : 4, 'validate_variance_for': 'current_temp'
})
```
  

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
