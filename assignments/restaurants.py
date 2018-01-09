import tkinter.filedialog
"""
A restaurant recommendation system.

Here are some example dictionaries.  These correspond to the information in
restaurants_small.txt.

Restaurant name to rating:
# dict of {str: int}
{'Georgie Porgie': 87,
 'Queen St. Cafe': 82,
 'Dumplings R Us': 71,
 'Mexican Grill': 85,
 'Deep Fried Everything': 52}

Price to list of restaurant names:
# dict of {str, list of str}
{'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
 '$$': ['Mexican Grill'],
 '$$$': ['Georgie Porgie'],
 '$$$$': []}

Cuisine to list of restaurant names:
# dict of {str, list of str}
{'Canadian': ['Georgie Porgie'],
 'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
 'Malaysian': ['Queen St. Cafe'],
 'Thai': ['Queen St. Cafe'],
 'Chinese': ['Dumplings R Us'],
 'Mexican': ['Mexican Grill']}

With this data, for a price of '$' and cuisines of ['Chinese', 'Thai'], we
would produce this list:

    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
"""


# The file containing the restaurant data.
filename = 'C:/Users/haoli/OneDrive/Documents/GitHub/LearnToProgramCraftingQualityCode/assignments/restaurants.txt'


def recommend(file, price, cuisines_list):
    """(file open for reading, str, list of str) -> list of [int, str] list

    Find restaurants in file that are priced according to price and that are
    tagged with any of the items in cuisines_list.  Return a list of lists of
    the form [rating%, restaurant name], sorted by rating%.
    """

    # Read the file and build the data structures.
    # - a dict of {restaurant name: rating%}
    # - a dict of {price: list of restaurant names}
    # - a dict of {cusine: list of restaurant names}
    name_to_rating, price_to_names, cuisine_to_names = read_restaurants(file)


    # Look for price or cuisines first?
    # Price: look up the list of restaurant names for the requested price.
    names_matching_price = price_to_names[price]

    # Now we have a list of restaurants in the right price range.
    # Need a new list of restaurants that serve one of the cuisines.
    names_final = filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)

    # Now we have a list of restaurants that are in the right price range and serve the requested cuisine.
    # Need to look at ratings and sort this list.
    result = build_rating_list(name_to_rating, names_final)

    # We're done!  Return that sorted list.
    return result

def build_rating_list(name_to_rating, names_final):
    """ (dict of {str: int}, list of str) -> list of list of [int, str]

    Return a list of [rating%, restaurant name], sorted by rating%

    >>> name_to_rating = {'Georgie Porgie': 87,
     'Queen St. Cafe': 82,
     'Dumplings R Us': 71,
     'Mexican Grill': 85,
     'Deep Fried Everything': 52}
    >>> names_final = ['Queen St. Cafe', 'Dumplings R Us']
    >>> build_rating_list(name_to_rating, names_final)
    [[82, 'Queen St. Cafe'], [71, 'Dumplings R Us']]
    """
    sorted_rating = []
    for rest in names_final:
        if rest in name_to_rating:
            sorted_rating.append([int(name_to_rating[rest]),rest])
    sorted_rating.sort(reverse = True)
    
    return sorted_rating
                           
def filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list):
    """ (list of str, dict of {str: list of str}, list of str) -> list of str

    >>> names_matching_price = ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything']
    >>> cuisine_to_names = {'Canadian': ['Georgie Porgie'],
     'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
     'Malaysian': ['Queen St. Cafe'],
     'Thai': ['Queen St. Cafe'],
     'Chinese': ['Dumplings R Us'],
     'Mexican': ['Mexican Grill']}
    >>> cuisines_list = ['Chinese', 'Thai']
    >>> filter_by_cuisine(names_matching_price, cuisine_to_names, cuisines_list)
    ['Queen St. Cafe', 'Dumplings R Us']
    """
    price_and_cuisine = []
    # look at each name in the price range
    for rest in names_matching_price:
        # inside the cuisines_list for each cuisine
        for cuis in cuisines_list:
            # if the restaurant name is in the cuisine_to_names dict under
            # the cuis key, append the restaurant name to the result list
            if rest in cuisine_to_names[cuis]:
                price_and_cuisine.append(rest)

    return price_and_cuisine
    
def read_restaurant(file):
    """(file) -> (dict, dict, dict)

    Return a tuple of three dictionaries based on the information in the file:

    - a dict of {restaurant name: rating%}
    - a dict of {price: list of restaurant names}
    - a dict of {cusine: list of restaurant names}
    """

    from_file = open(file, 'r')
    # Create accumulators and accumulate information as we read each restaurant.
    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = {}

    list_of_restaurant_info = get_info_from_file(file)

    for rest in list_of_restaurant_info:
        # build name_to_rating dict
        # to create a keyword restaurant name, and assign it the value of its rating.
        name_to_rating[rest[0]] = rest[1]

        # build price_to_names dict
        # two cases, key price not in the key, OR in the dictionary already
        if not rest[2] in price_to_names:
            price_to_names[rest[2]] = [rest[0]]
        else:
            price_to_names[rest[2]].append(rest[0])

        # build cuisine_to_names dict
        for cuis in rest[3]:
            if not cuis in cuisine_to_names:
                cuisine_to_names[cuis] = [rest[0]]
            else:
                cuisine_to_names[cuis].append(rest[0])
    
    return (name_to_rating, price_to_names, cuisine_to_names)
    
def get_info_from_file(filename):
    '''(file) -> list of list of restaurant information

    Return a list containing a list of each restaurant information
    '''
    rest_file = open(filename,'r')
    # set up a list of lists to store info in the following format
    #[[name, rating%, price, cuisine],[name, rating%, price, cuisine],...]
    restaurant = []
    list_of_restaurant_info = []

    line = rest_file.readline()
    # Until reads to the end of the file
    while line != '':
        # As long as does not read the blank line, read every line and
        # add this information to list restaurant
        if line != '\n':
            restaurant.append(line.rstrip('\n'))
        else:
            list_of_restaurant_info.append(restaurant)
            restaurant = []
        line = rest_file.readline()

    list_of_restaurant_info.append(restaurant)
    rest_file.close()

    # format the list of information lists
    #[[name, rating%, price, cuisine],...[name, rating%, price, cuisine]]
    for rest in list_of_restaurant_info:
        # remove % sign for ratings
        rest[1] = int(rest[1][:-1])
        rest[3] = rest[3].split(',')

    return list_of_restaurant_info

    
