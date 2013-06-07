import subprocess

def ls():
    output = subprocess.check_output(['ls']) # output is a string of everything returned
    directory = output.split('\n') # split the string on newlines
    directory.pop() # throw away the last, empty line
    for filename in directory:
        print filename

def lsl():
    output = subprocess.check_output(['ls', '-l', '-h'])
    directory = output.split('\n') # split the string on newlines
    directory.pop() # throw away the last, empty line
    for filename in directory:
        print filename

def main():
    print 'ls:'
    ls()
    print
    print 'ls -l -h:'
    lsl()
    print

if __name__ == '__main__':
    main()


