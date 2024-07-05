def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def main():
    test_string = input("Enter a string to check if it is a palindrome: ")
    if is_palindrome(test_string):
        print(f'"{test_string}" is a palindrome.')
    else:
        print(f'"{test_string}" is not a palindrome.')

if __name__ == "__main__":
    main()

