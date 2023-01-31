

# This program converts kilometers to miles.

# Global constant for conversion
CONVERSION_FACTOR = 0.6214

# The main function gets a distance in kilometers and calls
# the show_miles function to convert it.
def main():

    # Get distance in kilometers.
    kilometers = float(input('Enter the distance in kilometers: '))

    #Display the distance converted to miles.
    show_miles(kilometers)

# The show_miles function converts the parameter km from
#kilometers to miles and displays the result.
def show_miles(km):
    #calculate miles.
    miles = km * CONVERSION_FACTOR

    #Display the miles.
    print (km, 'kilometers equals', format(miles, '.2f), 'miles.')

#Call the main function.
main()