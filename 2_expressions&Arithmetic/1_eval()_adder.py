# If the user types the sequence 431 and then presses the enter key, value1 is assigned the integer 431. If instead the user enters 23 + 3, the variable gets the value 26.
value1 = eval(input('Please enter a number: '))
value2 = eval(input('Please enter another number: '))
sum = value1 + value2print(value1, '+', value2, '=', sum)