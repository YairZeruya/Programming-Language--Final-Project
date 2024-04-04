from functools import reduce

count_palindromes = lambda lst: list(map(lambda sublist: reduce(lambda x, _: x + 1, filter(lambda word: word == word[::-1], sublist), 0), lst))

input_lists = [['level', 'noon', 'hello'], ['radar', 'banana', 'world'], ['madam', 'racecar', 'python']]
result = count_palindromes(input_lists)
print(result)  # Output: [2, 1, 2]
