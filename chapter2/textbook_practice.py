def main():
    string = "Test String"

    print("Creates substring from every second letter of string[5:9]:")
    print(string[5:9:2])
    print("Creates substring from every second letter of string[5:9], starting from the end:")
    print(string[9:5:-2])
    return

if __name__ == "__main__":
    main()
