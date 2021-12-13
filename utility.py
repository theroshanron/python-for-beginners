def find_max2(enter_list):
    max2=enter_list[0]

    for numbers in enter_list:
        if numbers > max2:
            max2 = numbers
    return max2

num_list=[12,5,6,18,9,20]

print(find_max2(num_list))