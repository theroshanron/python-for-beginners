# customer = {

# "name" : " Roshan", 
# "Age" : 26,
# "is_verified" : True

# }

# customer["Age"] = 24
# customer["Birth"] = 1995
# print(customer)
# print(customer["name"])
# print(customer.get("Birth_date", "10th December, 1995"))

#Exercise

phone= input("Enter your phone number: ")
phone_number = {
"1":"one",
"2":"two",
"3":"three",
"4":"four"
}

output =""
for i in phone:
   output += phone_number.get(i, "!") + " "
print(output)