def count_substring(string, sub_string):
    count = 0
    start_index = 0

    while start_index != -1:
        start_index = string.find(sub_string, start_index)
        if start_index != -1:
            count += 1
            start_index += 1  # Move to the next index after the found substring

    return count

# Input
string = input().strip()
sub_string = input().strip()

# Output
result = count_substring(string, sub_string)
print(result)
