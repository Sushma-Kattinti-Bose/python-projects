def count_vowels():

    sentence = "now is the time for all the good people to come to an aid"
    count = 0
    for letter in sentence:
        if letter == 'a' or letter == 'e'or letter == 'i'or letter == 'o'\
             or letter == 'u':
            count = count + 1
    print("The vowels in the sentence are:" + str(count))

if __name__ == "__main__":
    count_vowels() 