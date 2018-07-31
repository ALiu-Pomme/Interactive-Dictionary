import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff = 0.8)) > 0:
        while 1:
            correction = input("Did you mean %s instead? Please enter Y for yes or N for no: " %get_close_matches(word, data.keys())[0])
            if correction.lower() == "y":
                return data[get_close_matches(word, data.keys())[0]]
            elif correction.lower() == "n":
                return "The word does not exist, please double check it."
            else:
                print("That is not a valid input. Please try again.")
    else:
        return "The word does not exist, please double check it."

word = input("Please enter the word you want to look up: ").lower()

output = translate(word)

if type(output) == list:
    for entry in output:
        print(entry)
else:
    print(output)