import hashlib
ip_address="192.168.1.1"
password=input("Enter your password: ")
masked_pass="*"*(len(password)-2)+password[-2:]
print(f"your password is {masked_pass}")
hashed_pass=hashlib.sha256(password.encode()).hexdigest()
print(f"Your Hashed password is {hashed_pass}")
ip_address=ip_address.split(".")
print(f"IP OCTET : {ip_address}")