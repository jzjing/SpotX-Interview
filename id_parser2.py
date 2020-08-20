
from sys import argv

def count_ids(ts, s, r):
    #convert string ids to lists
    s = s.strip('[]').replace(" ", "").split(',')
    #append ids to a key
    for i in s:
        if ts in r:
            r[ts].append(i)
        else:
             r[ts] = [i]

def readfile(data):
    results = {}
    with open(data) as f:
        for line in f:
            line = line.rstrip().split(':')
            timestamp = int(line[0][:11])
            count_ids(timestamp, line[1], results)
    return results

def writefile(r):
    u = open('unique.txt', 'w')
    n = open('nonunique.txt', 'w')
    for ts in r:
        while '-' in r[ts]:
            r[ts].remove('-')
        u.write(str(ts) + ':' + str(len(set(r[ts]))) + '\n')
        n.write(str(ts) + ':' + str(len(r[ts])) + '\n')
    u.close()
    n.close()

def main():
    results = readfile(argv[1])
    writefile(results)

if __name__ == "__main__":
    main()
