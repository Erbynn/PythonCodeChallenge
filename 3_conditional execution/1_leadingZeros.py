num = eval(input('>> Please enter an integer in the range 0...9999: '))
if num < 0:
    num = 0
if num > 9999:
    num = 9999

print(end='[')

digit = num//1000           # Determine the THOUSANDTHS-place digit
print(digit, end="")
num %= 1000                 # Discard the THOUSANDTHS-place digit

digit = num//100            # Determine the HUNDREDTHS-place digit
print(digit, end="")        # Print the HUNDREDTHS-place digit
num %= 100                  # Discard the HUNDREDS-place digit

digit = num//10              # Determine the tens-place digit 
print(digit, end="")         # Print the tens-place digit
num %= 10                    # Discard the tens-place digit

print(num, end="")          # Floor Division and Modulo op. on 1 still remains 1 

print("]")