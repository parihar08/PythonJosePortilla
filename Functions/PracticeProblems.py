def func(a,b):
    if a%2 ==0 and b%2 ==0:
        #both numbers are even
        if b>a:
            result =a
        else:
            result =b
    else:
        #one or both numbers are odd
        if a>b:
            result =a
        else:
            result=b
    return result

print(func(2,6))
print(func(6,7))


def func1(a,b):
    if a%2 ==0 and b%2 ==0:
        #both numbers are even
        result=min(a,b)
    else:
        #one or both numbers are odd
        result = max(a, b)
    return result

print(func(2,6))
print(func(6,7))


def func2(a,b):
    if a%2 ==0 and b%2 ==0:
        #both numbers are even
        return min(a,b)
    else:
        #one or both numbers are odd
        return max(a, b)

print(func(12,8))
print(func(19,7))

print('******************************')

#Write a function that takes 2 word string and returns True if both start with same letter

def animal_crackers(text):
    list=text.split()
    print(list)
    first =list[0]
    second =list[1]
    return first[0]==second[0]

print(animal_crackers('Daily Dhoni'))
print(animal_crackers('Sandeep Parihar'))

def animal_crackers1(text):
    list=text.lower().split()
    print(list)
    return list[0][0]==list[1][0]

print(animal_crackers1('Toronto Calgary'))
print(animal_crackers1('Vancouver victoria'))

#Given 2 integers, return true if sum of integers is 20 or if one of them is 20. else False

def makes_twenty(a,b):
    if a+b==20:
        return True
    elif a==20:
        return True
    elif b==20:
        return True
    else:
        return False

print(makes_twenty(10,10))
print(makes_twenty(20,0))
print(makes_twenty(18,6))

def makes_twenty1(a,b):
    return (a+b)==20 or a==20 or b==20

print(makes_twenty1(10,10))
print(makes_twenty1(20,0))
print(makes_twenty1(18,6))