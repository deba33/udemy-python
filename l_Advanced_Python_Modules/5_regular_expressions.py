# re module

import re

patterns = ["term 1", "term 2"]

text = "This is a string with term 1, but not other term"

for pattern in patterns:
    print(f"Searching for {pattern} in: \n{text}")

    if re.search(pattern, text):
        print("\nMatch was found.\n")
    else:
        print("\nNo match was found. \n")


match = re.search(patterns[0], text)

print(type(match))

print(match.start())
print(match.end())

split_term = "@"
phrase = "What is your email, is it hello@gmail.com?"
print(re.split(split_term, phrase))

print(re.findall("term", text))
