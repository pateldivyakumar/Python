def split_string(sentence):
    words = sentence.split()
    return words

sentence = input("Enter a sentence: ")
words = split_string(sentence)
print("Words in the sentence:", words)
