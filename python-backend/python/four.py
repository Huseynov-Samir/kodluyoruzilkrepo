def is_leap(year):
    # Leap year condition
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Read the input year from STDIN
year = int(input().strip())

# Call the function and print the result
print(is_leap(year))
