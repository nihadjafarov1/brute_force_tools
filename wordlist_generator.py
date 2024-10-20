import itertools
import argparse

parser = argparse.ArgumentParser(description="Brute force password length.")
parser.add_argument("-username", type=str, required=True, help="Username for the login")
args = parser.parse_args()

base_username = args.username

characters = ['.', '_', '-', '!', '@', '123', '2024']
numbers = [str(i) for i in range(100)] 

case_variations = set(map(''.join, itertools.product(*((c.upper(), c.lower()) for c in base_username))))

wordlist = set()

for variation in case_variations:
    wordlist.add(variation)
    for char in characters:
        wordlist.add(variation + char)
        wordlist.add(char + variation)
    for number in numbers:
        wordlist.add(variation + number)
        wordlist.add(number + variation)

with open("username_wordlist.txt", "w") as f:
    for word in sorted(wordlist):
        f.write(word + "\n")

print("Wordlist generated and saved to 'username_wordlist.txt'")
