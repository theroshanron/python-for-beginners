number = [5,4,7,89,8]

print(number.count(89))
number.insert(3,'ABC')
number.remove(8)
number.append(65)
number.reverse()
number.pop()
print(number.index(89))
print(number)
print(89 in number)
# number.sort()
# print(number)

num2 = number.copy()
print(num2)
number.append(83)
print(number)

# Exercise to remove duplicates
num = [2,2,4,5,6,3,7,6,8]
unique = []

for i in num:
    if i not in unique:
        unique.append(i)
print(unique)