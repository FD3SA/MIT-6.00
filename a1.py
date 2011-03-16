#Problem 1:

##primes = [2]
##
##i = 1
##
##isprime = False
##
##while len(primes) < 1000:
##    i += 1
##    for j in range(2,i):
##        if i%j == 0:
##            isprime = False
##            break
##        else:
##            isprime = True
##
##    if isprime == True:
##        primes += [i]
##        #print i
###else: print primes[999]

#Problem 2:

n = int(raw_input('enter a positive integer: '))

primes = [2]

i = 1

isprime = False



while primes[-1] < n:
    i += 1
    for j in range(2,i):
        if i%j == 0:
            isprime = False
            break
        else:
            isprime = True

    if isprime == True:
        primes += [i]
        print i

primes = primes[0:-1]
print primes


sumprimes = 0

import math
for k in primes:
    sumprimes += math.log(k)

print 'sumprimes =',sumprimes
print 'n = ',n
print 'sumprimes/n =',sumprimes/n
                            
