import re

def validate_phonenumber(data):
    phone_number = data.get("phone")

    if phone_number:
        pattern = r'^99\d{8}$'

        if re.match(pattern, phone_number):
            print("Valid phone number:", phone_number)
        else:
            print("Invalid phone number:", phone_number)
    else:
        print("Phone number not provided in the data.")


def validate_email(data):
    email = data.get("email")

    if email:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(pattern, email):
            print("Valid email:", email)
        else:
            print("Invalid email:", email)
    else:
        print("Email not provided in the data.")