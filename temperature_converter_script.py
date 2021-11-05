import sys

print('press 1 to convert from C° to F°')
print('press 2 to convert from F° to C°')

def failure():
    print('incorrect')
    exit()


choice = input(' ')

print(choice)

# C° route
if choice == 1: 
    initial_value = input('enter initial temperature: ')
    print(initial_value)

#F° route
if choice == 2:
    initial_value = input('enter initial temperature: ')
    print(initial_value)
