# # get the number of seconds
# seconds = eval(input('>> Enter the number of seconds: '))
# # conpute the number of hours in the seconds using truncation
# hours = seconds // 3600
# # compute and store the remaining seconds
# seconds = seconds % 3600
# # compute the number of minutes left in the remaining seconds
# minutes = seconds // 60
# # conpute the number of seconds left
# seconds = seconds % 60

# print(hours,'hr', minutes, 'min', seconds, 'sec')

# # note...'/' would have given float numbers, ie decimals


# #can also be done this way
# sec = eval(input('>> Enter the number of seconds : '))
# hr = sec // 3600
# mins = (sec % 3600) // 60
# sec = (sec % 3600) % 60
# print(sec,'secs', '=', hr, 'hr,',mins, 'min,',sec,'secs', sep=' ')


# uses the keyword arguments
sec2 = eval(input('>> Enter the number of seconds : '))
hr2 = sec2 // 3600
print(sec2,'secs =',hr2,'hr', sep=' ', end=' ') # terminates(stops) with one space
mins2 = (sec2 % 3600) // 60
print(mins2,'mins', sep=' ', end=' ')
sec2 = (sec2 % 3600) % 60
print(sec2,'secs', sep=' ', end='')
