Weight = input ("Enter your weight: ")
print("Thank you for sharing!")
conversion= input("Please tell us whether in Lbs or Kgs: ")
entered_weight = conversion.lower()

if entered_weight == "l":
   weight_in_kgs = float(Weight) / 2.2
   print(f"Your are {weight_in_kgs} kgs")
elif conversion == "K":
    weight_in_pounds = float(Weight) * 2.2
    print(f"Your weight is {weight_in_pounds} lbs")
else:
    print("Type the correct conversion: ")


