def is_palindrome(s): 
    return s == s[::-1]
while True:
    user_input = input("Enter a string to check if it's a palindrome (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome.")
    else:
        print(f"'{user_input}' is not a palindrome.") 
    continue_choice = input("want to check another string (y/n)? ")    
    if continue_choice.lower() != 'y':
        break