def main():
    print("This is the email slicer")
    print("")

    email_input = input("Enter email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username : ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

while True:
    main()