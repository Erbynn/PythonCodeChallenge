# The expression end=’’ is known as a keyword argument
# Without this keyword argument, the cursor moves down to the next line after printing the text.

#  terminate the line with nothing instead of the normal \n newline code
print('Please enter an integer value1: ', end='')
print(end='Please enter an integer value2: ')

# this is the default print...terminates with newline
print('Please enter an integer value3:')  #same as
print('Please enter an integer value4:', end='\n')

print() #same as
print(end='\n')