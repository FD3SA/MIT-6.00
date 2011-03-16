x = 100
divisors = []
for p in range (1,x):
    if x%p == 0:
        divisors = divisors + [p]
print divisors
