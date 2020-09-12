from ModulesAndPackages import one

print('Top Level in two.py')

one.my_func()

if __name__ == "__main__":
    #Run the script
    print('two.py is being run directly')
else:
    print('two.py has been imported')