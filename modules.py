
#Module should contain all the related functions and classes
#helps in better organizing our codes

import converters

print(converters.kg_to_lbs(80))


from converters import lbs_to_kg
print(lbs_to_kg(90))



#Exercise
numbers_list=[12,5,6,18,9,20,28]
import utility

y= utility.find_max2(numbers_list)
print(y)

num_list2 = [12,5,6,18,9,34,20,28]

from utility import find_max2

x = find_max2(num_list2)
print(x)