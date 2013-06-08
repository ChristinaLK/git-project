import sys

def readLinesFromStdin():
    return sys.stdin.readlines()

def readDataFromStdin():
    return sys.stdin.read()

def readLinesFromFile(filename):
    return open(filename).readlines()

def readDataFromFile(filename):
    return open(filename).read()

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '-l':
            # Use read lines mode
            if len(sys.argv) > 2:
                # We have filename(s)
                for filename in sys.argv[2:]:
                    lines = readLinesFromFile(filename)
                    print 'read', len(lines), 'lines from', filename
            else:
                lines = readLinesFromStdin()
                print 'read', len(lines), 'lines from stdin'
        else:
            for filename in sys.argv[1:]:
                data = readDataFromFile(filename)
                print 'read', len(data), 'characters from', filename
    else:
        data = readDataFromStdin()
        print 'read', len(data), 'characters from stdin'

if __name__ == '__main__':
    main()