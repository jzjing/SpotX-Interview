
fn = input('Enter file:')
if len(fn) < 1: fn = 'interview.log'

#count = 0
c = {}

def count_ids(timestamp, string):
    #convert string ids to lists
    string = string.strip('[]').replace(" ", "").split(',')
    #append ids to a key
    for i in string:
        if timestamp in c:
            c[timestamp].append(i)
        else: c[timestamp] = [i]


with open(fn) as f:
    for line in f:
        line = line.rstrip().split(':')
        timestamp = int(line[0][:11])
        count_ids(timestamp, line[1])
        #count += 1
        #if count == 2000: break

inp = input('unique or total? ')

for line in c:
    while '-' in c[line]:
        c[line].remove('-')
    #print(line,':', c[line])
    if inp == 'unique':
        print(line,':', len(set(c[line])))
    else:
        print(line,':', len(c[line]))
