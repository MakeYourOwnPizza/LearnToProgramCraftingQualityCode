# 1.
def is_palindrome_v3(s):
    """ (str) -> bool

   Return True if and only if s is a palindrome.
   
   >>> is_palindrome_v3('noon')
   True
   >>> is_palindrome_v3('racecar')
   True
   >>> is_palindrome_v3('dented')
   False
   """

    '''for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    
    return True'''
    # OR
    j = len(s) - 1
    for i in range(len(s) // 2):
        if s[i] != s[j - i]:
            return False

    return True
# 2.
def is_anagram(s1, s2):
    """ (str, str) -> bool
   
    Return True if and only if s1 is an anagram of s2.
  
    >>> is_anagram("silent", "listen")
    True
    >>> is_anagram("bear", "breach")
    False
    """

    # 1.Create a dictionary d1 in which each key is a letter from s1 and each value is the number of occurrences of that letter in s1.
    # 2.Create a dictionary d2 in which each key is a letter from s2 and each value is the number of occurrences of that letter in s2.
    # 3.If d1 == d2, then s1 is an anagram of s2.

# OR
    # 1.Create a list L1 of the characters in s1.
    # 2.Create a list L2 of the characters in s2.
    # 3.Sort both lists.
    # 4.If L1 == L2, s1 is an anagram of s2.
    
#3.
def count_startswith(L, ch):
    """ (list of str, str) -> int

    Precondition: the length of each item in L is >= 1, and len(ch) == 1

    Return the number of strings in L that begin with ch.
  
    >>> count_startswith(['rumba', 'salsa', 'samba'], 's')
    2
    """
    '''Select the algorithm that best describes the approach taken in the function defined above.'''
    # 1. Use a list accumulator.
    # 2. For each item in L, if the item begins with ch, add it to the accumulator.
    # 3. Return the length of the accumulator.
    ch_strings = []

    for item in L:
        if item[0] == ch:
            ch_strings.append(item)
    return len(ch_strings)
# 4.
def count_startswith(L, ch):
    """ (list of str, str) -> int

    Precondition: the length of each item in L is >= 1, and len(ch) == 1

    Return the number of strings in L that begin with ch.
  
    >>> count_startswith(['rumba', 'salsa', 'samba'], 's')
    2
    """
    '''startswith = L[:]

    for item in L:
        if not item.startswith(ch):
            startswith.remove(item)
    return len(startswith)'''

    # OR
    startswith = L[:]

    for item in L:
        if item.startswith(ch):
            startswith.remove(item)

    return len(L) - len(startswith)

# 5. Consider this code, in which s refers to a string:
def dig(s):
    '''digits = ""

    for ch in s:
        if ch.isdigit():
            digits = digits + ch
    return digits'''
    '''Select the code fragment(s) that will produce the same value for digits.'''

    '''digits = ''

    for ch in s:
        if ch in '0123456789':
            digits = digits + ch
    return digits'''
    # OR
    '''digits = ''

    for i in range(len(s)):
        if s[i].isdigit():
            digits = digits + s[i]
    return digits'''
    # OR
    indices = []
    digits = ''

    for i in range(len(s)):
        if s[i].isdigit():
            indices.append(i)

    for index in indices:
        digits = digits + s[index]
    return digits

# 6. 
def is_one_to_one(d):
     """ (dict) -> bool

     Return True if and only if no two of d's keys map to the same value.
     
     >>> is_one_to_one({'a': 1, 'b': 2, 'c': 3})
     True
     >>> is_one_to_one({'a': 1, 'b': 2, 'c': 1})
     False
     >>> is_one_to_one({})
     True
     """
    # 1.Put all the values from d into a list.
    # 2.For each value in the list, count how many times it appears in the list. If a value appears more than once in the list, return False.
    # 3.Once all the values in the list have been processed, return True because we didn't see a duplicate value.

    # OR
    # 1.Use a list accumulator to keep track of the values we've seen so far.
    # 2.For each key in d, if the value associated with that key has already been seen, return False; otherwise, append it to the list of values that we've seen so far.
    # 3.Once all the keys have been processed, return True because we didn't see a duplicate value.'''

    # OR
    # 1.Put all the values from d into a list.
    # 2.Make a copy of that list.
    # 3.Remove all the duplicate items from the second list.
    # 4.Compare the lengths of the two lists. If they are equal, return True because that means that there were no duplicate items; otherwise, return False.


def is_one_to_one(d):
    """ (dict) -> bool
 
    Return True if and only if no two of d's keys map to the same value.

    >>> is_one_to_one({'a': 1, 'b': 2, 'c': 3})
    True
    >>> is_one_to_one({'a': 1, 'b': 2, 'c': 1})
    False
    >>> is_one_to_one({})
    True
    """
    # best description:
    # 1.Use a list accumulator to keep track of the values we've seen so far.
    # 2.For each key in d, if the value associated with that key has already been seen, return False; otherwise, append it to the list of values that we've seen so far.
    # 3.Once all the keys have been processed, return True because we didn't see a duplicate value.'''
    
    seen = []  # The values that have been seen so far.
    for k in d:
        if d[k] in seen:
             return False
        else:
            seen.append(d[k])
    return True

'''8. You are conducting a survey with an ordered list of questions to which people
can answer 'Y' or 'N' ("yes" or "no"). You need to keep track of each person's
responses so that you can find out which questions they answered 'Y' to and
which questions they answered 'N' to. Which of the following data structures
could be used to represent one person's responses to the questions?'''

# dict of {str: list of int}, where each key is a response (either 'Y' or 'N')
# and each value is list of question numbers for which the person provided that response.
# OR
# dict of {int: str}, where each key is a question number and each value is
# a response to that question (either 'Y' or 'N')
# ?two list of str, where one list contains all the 'Y's and the other contains all the 'N's

'''9. A cycling time trial race is a race in which each cyclist aims to finish in
the fastest time. (All the cyclists start at different times, rather than
everyone starting at the same time.) There may be ties.
Your job is to determine which data structure to use to keep track of the names
and times of the cyclists. The data structure will initially be empty and
when a cyclist crosses the finish line, their data will be added to the
data structure.

Which of the following data structures could be used to represent all the
cyclists and their times? You may assume that the names of the cyclists
are unique.'''

# A dict of {str: float}, where each key is a cyclist and each value is a time.
# A list of [str, float] lists, where each inner list represents [cyclist, time]. The outer list is ordered from fastest time to slowest time.
# Parallel lists, where one is a list of str and the other is a list of float: the list of cyclists, and the list of their times. The lists are sorted by the order in which the cyclists cross the finish line (which is not the same as how long they took).

''' 10.This question is a followup to the previous question about cycling
time trials.
Now that the race is over, you need to determine the three fastest cyclists.
(Assume there are no ties among the top three.)
Which data structure will make it easiest to look up the three fastest cyclists? You may assume that the names of the cyclists are unique.'''
# A list of [str, float] lists, where each inner list represents [cyclist, time]. The outer list is ordered from fastest time to slowest time.

'''Jan
Toronto: 3.5,0,1.8,0,...
Montreal: 1.5,0,0,0,...
Vancouver: 0,8.6,23.6,19.2,...

Feb
Toronto: 0,0,1.5,1.2,...
Montreal: 0.4,0,0.3,0.4,...
Vancouver: 14,0,0.2,0.2,...

...

Dec
Toronto: 1.3,13.7,0.6,3.8,...
Montreal: 0,7.7,0,6.9,
Vancouver: 15.2,21.4,11.4,14.6,...'''

'''11. This problem involves a weather dictionary in which the keys are month names
and the values are dictionaries containing information about precipitation in
cities for that month.

In each of the nested dictionaries, the keys are city names and the values
are lists of millimetres of precipitation for each day that month, in order.
We'll refer to these nested dictionaries as "city to precipitation" dictionaries.

Select the algorithm(s) that can be used to determine the city that had
the maximum total precipitation in February. (You can break ties any way
you like, or you can assume that there are no ties. Either is fine.)'''
'''
Build the weather dictionary.
Look up key 'Feb' in the weather dictionary to get the "city to precipitation" dictionary for February.
Create a list containing the sum of the precipitation amounts from each of the city precipitation lists for February. Also create a parallel list containing the city names.
Sort the list containing the sum of the precipitation amounts so that the largest value is last. The answer is the city in the parallel list at the last position.'''
# 1.Build the weather dictionary.
# 2.Look up key 'Feb' in the weather dictionary to get the "city to precipitation" dictionary for February.
# 3.Iterate through the cities in that dictionary, calculating the sum of the precipitation amounts for that city. Keep track of the city that has the most precipitation so far.
# 4.Once the iteration is complete, whichever city had the most precipitation is the answer.

# ?Build the weather dictionary.
Look up key 'Feb' in the weather dictionary to get the "city to precipitation" dictionary for February.
Create a dictionary where the keys are cities and the values are the sum of the precipitation amounts for that city for February.
Find the maximum value in that dictionary of city maximums. The answer is the key associated with that maximum.

# ?Build the weather dictionary.
Look up key 'Feb' in the weather dictionary to get the "city to precipitation" dictionary for February.
Create a list containing the sum of the precipitation amounts from each of the city precipitation lists for February. Also create a parallel list containing the city names.
Sort the list containing the sum of the precipitation amounts so that the largest value is last. The answer is the city in the parallel list at the last position.

'''12. This question also involves a weather file and a weather dictionary.
Please see the previous question for details.
Select the algorithm(s) that can be used to make a list of the days in which
no city had precipitation — we'll call this the "zero-precipitation list".
Each day should be a tuple of (month name, day number).
For example, if all cities in the "city to precipitation" dictionary for
February had no precipitation on the very first day, then ('Feb', 1) would
be in the resulting list.

Note: in the weather dictionary, the list of precipitation amounts starts at
index 0; to get the corresponding day number for an index, just add 1.

Hint: You will probably find this question easier to do if you take notes
about the problem on a piece of paper, including drawing a small example
weather dictionary.'''

# 1.Build the weather dictionary.
# 2.Create a "zero-precipitation" list containing all days of the year from ('Jan', 1) through ('Dec', 31).
# 3.Iterate over the months to get each "city to precipitation" dictionary. For each of these dictionaries:
# a) For each city in the current "city to precipitation" dictionary,
# iterate over the precipitation amounts. Because we know the current month
# and day number, we will remove from the "zero-precipitation" list any day
# that has a non-zero precipitation amount.
# 4. One this process is complete, the "zero-precipitation" list contains only the (month, day number) for days in which no city had precipitation.

# 1.Build the weather dictionary.
# 2.Create an empty "zero-precipitation" list to accumulate the answer.
# 3.Iterate over the months to get each "city to precipitation" dictionary. For each of these dictionaries:
# a) Build a dictionary where each key is a city from the current "city to precipitation" dictionary, and each value is a list of the day numbers on which the city had no precipitation.
# b) Iterate over the values in that dictionary to build a list containing the day numbers that appear in all the lists of day numbers.
# c) Iterate over the list of day numbers, appending tuples containing the current month name and the day number to the "zero-precipitation" list.
