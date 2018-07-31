seconds = eval(input('>>> Enter the number of seconds: '))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = (seconds % 3600) % 60 # seconds = minutes % 60,,,gives wrong answer

# same as like 23
# but just put leading zero in front of single-digit values as on digi-clock
# 5 = 05
min_tens = minutes // 10
min_ones = minutes % 10

sec_tens = seconds // 10
sec_ones = seconds % 10

print(hours, ':', min_tens, min_ones, ':', sec_tens, sec_ones, sep='')