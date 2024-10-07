def generate_password(name):
    if len(name) < 3:
        return "Name must contain at least 3 characters."

    lc = name[-1]  # Last character
    le = len(name)  # Length of the name
    fc = name[0]  # First character

    # Generate password based on the length of the name
    if le % 2 == 0:  # Even length
        password = lc + str(le) + "@" + fc + "654" + lc
    else:  # Odd length
        password = lc + str(le) + "!" + fc + "432" + lc

    return password

# Input format
name = input("Enter the name: ")

# Generate and print the password
password = generate_password(name)
print(f"Generated password: {password}")