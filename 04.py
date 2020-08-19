# generator

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

routes = ((a, b) for a in ports for b in ports if a > b)

print(next(routes))
print(next(routes))

print('-'*10)
'''Zauważ, że pętla while nie pobierze dwóch pierwszych wartości - pobrały je polecenia wyżej'''

while True:

    try:

        print(next(routes))

    except StopIteration:
        print('All values have been generated')
        break

print('-'*10)
