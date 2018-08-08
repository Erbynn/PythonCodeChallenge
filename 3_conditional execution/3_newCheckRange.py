value = eval(input("Please enter an integer value in the range 0...10: "))
if value >= 0 and value <= 10:
    print('In range')
print('Done')
 

# ... cam be more compactly as
value = eval(input("Please enter an integer value in the range 0...10: "))
if 0 <= value <= 10:
    print('In range')
print('Done')
 