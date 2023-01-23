some_list = [1, 2, 3]

# такой себе пример, используй нижний.
for item in enumerate(some_list):
    print(f'item with index {item[0]} is {item[1]}')

for index, value in enumerate(some_list):
    print(f'item with index {index} is {value}')
