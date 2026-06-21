def is_palindrome(word):
    # Word-ah lowercase mathi, space ethavathu iruntha remove panrom
    clean_word = word.lower().replace(" ", "")
    # Clean panna word-um athoda reverse-um samama nu check panrom
    return clean_word == clean_word[::-1]

# User kitta irundhu input vanga
user_word = input("Enter a word to check palindrome: ")

if is_palindrome(user_word):
    print(f"Yes, '{user_word}' is a palindrome!")
else:
    print(f"No, '{user_word}' is NOT a palindrome.")