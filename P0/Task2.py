"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import operator

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

number_dict = {}

for call in calls:
    send_number = call[0]
    receive_number = call[1]

    if send_number not in number_dict:
        number_dict[send_number] = 0
    if receive_number not in number_dict:
        number_dict[receive_number] = 0

    number_dict[send_number] += int(call[3])
    number_dict[receive_number] += int(call[3])
    
max_time = max(number_dict.items(), key = operator.itemgetter(1))

print(f'{max_time[0]} spent the longest time, {max_time[1]} seconds, on the phone during September 2016.')

# Big(O) = O(n) Linear time