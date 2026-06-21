def word_counter():
    print("Welcome to the Word Counter Program!")
    
    
    user_input = input("Enter a sentence or paragraph: ")
    
    
    words = user_input.split()
    
    
    word_count = len(words)
    
    print(f"Total numbber of words (Total words): {word_count}")

# Program-ah run panrom
word_counter()