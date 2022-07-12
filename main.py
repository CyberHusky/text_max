print()
sdasdas
print()






'''
# -- 3 -- List Comprehension
squares = [i * i for i in range(10)]
print(squares)



# new_list = [expression for member in iterable (if conditional)]
sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']
print(vowels)

#new_list = [expression (if conditional) for member in iterable]
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)
prices2 = [i for i in original_prices if i > 0]
print(prices2)
'''


# Создать список из 30 элементов случайных чисел + randint
# Создать список из элементов случайных чисел которые больше некого числа
# Создать список из элементов случайных чисел которые больше 20
# и числа которые меньше 20 стают отрицательными

from random import randint
print( [i for i in randint(1, 100) if i>15] )

