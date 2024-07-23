def main():
    with open('books/frankenstein.txt') as f:
        text = f.read()
        words = text.split()
        number_of_words = len(words)
        
        Letters = {}
        for letter in text:
            lowered = letter.lower()
            if lowered.isalpha():    
                if lowered in Letters:
                    Letters[lowered] += 1
                
                else:
                    Letters[lowered] = 1
        sorted_letters = sorted(Letters.items(), key=lambda item: item[1], reverse=True)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{number_of_words} words found in the document")
        for letter, count in sorted_letters:
            print(f"the '{letter}' character was found {count} times")
        print("--- end report ---")
        



main()
