import bisect
import sys
import pandas as pd

from sodapy import Socrata
from geopy.distance import geodesic


def find_food_truck():
    # Get the latitude and longitude (either from CLI input or via prompt).
    if len(sys.argv) <= 1 or len(sys.argv) > 3:
        print("We'll just need some coordinates to search for a food truck.")
        latitude = input("What latitude should we search for food trucks at? ")
        longitude = input("What longitude should we search for food trucks at? ")

    else:
        latitude = sys.argv[1]
        longitude = sys.argv[2]

    # Initialize unauthenticated client per Socrata API
    #   https://dev.socrata.com/foundry/data.sfgov.org/rqzj-sfat
    client = Socrata("data.sfgov.org", None)

    # we use the Socrata client's support for SoQL keywords to query the API endpopint just the results which are:
    # 1. Food Trucks (not push carts)
    # 2. Whose permit status is `APPROVED`
    results = pd.DataFrame.from_records(
        client.get("rqzj-sfat", "JSON", where="status LIKE 'APPROVED' AND facilitytype LIKE 'Truck'"))
    food_trucks_sorted_by_distance = get_food_trucks_sorted_by_distance((latitude, longitude), results)
    print_nearest_unique_food_trucks(food_trucks_sorted_by_distance)


def get_food_trucks_sorted_by_distance(searchingCoordinate, results):
    """
    Iterates over the `results` data frame and finds the five closest food trucks in O(n log(n)) time.
    We craft a sorted tuple array (food_trucks_sorted_by_distance) which has a tuple of: <distance, [applicant, address]>

    This function leverages the `bisect` libraries `insort_left` method.

    I'd considered creating a custom data type for the food truck object and implementing a comparator method and
    then sorting an array of those objects by distance, but decided that the extra space needed wasn't justified
    when I could achieve the same results during runtime using the aforementioned method / library.

    :param latitude: the latitude we want to search for food truck options at.
    :param longitude: the longitude we want to search for food truck options at.
    :param results: the dataframe representation of the of dataset's records
    :return: an array of food trucks - we print the top five closest carts here.
    """
    food_trucks_sorted_by_distance = []

    for index, row in results.iterrows():
        if row["status"] == "APPROVED" and row["facilitytype"] == "Truck":
            distance = geodesic(searchingCoordinate, (row["latitude"], row["longitude"])).miles
            bisect.insort_left(food_trucks_sorted_by_distance, (distance, [row["applicant"], row["address"]]))

    return food_trucks_sorted_by_distance


def print_nearest_unique_food_trucks(food_trucks_sorted_by_distance):
    """
    Print the first five unique food trucks - I noticed the data had some repeating trucks, in terms of address +
    applicant (not objectId). I didn't think it made sense to show the same truck multiple times, so I
    keep a set of the applicants and only print the first five unique food trucks with their address and distance from
    the coordinate searched for.

    :param food_trucks_sorted_by_distance: list of tuples in the form of (distance, [applicant, address])
    :return:
    """
    five_set = set()
    i = 0

    for entry in food_trucks_sorted_by_distance:
        if i >= 5:
            exit()
        if entry[1][0] not in five_set:
            five_set.add(entry[1][0])
            i = i + 1
            print(str(i) + ". " + entry[1][0].title() + " - " + entry[1][1].title()
                  + " (Distance: " + "{:.2f}".format(entry[0]) + "miles)")


if __name__ == '__main__':
    find_food_truck()
