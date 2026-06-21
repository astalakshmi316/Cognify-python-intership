def generate_fibonacci():
    print("Welcome to the Fibonacci Sequence Generator!")
    
    
    n_terms = int(input("Enter the number of terms: "))
    
    
    fib_sequence = []
    
    if n_terms <= 0:
        print("Please enter a positive integer greater than 0.")
        return
    elif n_terms == 1:
        fib_sequence = [0]
    else:
        fib_sequence = [0, 1]
        
        while len(fib_sequence) < n_terms:
            next_term = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_term)
            
    print(f"The Fibonacci sequence up to {n_terms} terms is:")
    print(fib_sequence)


generate_fibonacci()
