def count_vowels_consonants(string):
    vowels = 0
    consonants = 0
    for char in string:
        if char.lower() in 'aeiou':
            vowels += 1
        elif char.isalpha():
            consonants += 1
    return vowels, consonants

string = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(string)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
