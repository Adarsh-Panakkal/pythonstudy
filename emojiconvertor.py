message = input("> ")
words = message.split(" ")
emojis ={
    ":)":"😁",
    ":(":"😞",
    ":'(":"😢",

    ":O":"😮",
    ":*":"😚",
    ":/":"🫤"



}
output1 = ""
for em in words:

  output1 +=  emojis.get(em,em)+" "
print(output1)