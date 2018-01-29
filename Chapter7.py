"""how many odd numbers are in a list."""

numlist=[0,2,3,7,11,12]

def count_odd(numlist):
    count = 0
    for i in numlist:
        if i%2 != 0:
            count += 1
            
    return count

print(count_odd(numlist))

"""how many even numbers in a list."""

def sum_even(numlist):
    sum=0
    for i in numlist:
        if i%2 == 0:
            sum = sum +i
            
    return sum
print(sum_even(numlist))

"""how negative in a list"""
def sum_neg(numlist):
    total=0
    for n in numlist:
        if n < 0:
            total=total+n
    return total
print (sum_neg(numlist))
#4
wordlist=["one", "two", "three", "four", "five", "six", "seven", "eight"]
def count_words(wordlist):
    count=0
    for n in wordlist:
        if len(n)==5:
            count+=1           
    return count
print(count_words(wordlist))

#5
def sum_evenbuttheirst(numlist):
    sum=0
    for n in numlist:
        if n%2 == 0:
            sum=0
            break
    for n in numlist:
        if n%2 ==0:
            sum+=n
    return sum
print(sum_evenbuttheirst(numlist))

#6
namelist=["owen","stef","annie", "tianhao", "leo", "Justice", "sam", "maikel","kayla", "gen"]

def sam(namelist):
    count=0
    for i in namelist:
        if i == "sam":
            count+=1
            break
        else:
            count+=1
print(sam(namelist))
        
        