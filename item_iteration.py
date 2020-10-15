datum = ['apple',7,19,'banana']
print(f'datum ->  {datum} ')

datum_2 = []
for data in datum:
    datum_2.append(data*2)

print(f'datum_2 ->  {datum_2} ')    

dict_1 = dict()
for data,element in enumerate(datum):
    dict_1[data] = element
print(f'dict_1 -> {dict_1} ')  