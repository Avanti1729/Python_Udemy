def master_yoda(text):
    mylist = text.split()
    print(mylist[::-1])
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True

    return False
def paper_doll(text):
    result = ''
    for char in text:
        result += 3 * char
    return result
def blackjack(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a, b, c] and sum([a, b, c]) <= 31:
        return sum([a, b, c]) - 10
    else:
        return "BUST"
def count_primes(nums):
    if nums<2:
        return 0
    primes=[2]

    for i in range(3,nums+1,2):
        count = 0
        for j in range(3,i+1,2):
            if i%j==0:
                count+=1
        if count == 1:
            primes.append(i)
    return primes
# mapping a function
def squaree(nums):
    return nums**2
nums=[1,2,3,4,5,6]
# lambda of a function
square = lambda num: num**2

def vol(rad):
    return (4/3)*(22/7)*(rad**3)
# print(vol(2))
# print(square(465))
# print(list(map(squaree,nums)))
# print(count_primes(99))
# print(blackjack(11,11,11))

# master_yoda("Hello My name is Avantika Gupta")
# print(has_33([1, 3, 1, 3, 1, 3, 3]))
# print(paper_doll("Hello"))
