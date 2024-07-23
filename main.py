def main():
    with open('books/frankenstein.txt') as f:
        text = f.read()
        words = text.split()
        number_of_words = len(words)
        Letters = {}
        for letter in text:
            lowered = letter.lower()
            if lowered in Letters:
                Letters[lowered] += 1
            else:
                Letters[lowered] = 1
        print(Letters)



main()
