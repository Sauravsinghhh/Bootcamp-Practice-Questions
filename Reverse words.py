def reverse_words(text):
    # Split the text into words using spaces as the delimiter
    words = text.split()
    
    # Reverse the order of words
    reversed_words = words[::-1]
    
    # Join the reversed words back into a string with spaces in between
    reversed_text = ' '.join(reversed_words)
    
    return reversed_text

# Example usage:
input_text = "Hello world this is an example"
reversed_text = reverse_words(input_text)
print(f"Original text: {input_text}")
print(f"Reversed words text: {reversed_text}")
