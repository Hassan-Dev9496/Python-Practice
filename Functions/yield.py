def even_numbers(limit):
    for i in range(2 , limit , 2):
        yield i

numbers = even_numbers(10)
print(*numbers)
