"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
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
durations = {}
maxCallerNumber = ""
maxDuration = 0
for call in calls:
    if call[0] in durations.keys():
        durations[call[0]] += call[3]
    else:
        durations[call[0]] = call[3]

    if call[1] in durations.keys():
        durations[call[1]] += call[3]
    else:
        durations[call[1]] = call[3]

    # Determine the max duration in the same iteration
    if durations[call[0]] > maxDuration:
        maxDuration = durations[call[0]]
        maxCallerNumber = call[0]
    elif durations[call[1]] > maxDuration:
        maxDuration = durations[call[1]]
        maxCallerNumber = call[1]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(maxCallerNumber, maxDuration))
