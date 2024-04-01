#Write a Python program to count the occurrences of each word in a given sentence



def count_word_occurrences(sentence):
    word_count = {}
    words = sentence.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


sentence = input("Enter a sentence: ")
word_occurrences = count_word_occurrences(sentence)

print("Occurrences of each word:")
for word, count in word_occurrences.items():
    print(f"{word}: {count}")
