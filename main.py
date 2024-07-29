def caching_fibonacci():
    # порожній словник
    cache = {}
    def fibonacci(n):
    # базові випадки
        if n <= 0:
            return 0
        elif n == 1:
            return 1
    # перевірка результату у кеші
        if n in cache:
            return cache[n]
    # обчислюємо число Фібоначчі рекурсивно і зберигаєм у кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

    #  приклад

fib = caching_fibonacci()
print(fib(10))
print(fib(15))