from nth import flag1
import base64
code = input("Enter a code: ")
if code[::-1] == "bird":
    print(f"Access granted. hex{ {flag1} }")
else:
    print("Access denied.")