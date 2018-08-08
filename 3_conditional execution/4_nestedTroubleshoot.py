print("Help! My computer doesn't work!")
print("Does the computer make any sounds (fans, etc.)")
choice = input("or show any lights? (y/n): ") 

if choice == 'n':
    choice = input('Is it pluged in? (y/n): ')
    
    if choice == 'n':
        print('Plug it in. If the problem persists,')
        print('Please run the program again.')


    else:
        choice = input('Is the switch in the \'on\' position (y/n): ')

        if choice == 'n':
            print('Turn it on. If the problem persists,')
            print('please run this program again')
        else:
            choice = input('Is the switch on \'on\' position (y/n): ')
            if choice == 'n':
                choice = input('Is the outlet OK? (y/n): ')

                if choice == 'n':
                    print('Check the outlet\'s circuit breaker or fuse. Move to a new outlet, if necessary.')
                    print('If the problem persists,please run this prgram again') 
                else:
                    print('Please consult a service technician.')
            else:
                print('Check the fuse. replace is necessary.')
                print('please run this program again, if problem persist.')
else:
    print('Consult a service technicioan')