# nested loops

listA = list(range(6))

listB = list(range(6))

product1 = [(a, b) for a in listA for b in listB]

product2 = [(a, b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0]

'''
print(product1)
print(product2)
'''

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

connections_with_rep = [(a, b) for a in ports for b in ports]
connections_without_rep = [(a, b) for a in ports for b in ports if a != b]
routes = [(a, b) for a in ports for b in ports if a > b]

print(connections_with_rep)
print(len(connections_with_rep))


print(connections_without_rep)
print(len(connections_without_rep))

print(routes)
print(len(routes))

