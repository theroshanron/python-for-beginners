

# for x in range (4):
#     for y in range(3):
#         print(f'({x},{y})')


#Exercise

# items = [5,2,5,2,2]

# for x in items:
#     print('x'*x)   #Shortcut 



items = [5,2,5,2,2]


for x in items:
    output = ''
    # print(output)
    # print(x)
    for y in range(x):   # This loop will run five times to add value in output and then two times so on... to store the x string in output
        output += 'x'
    print(output)