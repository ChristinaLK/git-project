def appendToFiles(filenames):
    for filename in filenames:
        out = open(filename, 'a') # 'a' opens in "append" mode
        print >> out, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        out.close()

def overwriteFiles(filenames):
    for filename in filenames:
        out = open(filename, 'w') # 'w' opens in "write" mode, which erases existing content of the file
        print >> out, '1234567890'
        out.close()

def main():
    appendToFiles(['data1.txt', 'data2.txt'])
    overwriteFiles(['data3.txt', 'data4.txt'])

if __name__ == '__main__':
    main()