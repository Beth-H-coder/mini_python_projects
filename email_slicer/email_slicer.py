email = input("Please enter your email: ").strip()
if '@' not in email:
    print('Invalid email entered!')

index = email.index("@")
username = email[:index] 
domain = email[index + 1:]
print(f"Your username is {username} and the domain is {domain}.")


