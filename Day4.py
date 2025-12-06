# for i in range(1, 6):
#     print("Day", i)

# list_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# for day in list_of_days:
#     print("Day of the week:", day)    


#Build a dictionary by adding key–value pairs in a loop

data = {}
for i in range(5):
    data[i] = i * 10
print(data)

#Create a list of dictionaries inside a loop

items = []
for i in range(3):
    d = {'id': i, 'value': i * 5}
    items.append(d)
print(items)

#Two lists → dictionary (using for loop)

keys = ['name', 'age', 'city']
values = ['Sathish', 34, 'New York']

keys.append('country')
values.append('USA')

result = {}

for i in range(len(keys)):
    result[keys[i]] = values[i]
print(result)   

