import re

def is_valid_email(email):
    # Email format-ah check panna intha regular expression pattern use aagum
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(email_regex, email):
        return True
    return False

# User kitta irundhu input vanga
test_email = input("Enter an email id to validate: ").strip()

if is_valid_email(test_email):
    print(f"Yes, '{test_email}' is a valid email format!")
else:
    print(f"No, '{test_email}' is an invalid email format.")