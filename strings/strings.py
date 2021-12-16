course = "Python \"Programming"
# """" quotes are for format of long strings (messages)
#"" double quotes are mostly preferred for the strings
# functions - a reusable piece of code to carry out the repetitive tasks

print(len(course)) #len to calculate length 

print(course[7])
print(course[1])
print(course[0:3])
print(course[4:])
print(course[:])
print(course[:4])


# \ escape character whereas # is comment
#\" escapes double quote
# \' escapes single quote
#\\ includes one backslash
#\n new line


first = "Roshan"
last = "Chaudahry"

full = first + " " + last # concatenation
full_formatted = f"{len(first)} {last}" #formatted text

print(full)
print(full_formatted)


print(course.upper())
print(course.lower())

print(course.strip())

print(course.find("Py")) #case sensitive and helpful to find index of the string

print(course.replace("P", "C"))

print("th" in course) # to check the existence of letter string in defined variable and returns a boolean

print("swift" not in course) # to check whether it exist in boolean