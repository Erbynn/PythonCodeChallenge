degF, degC = 0, 0
degF = eval(input('>> Enter the temperature in degrees F: '))
degC = 5/9*(degF - 32)
degC_round = round(degC, 2)
print(degF, 'degrees Farienheit =', degC_round, 'degrees Celcius')
