#if an applicant has high income AND good credit, he is eligible for loan

# AND operator -- both condition should be true

high_income = True
good_credit = True

if high_income and good_credit:
    print ("Eligible for loan")
else:
    print("Not eligible")

# Or operator -- at lease one condition should be true

high_income = True
good_credit = False

if high_income or good_credit:
    print ("Eligible for loan")
else:
    print("Not eligible")


good_credit = True
has_criminal_record = True

if good_credit and not has_criminal_record:
    print("Eligible boy")
else:
    print("Our boy is not eligible")
    