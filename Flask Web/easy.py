from nth import flag1
import base64
code = input("Enter a code: ")
if code[::-1] == "1234":
    print(f"Access granted. Flag { {flag1} }")
else:
    print("Access denied.")