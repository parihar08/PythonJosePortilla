#SPY GAME: Write a function that takes a list of integers and returns TRUE if it contains
#007 in that order

def spy_game(nums):
    for i in range(0,len(nums)-1):
        if nums[i] ==0 and nums[i+1] ==0 and nums[i+2] ==7:
            return True

    return False

print(spy_game([1,3,0,7]))
print(spy_game([1,1,0,1,0,7]))
print(spy_game([4,5,6,0,0,7]))

print('************************************')

def spy_game1(nums):
    for i in range(0,len(nums)-1):
        if nums[i:i+3] == [0,0,7]:
            return True

    return False

print(spy_game([1,3,0,7]))
print(spy_game([1,1,1,0,0,7]))
print(spy_game([4,5,6,0,0,7]))

print('************************************')

#Here 0,0,7 does not have to be together. They can have any other number in between
def spy_game2(nums):

    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            #[0,0,7,'x'] --code
            #[0,7,'x']      --code.pop(0)
            #[7.'x']        --code.pop(0)
            #['x'] length=1 --code.pop(0) and code = ['x'] now. therefore, len(code) = 1
            code.pop(0)
    return len(code) == 1

print(spy_game2([1,3,0,7]))
print(spy_game2([1,0,1,4,0,7]))
print(spy_game2([4,5,6,0,1,2,0,5,6,7]))
print(spy_game2([4,5,6,7,0,0]))

print('************************************')

#COUNT PRIMES: Write a program that returns the number of prime numbers that exist up to and
#including a given number

def count_primes(num):
    #Check for 0 or 1
    if num < 2:
        return 0
    #2 or greater
    #List to store prime numbers
    primes = [2]
    #Counter going upto the input num
    x = 3
    #x is going through every number up to input number
    while x <= num:
        for y in range(3,x,2):  #for y in primes:
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(20))
print('************************************')
print(count_primes(50))
print('************************************')
print(count_primes(100))
print('************************************')

