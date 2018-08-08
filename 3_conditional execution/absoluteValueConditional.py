# acquir a number from the user and 
# print its absolute value.

value = eval(input('>> Enter a number: '))

print( '|', value, '| = ', (-value if value<0 else value), sep='' )