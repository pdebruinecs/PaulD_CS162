#Week 3 CS 162
#Paul Debruine
#Queue in Python HW

from queue import *

#decalring three lists, which will act as queues, pq(priority queue), sq(standard queue), and eq(economy queue)
pq = []
sq = []
eq = []
output = []

#starting queue
inputlist = [
    "S Mary", "P Dee", "P Dee", "E Eileen", "E Mike", "E Joe", "P Dee",
    "E Vicky", "E George", "P Dee", "P Joe", "E Sally", "P Joe", "S Pete",
    "P Dee", "S Bill", "S Chase", "E Price", "P Dee", "E Sue"
]

#iterates through the starting queue, appends values to their respective queues. Parses strings
#to determine what the first letter is to determine which list they should be apppended to
for item in inputlist:
    if (item[0] == "P"):
        pq.append(item)
    elif (item[0] == "S"):
        sq.append(item)
    else:
        eq.append(item)

#next three lines check that the items have been appended to the correct queues
print(pq)
print(sq)
print(eq)

def WFQ(q1,q2,q3):
    '''This function does the following: pops three names from the front of the list pq,
    pops two items from the list sq, pops one item at eq. Items are popped at index (0), which is the
    front of the list. The individual loops that pop items off the lists are nested within a while loop
    that loops until there are 0 items in each queue. The nested for loops that pop the desired
    amount of items from (0) only run if there are items in the individuals queues, if there are
    no longer any items in the queues, the nested loop breaks.'''
    while (len(pq) + len(sq) + len(eq) != 0):    
        for i in range (0,3):
            if (len(pq) > 0):
                print(pq.pop(0))
            else:
                break
        for item in range (0,2):
            if (len(sq) > 0):
                print(sq.pop(0))
            else:
                break
        for item in range (0,1):
            if (len(eq) > 0):
                print(eq.pop(0))       
WFQ(pq,sq,eq)