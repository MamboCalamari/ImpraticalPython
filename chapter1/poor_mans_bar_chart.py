import pprint
from collections import defaultdict

# simulates a character bar chart with a pretty printed dictionary given user's sentence
def main():

    while True:
        sentence_input = input("\nWrite a sentence for a dict bar chart: ""\n")

        char_dict = generate_sentence_dict(sentence_input)

        # TODO text part
        # pprint includes newlines based of width and sorts char_dict alphabetically
        pprint.pprint(char_dict, width=100)

        try_again = input("\n\nTry again? (Press Enter else q to quit)\n ")

        if try_again.lower() == "q":
            break

    input("\nPress Enter to exit.")


def generate_sentence_dict(sentence_input):
    sentence_input = sentence_input.lower()
    # collections.defaultdict lets us append to lists
    sentence_dict = defaultdict(list)
    for c in sentence_input:
        if c.isalpha():
            sentence_dict[c].append(c)
    return sentence_dict


if __name__ == "__main__":
    main()