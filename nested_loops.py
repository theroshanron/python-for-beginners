

# for x in range (4):
#     for y in range(3):
#         print(f'({x},{y})')


#Exercise

# items = [5,2,5,2,2]

# for x in items:
#     print('x'*x)



items = [5,2,5,2,2]


for x in items:
    output = ''
    # print(output)
    # print(x)
    for y in range(x):
        output += 'x'
    print(output)