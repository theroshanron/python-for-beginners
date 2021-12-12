message= input(">")

words = message.split(' ')
print(words)


emojis = {
":)": "😊",
":(":"😒"
}
output = ""
for wordy in words:
   output += emojis.get(wordy, wordy)  + " "
print(output)
