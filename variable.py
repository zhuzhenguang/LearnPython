print('hello world', end='!')

# input_string = input('Enter something:')
# print(input_string)

print('yes' if 0 > 1 else 'no')

li = [1, 2, 3]
print(li[-1])
print(li[1:3])
print(li[2:])
print(li[:1])
print(li[::2])
print(li[:])
other = [4, 5]
print(li + other)
li.extend(other)
print(li)
print(1 in li)

tup = (1, 2, 3)
print(type(1))
print(type((1,)))
print(len(tup))
tup + (4, 5, 6)
