def main():
    password = input("Password: ")
    if len(password) < 8 or len(password) > 20:
        print("New password must have 8 to 20 characters!")


main()
