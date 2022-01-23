# Food Truck Finder
## Project Description

---

This repository contains a Python script for finding a food-truck based on latitude and longitude coordinates that you
can run in your shell!


## Project Reflection

---
After spending approximately 3 or so hours of focused work on this - I'm going to finish. Here are some thoughts I have looking back on the project / my implementation. 

#### Design Decisions
1. **Using The `bisect` [Library](https://docs.python.org/3/library/bisect.html)** - While using this saved some space (in memory), it would have been faster to implement the other solution (see the comment beginning with `I'd considered`). This could have left _more time to set up tests_.
2. **Calculating Distance** - For calculating distance, I'd originally set up a method which calculated the distance between two latitude and longitude points. While this worked (and got the same distance ordering as the final solution) - the ability for the `geopy` library to support converting the distance to miles I weighed worth it. Again, had I made that choice earlier _I'd have had more time to set up tests._
3. **Uniqueness + What Food Trucks To Consider** - The dataset had a lot of entries which had the same `Applicant` + `Address` item(s). Since this was not a question where I could interact with the stakeholder(s) to clarify ambiguity - I made what I think was the best call with the information that I had at hand. (This is the same reason I'd decided to only consider trucks which had the `Approved` status ) 
#### Testing
1. **Solution Structure** - I was designing this system with testing in mind - with many small easily testable method(s). However, due to the reasons outlined above, I didn't have enough time to spend setting up tests. 
   1. Tangentially, while I do plenty of scripting in this language for University / Personal Projects I don't use it enough to be as familiar with the testing frameworks available as I am in Java (`Mockito` / `JUnit`)

#### What Would I Do Next 
1. **Setup Testing** - As outlined above I didn't get a chance to set up tests for these methods, and I think it would have been good to do that (a step for true _production-ization_ )
2. **Graceful Error Handling / Input Validation** - Another one of the things I'd originally called out in the project roadmap was adding input validation. Right now if we try and execute the script with alphabetic inputs, it fails throwing a `ValueError`. It would be easy enough to check the validity of the inputs I just did not get around to it.
3. **Setting Up Map Linking** - A feature I thought of towards the end was taking two longitude and latitude points and invoking an API to get the shortest walking or driving path between them and returning it to the user. This would be used to find a path to their destination from their location (the coordinates they entered). 
4. **Unique Flag** - I would have liked to setup a flag so that the user could decide for themselves whether to look at the five closest _unique_ food trucks or not - but I never got a chance to set that up. 
 
## Usage

---

#### Pre-requisites

This tool was built for Python 3. To set that up on your system,
follow [this guide](https://realpython.com/installing-python/). Once you have installed Python 3 you'll need to install
a few supporting libraries for this script to function properly. To do so use these commands:

1. `pip3 install sodapy` - This library is used for interacting with the San Francisco Open Data API.
2. `pip3 install geopy` - This library is used for setting up the distance calculator which returns a value in miles.
3. `pip3 install pandas` - This library is used for data handling within the script. 

#### Tool Usage

In order to find the five closest food trucks to you, you just need to run the command as outlined below from the directory of this script:

```commandline
# Syntax
python3 findFoodTrucks.py <LATITUDE> <LONGITUDE>

# Example
python3 findFoodTrucks.py 37.7865580501799 -122.40103337534973

# Example Output
1. Momo Innovation Llc - 667 Mission St (Distance: 0.00miles)
2. Senor Sisig - 120 02Nd St (Distance: 0.10miles)
3. El Calamar Perubian Food Truck - 85 02Nd St (Distance: 0.15miles)
4. Treats By The Bay Llc - 201 02Nd St (Distance: 0.17miles)
5. Roadside Rotisserie Corporation / Country Grill - 1 Post St (Distance: 0.17miles)
```

Don't worry if you forget to add the two command line arguments, if you do we'll prompt you for that information.

## Project Road Map

---
1. Break latitude + longitude retrieval out into own method w/ tests + input validation (i.e. confirm the input is numeric).
2. Implement latitude + longitude fuzzy search.
