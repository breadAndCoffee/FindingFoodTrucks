import sys
import pandas as pd
from sodapy import Socrata
import pprint


def find_food_truck():

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
    results = client.get("rqzj-sfat", "json", latitude = latitude, longitude = longitude)

    pprint.pprint(results)


if __name__ == '__main__':
    find_food_truck()
