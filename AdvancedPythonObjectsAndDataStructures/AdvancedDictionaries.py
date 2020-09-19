d = {'k1':1,'k2':2}

print('*********DICTIONARY COMPREHENSIONS************','\n')

print({x:x**2 for x in range(10)})
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#To assign keys not based on values. We can use Zip
print('*********************************','\n')

print({k:v**2 for k,v in zip(['a','b'],range(2))})      #{'a': 0, 'b': 1}

print('*********ITERATIONS OF KEYS VALUES AND ITEMS************','\n')

print(d.items())
print(d.keys())
print(d.values())

print('*********************************','\n')

#ITEMS
for k in d.items():
    print(k)

#KEYS
print('*********************************','\n')
for k in d.keys():
    print(k)

#VALUES
print('*********************************','\n')
for k in d.values():
    print(k)
