email_user = input("Enter your email address: ")

if email_user.lower().endswith(".com"):
     if email_user.count("@") == 1:
         print("Valid email address.")
     else:
         print("Invalid email address.")
else:
    print("Invalid email address.")