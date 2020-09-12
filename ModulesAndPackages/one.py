def my_func():
    print('myfunc() in one.py')

print('Top Level in one.py')

import sys

print(sys.path)


#Built in variable in Python - this variable gets assigned a string depending on how we run our
#script
if __name__ == "__main__":
    print('one.py is being run directly')
    my_func()
else:
    print('one.py has been imported')