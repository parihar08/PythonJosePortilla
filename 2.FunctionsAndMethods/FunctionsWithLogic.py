def even_number(num):
    if num % 2 ==0:
        print("Even number")
    else:
        print("Odd number")


even_number(3)

def even_check(num1):
    return  num1%2==0

even_check(3)


def check_even_list(num_list):
    for num in num_list:
        if num % 2==0:
            print('Found even number')
        else:
            pass
    print('Found odd number')

check_even_list([1,2,3,4,5])


def check_even_list1(num_list):
    for num in num_list:
        if num % 2==0:
            return True
        else:
            pass

    return False

print(check_even_list1([1,2,3,4,5]))

#Return all the even numbers in the list

def return_even(list):
    #placeholder variable
    even_numbers =[]
    for num in list:
        if num%2==0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers

print(return_even([1,8,10,4,5]))
