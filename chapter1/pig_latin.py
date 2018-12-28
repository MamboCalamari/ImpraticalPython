vowels = ['a', 'e', 'i', 'o', 'u']


# translates either a word or sentence to pig latin based on input
def main():

    while True:
        word_or_semtence_input = input("\nWould you like to translate a word or a sentence? "
                                       "(w for word, s for sentence)\n")
        if word_or_semtence_input == "w":
            english_word = input('Enter an English word to be translated to Pig Latin: ')
            pig_latin_word = translate_word(english_word)
            print(pig_latin_word)
        else:
            english_word = input('Enter an English sentence to be translated to Pig Latin: ')
            pig_latin_word = translate_sentence(english_word)
            print(pig_latin_word)

        try_again = input("\n\nTry again? (Press Enter else q to quit)\n ")

        if try_again.lower() == "q":
            break

    input("\nPress Enter to exit.")


# translate a single word to pig latin
def translate_word(english_word):
    does_start_with_vowel = False
    for v in vowels:
        if english_word[0] == v:
            does_start_with_vowel = True
            break
    if does_start_with_vowel:
        return english_word + "way"
    else:
        return english_word[1:] + english_word[0] + "ay"


# translate an entire sentence to pig latin
def translate_sentence(english_sentence):
    # get rid of period
    english_sentence = english_sentence[:-1].lower()
    words = english_sentence.split()
    pig_latin_sentence = ""
    for i in range(len(words)):
        # if last word of sentence, add period
        if i == len(words) - 1:
            pig_latin_sentence += translate_word(words[i]) + "."
        # if first word of sentence, capitalize first word
        elif i == 0:
            lower_first_word = translate_word(words[i])
            upper_first_word = lower_first_word[0].upper() + lower_first_word[1:]
            pig_latin_sentence += upper_first_word + " "
        # otherwise add space
        else:
            pig_latin_sentence += translate_word(words[i]) + " "
    return pig_latin_sentence


if __name__ == "__main__":
    main()