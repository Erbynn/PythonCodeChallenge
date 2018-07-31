#  This allows users to provide input in a variety of ﬂexible ways; for example, 


# users can enter multiple entries separated by commas in one line, and 
# the eval function evaluates it as a Python tuple

num1, num2 = eval(input('>> Enter two numbers separated by comma(ie number1,  number2): '))
print(num1,' + ',num2,' = ', num1 + num2)



# The eval function can be used to convert a string representing a numeric expression into its evaluated numeric value of datatype
# works just like the IDLE interpreter
print(eval(input('>> Enter your conputation as Strings: ')))