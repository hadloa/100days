#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
import pprint

url = 'https://api.sheety.co/42d9c8c88b600e298147017771843602/flightDeals/prices'
row = 2
def main():
    flight_sheety = DataManager(url=url)
    f_search = FlightSearch(url=None)
    sheet_data = flight_sheety.get_request_data()['prices']
    for city in sheet_data:
        if city['iataCode'] == '':
            f_search

if __name__ == "__main__":
    main()