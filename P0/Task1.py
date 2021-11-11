"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

'''
# Dictonary way

number_dict = {}

for text in texts:
    number_1 = text[0]
    number_2 = text[1]
    number_dict[number_1] = None
    number_dict[number_2] = None

for call in calls:
    number_1 = call[0]
    number_2 = call[1]
    number_dict[number_1] = None
    number_dict[number_2] = None 
'''

'''
using python set()
'''
number_set = set()

for text in texts:
    number_set.update([text[0],text[1]])


for call in calls:
    number_set.update([call[0],call[1]])


print(f'There are {len(number_set)} different telephone numbers in the records.')

# Big(O) = O(N) linear time

    

