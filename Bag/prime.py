from math import sqrt

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0 or num < 2:
        return False
    max = int(sqrt(num))
    for i in range(3, max+1, 2):
        if num % i == 0:
            return False
    return True

'''
First way i thought to write this but is bad since i am not keeping the list of primes 
between calls plus i wont be doing a lot of prime checking i dont think, 
it is faster to just check every num up to sqrt.

def is_prime(num):
    if num == 2:
        return True
    if num%2 == 0 or num < 2:
        return False
    for prime in next_prime(int(sqrt(num))):
        if num%prime == 0:
            return False
    return True

def next_prime(max):
    primes = [2]
    yield primes[-1]
    for i in range(3,max+1,2):
        j = 0
        local_max = int(sqrt(i))
        prime = True
        while primes[j] <= local_max:
            if i%primes[j] == 0:
                prime = False
                break
            j += 1
        if prime:
            primes.append(i)
            yield i
'''