def mutate_string(s, position, character):
    # Convert the string to a list to make changes
    s_list = list(s)
    
    # Change the character at the given position
    s_list[position] = character
    
    # Join the list back into a string
    modified_string = ''.join(s_list)
    
    return modified_string

# Read input
s = input().strip()
position, character = input().split()
position = int(position)

# Call the function and print the result
result = mutate_string(s, position, character)
print(result)
