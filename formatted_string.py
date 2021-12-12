first = 'Roshan'
last = 'Chaudhary'

message = first + ' [' + last + '] is a coder'

msg = f'{first} [{last}] is a coders' 
# For pre-formatted strings use 'f' as pre-fix and curly braces for the placeholders
print(msg)
print(message)

if (msg == message):
    print('Yo! It\'s a match')
else:
    print('Nah bro! did not happen')
