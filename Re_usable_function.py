

def emoji_converter(message):
    words = message.split(' ')
    print(words)


    emojis = {
    ":)": "😊",
    ":(":"😒"
    }
    output = ""
    for wordy in words:
        output += emojis.get(wordy, wordy)  + " "
    return output
    
    

message= input(">")
result = emoji_converter(message)
print(result)

