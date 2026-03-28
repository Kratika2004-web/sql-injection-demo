username = input("Enter username: ")
password = input("Enter password: ")

query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

print("\nExecuting Query:")
print(query)

# Convert to lowercase for easy detection
user_input = username.lower()

# Normal login
if username == "admin" and password == "1234":
    print("Login Successful!")

# SQL Injection detection (strong condition)
elif "'" in username and "or" in user_input:
    print("Login Bypassed! (SQL Injection Successful)")

else:
    print("Invalid Credentials")