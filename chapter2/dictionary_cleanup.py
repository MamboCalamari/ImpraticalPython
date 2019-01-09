from chapter2.authorcode.load_dictionary import load
from string import ascii_lowercase


def main():
    word_list = load('D:\\Code\\ImpraticalPython\\res\\dictionary.txt')
    for word in word_list:
        if len(word) == 1:
            print(word)
    for c in ascii_lowercase:
        try:
            word_list.remove(c)
        except ValueError:
            pass
    for word in word_list:
        if len(word) == 1:
            print(word)

if __name__ == '__main__':
    main()