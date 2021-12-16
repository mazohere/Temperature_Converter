import sys

# assigning colours for later
white = "\033[39m"
red = "\033[31m"
blue = "\033[34m"
colour_val = "\033[39m"


# function for after the conversion is finished so the program doesn't just end
def reset_function():
    print('would you like to convert anything else?\nY/N')
    reset = input(' ')

    if reset == 'Y' or reset == 'y':
        temperature_converter()
                
    elif reset == 'N' or reset == 'n':
        exit()

    else:
        print('invalid response, please try again')
        reset_function()

# x <= 10: light blue, 10 < x <= 20: blue, 20 > x >= 30: red, x > 30: black
def dependant_colour_variable_set(colour, initial_val, end_val, convert):

    #assigning the colour value for the final print screen
    if colour <= 10:
        colour_var = "\033[94m" # light_blue
    elif 10 < colour <= 25:
        colour_var = "\033[34m" # blue
    elif 25 < colour <= 35:
        colour_var = "\033[31m" # red
    elif colour > 35:
        colour_var = "\033[30m" # black

    # final print screen with colours based on the temperature and the converted temperature
    if convert == 1:
        print(colour_var, initial_val, white, 'converted to F° is:', colour_var, end_val, white)
    elif convert == 2:
        print(colour_var, initial_val, white, 'converted to C° is:', colour_var, end_val, white)

def temperature_converter():
    # inital print screen with colours
    print('press ' + blue + '1 ' + white + 'to convert from ' + red + 'C° ' + white + 'to ' + red + 'F° ' + white)
    print('press ' + blue + '2 ' + white + 'to convert from ' + red + 'F° ' + white + 'to ' + red + 'C° ' + white)

    # error function executing based on where it is called
    def error(where):

        print('invalid response, please try again')

        if where == 1:
            temperature_converter()
        elif where == 2:
            correct()
        


    # user input recording and conversion
    choice = input(' ')

    # when the user input is correct
    def correct():
        # both the C° and F° routes ask the user for their temperatures, convert the temperatures using their respective 
        # formulas and set a colour value based on the temperature for a visual/graphical representation of the temperature 
        # i.e light blue to red to black based on how hot it is

        # C° route
        if choice == 1:
            initial_value = input('enter initial temperature (C°): ')
            if initial_value.isnumeric() == True:
                initial_value = int(initial_value)
                end_value = (initial_value * 9/5) + 32

                colour_value = initial_value

                dependant_colour_variable_set(colour_value, initial_value, end_value, choice)
                
                reset_function()

            else:
                error(2)

        # F° route
        elif choice == 2:
            initial_value = input('enter initial temperature (F°): ')
            if initial_value.isnumeric() == True:
                initial_value = int(initial_value)
                end_value = (initial_value - 32) * 5/9

                colour_value = initial_value

                dependant_colour_variable_set(colour_value, initial_value, end_value, choice)

                reset_function()

            else:
                error(2)

    # testing if the user input is correct, converting it to an int if it is and calling the error function if it's not
    if choice == '1' or choice == '2':
        choice = int(choice)
        correct()
    else:
        error(1)

temperature_converter()