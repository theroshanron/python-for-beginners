course = "Python \"Programming"
# """" quotes are for format of long strings (messages)
#"" double quotes are mostly preferred for the strings
# functions - a reusable piece of code to carry out the repetitive tasks

print(len(course))

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