import copy

# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.

persons = [
    {'name': 'bharat',
     'age': 18,
     'hobbies': ['tv', 'music', 'cricket']},
    {'name': 'rohit',
     'age': 22,
     'hobbies': ['football', 'dance']},
    {'name': 'charan',
     'age': 32,
     'hobbies': ['tv']},
    {'name': 'ajay',
     'age': 5,
     'hobbies': ['ludo', 'youtube', 'pubg', 'coding']},
    {'name': 'sidhart',
     'age': 45,
     'hobbies': ['pubg', 'reading']}
]


# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).

names_list = [dict['name'] for dict in persons]
print(names_list)


# 3) Use a list comprehension to check whether all persons are older than 20.

# Method 1

older_persons = [True for dict in persons if dict['age'] > 20]

if len(older_persons) == 0:
    print('All are below 20 years of age')
elif len(older_persons) == len(persons):
    print('All are above 20 years of age')
else:
    print('Not all are above 20 years of age')

# Method 2

older_persons = []

for dict in persons:
    if dict['age'] > 20:
        older_persons.append(True)
    else:
        older_persons.append(False)

print(older_persons)

if all(older_persons):
    print('All are above 20 years of age')
else:
    print('Not all are above 20 years of age')


# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).

copy_persons = copy.deepcopy(persons)
copy_persons[0]['name'] = 'ram'
print('Actual List' + ' ' + str(persons))
print('Copy List' + ' ' + str(copy_persons))


# 5) Unpack the persons of the original list into different variables and output these variables.

a,b,c,d,e = persons

print (a)
print (b)
print (c)
print (d)
print (e)
