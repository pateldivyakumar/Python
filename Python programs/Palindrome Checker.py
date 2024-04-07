def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a word: ")
if is_palindrome(word):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
