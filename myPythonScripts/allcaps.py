# define a function to use later
def capitalize(str):
    return str.upper()

# we'll start here when run as a program, not because the name "main" is magic, but because of
# the two lines at the bottom
def main():
    import sys
    for arg in sys.argv[1:]:
        print capitalize(arg)

if __name__ == '__main__': # this line is magical and only succeeds when the script is called as a program
    main() # this line is not magical, we can put any python code here