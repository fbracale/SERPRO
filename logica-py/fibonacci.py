import time

def FibonacciSemCache(n):
    if n in {0, 1}:
        return n
    return FibonacciSemCache(n-1) + FibonacciSemCache(n-2)

cache = {0:0, 1:1}
def FibonacciComCache(n):
    if n in cache:
        return cache[n]
    cache[n] = FibonacciComCache(n-1) + FibonacciComCache(n-2)
    return cache[n]

if __name__ == '__main__':
    
    #inicio contagem 1
    begin1 = time.time()
    
    #execução 1 (sem cache)
    result1 = FibonacciSemCache(12)

    #fim contagem 1
    time.sleep(1)
    end1 = time.time()
    
    #inicio contagem 2
    begin2 = time.time()
    
    #execução 2 (com cache)
    result2 = FibonacciComCache(120)

    #fim contagem 2
    time.sleep(1)
    end2 = time.time()


    print(f"Tempo execução sem Cache: {end1 - begin1}")
    print(f"Tempo execução com Cache: {end2 - begin2}")

    print(cache)
