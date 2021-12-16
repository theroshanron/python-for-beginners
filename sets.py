# collection with no duplicates
#unordered collection of unique items and not in sequence

numbers = [1,1,1,2,3,4,4,5]
c = set(numbers)
print(c)

num = {3,5,7,4}
num.add("8")

num.remove(7)

print(len(num))
print(num)


print(c | num) #union in sets
print(c & num) #intersection
print(c - num) #difference
print(c ^ num)

print("Hello boy")

#set object does not support indexing

if 1 in c:
    print("yes") #check numbers existence in set