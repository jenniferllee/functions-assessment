"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(25, "CA")
    27.0

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0)
    150

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

def check_hometown(town_name):
    """Takes a town name as a string and returns 'True' if
    it is your hometown and 'False' otherwise

    For example:

    >>> check_hometown("Palo Alto")
    True

    >>> check_hometown("San Francisco")
    False

    """

    my_hometown = "Palo Alto"

    if town_name == my_hometown:
        return True
    else:
        return False

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.


def full_name(first_name, last_name):
    """ Takes a first and last name as arguments and returns the concatenation
    of the two names in one string.

    For example:

    >>> full_name('Jennifer', 'Lee')
    'Jennifer Lee'

    """

    return '%s %s' % (first_name, last_name)


#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.


def greeting(home_town, first_name, last_name):
    """ Takes a home town, first name, and last name as arguments and prints
    two different greetings depending on whether home town is the same.

    For example:

    >>> greeting('Palo Alto', 'Jennifer', 'Lee')
    Hi, Jennifer Lee, we're from the same place!

    >>> greeting('San Francisco', 'Jennifer', 'Lee')
    Hi Jennifer Lee, where are you from?

    """

    if check_hometown(home_town) is True:
        print "Hi, %s, we're from the same place!" % (full_name(first_name, last_name))
    else:
        print "Hi %s, where are you from?" % (full_name(first_name, last_name))


###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry"""

    if fruit == "strawberry" or fruit == "cherry" or fruit == "blackberry":
        return True
    else:
        return False


# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""

    if is_berry(fruit) is True:
        return 0
    else:
        return 5


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""

    # THIS DOES NOT WORK (methods that mutate sequences return None):
    # new_list = lst.append(num)
    # return new_list

    # THIS WORKS:
    new_list = lst + [num]
    return new_list


# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.

def calculate_price(base_price, state, tax=0.05):

    if state == "CA":
        tax = base_price * tax
        cost_with_tax = base_price + tax
        recycling_fee = base_price * 0.03
        total_cost = cost_with_tax + recycling_fee
    elif state == "PA":
        tax = base_price * tax
        cost_with_tax = base_price + tax
        total_cost = cost_with_tax + 2
    elif state == "MA":
        tax = base_price * tax
        cost_with_tax = base_price + tax
        if base_price < 100:
            total_cost = cost_with_tax + 1
        else:
            total_cost = cost_with_tax + 3
    else:
        tax = base_price * tax
        total_cost = base_price + tax

    return total_cost


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.

def create_list(lst, *arg):
    """ Takes in a list and any number of additional arguments, appends
    them to the list, and returns the entire list.

    >>> create_list([1, 2, 3], 4, 5, 6)
    [1, 2, 3, 4, 5, 6]

    """

    # Convert tuple to a list (arg returns additional argument(s) in a tuple).
    items_to_append = list(arg)

    # Concatenate additional arguments to original list.
    new_list = lst + items_to_append

    return new_list


# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


def outer(word):
    """ Takes in a word, calls an inner function that multiplies word by 3,
    returns a tuple with the original function argument and the result of
    the inner function.

    >>> outer("Balloonicorn")
    ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

    """

    def inner(word):
        return word * 3
    return word, inner(word)

###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
