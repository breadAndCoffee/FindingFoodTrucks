# Food Truck Finder

---

### Project Description

This repository contains a Python script for finding a food-truck based on latitude and longitude coordinates that you
can run in your shell!

# Usage

---

### Pre-requisites

This tool was built for Python 3. To set that up on your system,
follow [this guide](https://realpython.com/installing-python/). Once you have installed Python 3 you'll need to install
a few supporting libraries for this script to function properly. To do so use these commands:

1. `pip3 install sodapy` - This library will be used for interacting with the San Francisco Open Data API.

### Tool Usage

At the moment we support finding a food truck based on latitude and longitude search - we plan on adding functionality
to find multiple food trucks based on those coordinates. But to actually use the tool, you can run a command like this
from the directory of this script:

```commandline
# Syntax
python3 findFoodTrucks.py <LATITUDE> <LONGITUDE>

# Example
python3 findFoodTrucks.py 37.7865580501799 -122.40103337534973
```

Don't worry if you forget to add the two command line arguments, if you do we'll prompt you for that information.
