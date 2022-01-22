import bisect
import sys
import pandas as pd
from sodapy import Socrata
import pprint
import math
import numpy


def find_food_truck():
    pd.set_option("display.max_rows", None)

    # Get the latitude and longitude (either from CLI input or prompted).
    if len(sys.argv) <= 1 or len(sys.argv) > 3:
        print("We'll just need some coordinates to search for a food truck.")
        latitude = input("What latitude should we search for food trucks at? ")
        longitude = input("What longitude should we search for food trucks at? ")

    else:
        latitude = sys.argv[1]
        longitude = sys.argv[2]

    # print(latitude)
    # print(longitude)

    # Initialize unauthenticated client per Socrata API
    #   https://dev.socrata.com/foundry/data.sfgov.org/rqzj-sfat

    client = Socrata("data.sfgov.org", None)
    results = client.get("rqzj-sfat")
    results_df = pd.DataFrame.from_records(results)
    temp = []
    for index, row in results_df.iterrows():
        if row["status"] == "APPROVED" and row["facilitytype"] == "Truck":
            distance = calculate_distance(latitude, row["latitude"], longitude, row["longitude"])
            bisect.insort_left(temp, (distance, row["applicant"]))

    five_set = set()
    i = 0
    for entry in temp:
        if i >= 5:
            exit()
        if entry[1] not in five_set:
            five_set.add(entry[1])
            print(entry)
            i = i + 1

        # print(row["applicant"] + ", " + row["latitude"] + ", " + row["longitude"] + ", " + row[
        #    "status"] + "\t Distance Of: " + str(distance))


def get_first_five_unique():
    pass


def calculate_distance(searching_latitude, latitude_actual, searching_longitude, longitude_actual):
    latitude_distance = (float(latitude_actual) - float(searching_latitude)) ** 2
    longitude_distance = (float(longitude_actual) - float(searching_longitude)) ** 2
    return math.sqrt(latitude_distance + longitude_distance)


def find_result_in_dataframe(dataframe, latitude, longitude):
    print("")


class FoodTruck:
    def __init__(self, latitude, longitude, name):
        pass


if __name__ == '__main__':
    find_food_truck()
