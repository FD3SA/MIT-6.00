##x = 3 #creates variable and assign value 3 to it
##x = x*x #Bind x to value 9
##print x


##n = int(raw_input('Enter a number: '))
##print n
##print n/n

##x = int(raw_input('Enter a number: '))
##if (x/2)*2 == x:
##    print 'Even'
##else: print 'Odd'


##z = 'b'
##if 'a'<z:
##    print 'Hello'
##else: print 'Mom'
    

##x = 15  
##y = 11
##z = 5
##print x,y,z
##
##if x < y:         #does not compare y and z, simply assumes y is least if x>y
##    if x<z: print 'x is least'
##    else:print 'z is least'
##else: print 'y is least'
    
##x = 15
##y = 5
##z = 11
##print x,y,z
##
##if x < y and x < z:
##    print x, ' is least'
##elif y < z:
##    print y, ' is least'
##else:
##    print z, ' is least'

##y = 0  #squares y by adding x to itself x times
##x = 3
##
##itersleft = x
##
##while itersleft > 0:
##    y += x   
##    itersleft -= 1
##    print 'y =',y,'iterslef=',itersleft

##x = 9 #determines the square root of integer x by starting at 1 and squaring value
##
##ans = 0
##while ans*ans != x:
##    ans += 1
##    print ans
##else:
##    print 'The square root of',x,'is',ans
    
##x = 10 #finds the divisors of x by starting at 1 and going up by 1
##i = 1
##while i < x:
##    if x%i == 0:
##        print i,'is a divisor'
##    i += 1

x = 10
for i in range(1,x):
    if x%i == 0:
        print i,'is a divisor'




    




