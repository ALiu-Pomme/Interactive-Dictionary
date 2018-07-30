import json

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    else:
        return "The word does not exist, please double check it"

word = input("Please enter the word you want to look up: ").lower()

print(translate(word))