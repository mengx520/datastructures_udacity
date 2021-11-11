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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

sending_number = texts[0][0]
receiving_number = texts[0][1]
text_time = texts[0][2]

incoming_number = calls[-1][0]
answering_number = calls[-1][1]
call_time = calls[-1][2]
duration = calls[-1][3]

print(f'First record of texts, {sending_number} texts {receiving_number} at time {text_time}')
print(f'Last record of calls, {incoming_number} calls {answering_number} at time {call_time}, lasting {duration} seconds')

# Big(O) = 1 Constant time
