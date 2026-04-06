import re

password = input("Enter your password: ")


length_ok = len(password) >= 8
has_digit = re.search(r"\d", password)
has_upper = re.search(r"[A-Z]", password)
has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)


if length_ok and has_digit and has_upper and has_special:
    print("Strong Password!!")
else:
    print("Weak Password")

    
    if not length_ok:
        print("- Password should be at least 8 characters long")
    if not has_digit:
        print("- Include at least 1 number")
    if not has_upper:
        print("- Include at least 1 uppercase letter")
    if not has_special:
        print("- Include at least 1 special character")
