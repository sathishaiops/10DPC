#Examples of Lists in Python

task = ['eat', 'code', 'sleep']
print(task)  

task.append('repeat')          # Output the entire list
print(task)                   # Output the entire list after appending 'repeat'

task.remove('sleep')         # Remove 'sleep' from the list
print(task)                   # Output the entire list after removing 'sleep'

task.insert(1, 'exercise')   # Insert 'exercise' at index 1
print(task)                   # Output the entire list after insertion  

task.sort()                   # Sort the list alphabetically
print(task)                   # Output the sorted list

task.reverse()                # Reverse the list
print(task)                   # Output the reversed list    

task.pop()                    # Remove and return the last item
print(task)                   # Output the list after popping the last item 

task1 = task.copy()                   # Create a copy of the list
print(task1)                   # Output the copied list

task.clear()                  # Clear all items from the list
print(task)                   # Output the cleared list (should be empty)

task1.extend(['work', 'play'])  # Extend the list with new items
print(task1)                  # Output the extended list

count_code = task1.count('code')          # Count occurrences of 'code' in the list
print(task1)                  # Output the list to show the count operation (though count does not
print(count_code)

pos = task1.index('work')           # Find the index of 'work' in the list
print(task1)                  # Output the list to show the index operation (though index does not
print(task1.index('work'))