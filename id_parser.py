
import sys, getopt

def parse_ids(ts, s, r):
    #convert string ids to lists
    s = s.strip('[]').replace(" ", "").split(',')
    #append ids to a key
    for i in s:
        if ts in r:
            r[ts].append(i)
        else:
            r[ts] = [i]

def read_file(data):
    results = {}
    for line in data:
        line = line.rstrip().split(':')
        timestamp = int(line[0][:11])
        parse_ids(timestamp, line[1], results)
    return results

def write_file(r, arg):
    unique = ''
    nonunique = ''
    for ts in r:
        while '-' in r[ts]:
            r[ts].remove('-')
        unique +=((str(ts) + ':' + str(len(set(r[ts]))) + '\n'))
        nonunique += ((str(ts) + ':' + str(len(r[ts])) + '\n'))

    if arg in ['u', 'unique']:
        output = open('unique.txt', 'w')
        output.write(unique)
    else:
        output = open('nonunique.txt', 'w')
        output.write(nonunique)
    output.close()

def main(argv):
    #CLI options
    try:
        opts, args = getopt.getopt(argv, 'f:o:', ['file=', 'output='])
    except getopt.GetoptError as err:
        print(err)
        opts = []

    for opt, arg in opts:
        if opt in ['-f', '--file']:
            print('file =', arg)
            arg = open(arg)
            results = read_file(arg)
        elif opt in ['-o', '--output']:
            if arg in ['u', 'unique'] :
                print('output = unique.txt')
            else: print('output = nonunique.txt')
            write_file(results, arg)

if __name__ == "__main__":
    main(sys.argv[1:])
