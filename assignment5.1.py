while True:
    input_str = input("Please enter two words (or 'done' to exit): ").strip()
    
    if input_str == 'done':
        break
    
    words = input_str.split()
    
    if len(words) == 1:
        word = words[0]
        print(f"The word is: {word}")
    elif len(words) == 2:
        word1, word2 = words[0], words[1]
        if word1 < word2:
            print(f"The word that comes first is: {word1} ")
        elif word2 < word1:
            print(f"The word that comes first is: {word2}")
        else:
            print("Both words are the same.")
    else:
        print("Invalid input. Please enter two words separated by a space or 'done' to exit.")
