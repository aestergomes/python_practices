# Prime numbers have only two divisors: 1 and itself.
# Ex.: 2, 3, 5 and 7...
check_prime = [26, 39, 51, 53, 57, 79, 85]
for num in check_prime:
    for i in range(2, num):
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break
        if i == num -1:    
            print("{} IS a prime number".format(num))