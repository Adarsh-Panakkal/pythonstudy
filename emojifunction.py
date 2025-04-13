
def emoji_convertor(message):
    words = message.split(" ")
    emojis = {
        ":)": "😁",
        ":(": "😞",
        ":'(": "😢",

        ":O": "😮",
        ":*": "😚",
        ":/": "🫤"

    }
    output1 = ""
    for em in words:
        output1 += emojis.get(em, em) + " "
    return output1

message = input("> ")
result = emoji_convertor(message)
print(result)