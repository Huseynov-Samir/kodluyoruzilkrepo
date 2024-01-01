if __name__ == '__main__':
    n = int(input().strip())

    # Using a loop to print the consecutive integers without spaces
    for i in range(1, n + 1):
        print(i, end='')

    # If you prefer a single print statement
    # print(''.join(map(str, range(1, n + 1))))

