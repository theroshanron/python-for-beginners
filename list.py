name =['Roshan','Durgesh','Kajal','Pooja','Bob','Jordam']

print(name)
print(name[2])
print(name[-1])
print(name[2:])
print(name[:4])
print(name[:])
print(name[:5])
name[0] = 'BATMAN'
print(name)

#exercise to find the largest number

list = [1,4,3,6,8,9]

print(max(list))


list2 = [1,4,3,6,8,9]
max =list2[0]
for i in list2:
    if i > max:
        max = i
print(max)
    
