def count_word_occurrences():
    print("Welcome to the File Word Counter Program!")
    file_name = "sample.txt"
    
    try:
        with open(file_name, "r") as file:
            content = file.read()
            
            words = content.lower().split()
            word_counts = {}
            
            for word in words:
                word = word.strip(".,!?\"'()[]{}")
                if word:
                    word_counts[word] = word_counts.get(word, 0) + 1
            
            print("\nWord Counts in 'sample.txt':")
            print("-" * 30)
            for word, count in sorted(word_counts.items()):
                print(f"{word}: {count}")
            print("-" * 30)
            
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found. Please ensure it is in the same folder.")

count_word_occurrences()