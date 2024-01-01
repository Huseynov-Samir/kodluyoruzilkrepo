def split_and_join(line):
    # Split the string on a space delimiter
    words = line.split(" ")
    
    # Join the words using a hyphen
    joined_line = "-".join(words)
    
    return joined_line

# Read input
line = input().strip()

# Call the function and print the result
result = split_and_join(line)
print(result)
