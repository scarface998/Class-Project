# Weather application header
import requests
import json

api_key = "8635bc2c2e66727cc5d878f3875f35ec"

base_url_city = "http://api.openweathermap.org/data/2.5/weather?q="

base_url_zip = "http://api.openweathermap.org/data/2.5/weather?zip="


def main():

    while True:

        print("Thank you for using our current weather application!")

        location = input("Please enter your zip code or city name!")

        if len(location) == 5:

            finished_url_zip = base_url_zip + location + "&appid=" + api_key

            response = requests.get(finished_url_zip)

            print(response.json())

        else:

            finished_url_city = base_url_city + location + "&appid=" + api_key

            response = requests.get(finished_url_city)

            print(response.json())

        restart = input("Would you like to check another location? yes or no:")

        if restart == "yes":

            continue

        else:
            print("Thank you for using the weather tool!")

            break


main()
