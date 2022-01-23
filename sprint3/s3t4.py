def divisor(num):
    for i in range (1,num+1):
        if num % i == 0:
            yield i
    while True:
        yield None