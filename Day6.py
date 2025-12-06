# Examples of Dictionary

# Original dictionary operations
profile = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "occupation": "Software Developer"
}
print("Original profile:")
print(profile)

profile["age"] = 34 
print("\nAfter updating age:")
print(profile)

profile["skill"] = "AI Developer"
print("\nAfter adding skill:")
print(profile)

profile["name"] = "Jane Doe"
print("\nAfter updating name:")
print(profile)

del profile["city"]
print("\nAfter deleting city:")
print(profile)

# Creating multiple dictionaries and merging them
print("\n" + "="*50)
print("Merging Multiple Dictionaries")
print("="*50)

dict1 = {
    "name": "Alice",
    "age": 25,
    "city": "San Francisco"
}

dict2 = {
    "occupation": "Data Scientist",
    "skill": "Python",
    "experience": 3
}

dict3 = {
    "company": "Tech Corp",
    "salary": 120000,
    "department": "AI"
}

print("\nDict1:", dict1)
print("Dict2:", dict2)
print("Dict3:", dict3)

# Method 1: Using update() method
merged_dict1 = dict1.copy()
merged_dict1.update(dict2)
merged_dict1.update(dict3)
print("\nMerged using update():")
print(merged_dict1)

# Method 2: Using unpacking (Python 3.9+)
merged_dict2 = {**dict1, **dict2, **dict3}
print("\nMerged using unpacking (**):")
print(merged_dict2)

# Method 3: Using dict() constructor with unpacking
merged_dict3 = dict(**dict1, **dict2, **dict3)
print("\nMerged using dict() constructor:")
print(merged_dict3)

# Method 4: Merging with overlapping keys
dict_overlap1 = {"name": "Bob", "age": 30, "city": "Boston"}
dict_overlap2 = {"name": "Charlie", "occupation": "Engineer", "age": 28}

merged_overlap = {**dict_overlap1, **dict_overlap2}
print("\nMerged dictionaries with overlapping keys:")
print(f"dict_overlap1: {dict_overlap1}")
print(f"dict_overlap2: {dict_overlap2}")
print(f"Merged (dict_overlap2 overwrites): {merged_overlap}")