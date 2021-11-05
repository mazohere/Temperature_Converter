import sys

# assigning colours for later
white = "\033[39m"
red = "\033[31m"
blue = "\033[34m"


# function for after the conversion is finished so the program doesn't just end
def reset_function():
    print('would you like to convert anything else?\nY/N')
    reset = input(' ')

    if reset == 'Y' or reset == 'y':
        temperature_converter()
                
    elif reset == 'N' or reset == 'n':
        exit()

    else:
        print('invalid response')
        reset_function()

# x <= 10: light blue, 10 < x <= 20: blue, 20 > x >= 30: red, x > 30: black
def dependant_colour_variable_set(colour):
    if colour < 10:
        dependant_colour_variable = "\033[94m" # light_blue

    elif 10 < colour <= 20:
        dependant_colour_variable = "\033[34m" # blue

    elif 20 > colour >= 30:
        dependant_colour_variable = "\033[31m" # red
    
    elif colour > 30:
        dependant_colour_variable = "\033[30m" # black


def temperature_converter():
    # inital print screen (should add colours later)
    print('press ' + blue + '1 ' + white + 'to convert from ' + red + 'C° ' + white + 'to ' + red + 'F° ' + white)
    print('press ' + blue + '2 ' + white + 'to convert from ' + red + 'F° ' + white + 'to ' + red + 'C° ' + white)

    # error plan
    def error():
        print('incorrect')
        temperature_converter()

    # user input recording and conversion
    choice = input(' ')

    # when the user input is correct
    def correct():
        # C° route
        if choice == 1:
            initial_value = input('enter initial temperature (C°): ')
            if initial_value.isnumeric() == True:
                initial_value = int(initial_value)
                print(initial_value)
                print(type(initial_value))

                dependant_colour_variable = "\033[39m"

                dependant_colour_variable_set(initial_value)

                end_value = (initial_value * 9/5) + 32
                print(initial_value, 'converted to F° is:', end_value)
                
                reset_function()

            else:
                error()

        # F° route
        elif choice == 2:
            initial_value = input('enter initial temperature (F°): ')
            if initial_value.isnumeric() == True:
                initial_value = int(initial_value)
                print(initial_value)
                print(type(initial_value))

                end_value = (initial_value - 32) * 5/9
                print(initial_value, 'converted to C° is:', end_value)

                reset_function()

            else:
                error()

    # testing if the user input is correct
    if choice == '1' or choice == '2':
        choice = int(choice)
        print(choice)
        print(type(choice))
        correct()
    else:
        error()

temperature_converter()