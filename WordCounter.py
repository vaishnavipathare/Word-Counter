def word_counter(sentence):
    words = sentence.split()
    return len(words)

user_input = input("Enter a sentence: ")
word_count = word_counter(user_input)

print(f"Number of words in the sentence: {word_count}")