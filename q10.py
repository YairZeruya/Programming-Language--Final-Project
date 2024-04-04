from functools import reduce
 
concat_strings = lambda strings: reduce(lambda x, y: x + ' ' + y, strings)
input_list = ["hello", "world", "how", "are", "you"]
result = concat_strings(input_list)
print(result)