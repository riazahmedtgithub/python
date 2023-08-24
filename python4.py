# Weather program - Final project

import requests

def display(weather_output,metrics):    #  Function to display the output in proper format
    if metrics is None: unit = "Kelvin"
    elif metrics == "imperial": unit = "Fahrenheit"
    else: unit = "Celsius"
    print ('{:40}{} {}'.format("Current temperature is:",weather_output["main"]["temp"],unit))
    print('{:40}{} {}'.format("Temperature feels like:", weather_output["main"]["feels_like"], unit))
    print('{:40}{} {}'.format("Minimum temperature is:", weather_output["main"]["temp_min"], unit))
    print('{:40}{} {}'.format("Maximum temperature is:", weather_output["main"]["temp_max"], unit))
    print('{:40}{} {}'.format("Pressure is:", weather_output["main"]["pressure"], "hPa"))
    print('{:40}{} {}'.format("Humidity is:", weather_output["main"]["humidity"], "%"))
    print('{:40}{}'.format("General Weather is:", weather_output["weather"][0]["description"].capitalize() + "\n"))

def metric_finder(metric_option):    #  Function to determine the preference of metrics
    if metric_option == 1:   return None
    elif metric_option == 2:  return "imperial"
    elif metric_option == 3:  return "metric"

def location_weather_apicall(*zip_code):    #  Function to find out the latitue and longitude as well as the call to weather API
    try:
        if len(zip_code[0]) == 1:
            payload = {"zip": zip_code[0][0], "appid" : "XXXX"}
            response = requests.get("https://api.openweathermap.org/geo/1.0/zip", params = payload)
            response.raise_for_status()
        elif len(zip_code[0]) == 2:
            payload = {"appid": "XXXX"}
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={zip_code[0][0]},{zip_code[0][1]},US" , params = payload)
            response.raise_for_status()
        elif len(zip_code[0]) == 3:
            payload = {"lat": zip_code[0][0], "lon": zip_code[0][1], "appid": "XXXX", "units": zip_code[0][2]}
            weather_output = requests.get("https://api.openweathermap.org/data/2.5/weather", params=payload)
            display(weather_output.json(),zip_code[0][2])
    except requests.exceptions.HTTPError as error:
            print("You have encountered an HTTP Error.  If you are entering zipcode, please check whether you are entering a valid 5 digit zip code or if you are entering city/state, make sure valid input is given")
    except requests.exceptions.ReadTimeout as errrtimeout:
        print("Time out happened")
    except requests.exceptions.ConnectionError as conerror:
        print("Connection error encountered")
    except requests.exceptions.RequestException as errexception:
        print("Exception request encountered")
    else:
        if len(zip_code[0]) != 3 and 'coord' not in response.json().keys(): #response.json()['lat'] and response.json()['lon']:
            latitude = response.json()['lat']
            longitude = response.json()['lon']
            return latitude, longitude
        elif len(zip_code[0]) != 3 and 'coord' in response.json().keys(): #response_city_state.json()['coord']['lat'] and response_city_state.json()['coord']['lon']:
            latitude = response.json()['coord']['lat']
            longitude = response.json()['coord']['lon']
            return latitude, longitude

def main():
    while True:
        try:
            search_option = int(input("Would you like to search by zipcode or by city.\nEnter 1 for zipcode.\nEnter 2 for city.\nEnter 3 to quit.\n"))
            if search_option == 1 or search_option == 2:
                metric_option = int(input(
                "How would you like the temperature to be displayed.\nEnter 1 to display in Kelvin.\nEnter 2 for Farenheit.\nEnter 3 Celsius.\n"))
        except ValueError:
            print("Please enter only 1 or 2 or 3 to quit")
        else:
            list = []
            if search_option == 1 and (metric_option == 1 or metric_option == 2 or metric_option == 3):
                zip_code = (input("Please input the zipcode\n"))
                if zip_code.isnumeric() and len(zip_code) == 5:
                    zip_code = int(zip_code)
                    list.append(zip_code)
                    try:

                        latitude,longitude =  location_weather_apicall(list)
                        metrics = metric_finder(metric_option)
                        print(f"The weather for the entered zip code {zip_code} is: \n")
                        print("===============================================\n")
                        list=[]
                        list = [latitude,longitude,metrics]
                    except:
                        pass
                    location_weather_apicall(list)
                else:
                    print("Please enter a valid 5 digit zip code")
            elif search_option == 2 and (metric_option == 1 or metric_option == 2 or metric_option == 3):
                city = input("Please input the city\n")
                state = input("Please input the state code\n")
                list = [city,state]
                try:
                    latitude,longitude = location_weather_apicall(list)
                    metrics = metric_finder(metric_option)
                    print(f"The weather for the entered city {city.capitalize()} and state {state.upper()}  is: \n")
                    print("===========================================================\n")
                    list=[]
                    list = [latitude, longitude, metrics]
                    location_weather_apicall(list)
                except:
                    pass
            elif search_option == 3:
                break
            else:
                print("Enter only the numbers corresponding to the options shown\n")


if __name__ == '__main__':
    main()




Program output:
===============

Would you like to search by zipcode or by city.
Enter 1 for zipcode.
Enter 2 for city.
Enter 3 to quit.
1
How would you like the temperature to be displayed.
Enter 1 to display in Kelvin.
Enter 2 for Farenheit.
Enter 3 Celsius.
2
Please input the zipcode
75024
The weather for the entered zip code 75024 is: 

===============================================

Current temperature is:                 103.77 Fahrenheit
Temperature feels like:                 109.18 Fahrenheit
Minimum temperature is:                 99.41 Fahrenheit
Maximum temperature is:                 107.49 Fahrenheit
Pressure is:                            1012 hPa
Humidity is:                            30 %
General Weather is:                     Scattered clouds

Would you like to search by zipcode or by city.
Enter 1 for zipcode.
Enter 2 for city.
Enter 3 to quit.







