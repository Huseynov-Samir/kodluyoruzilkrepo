# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

def word_indices(n, m, group_a, group_b):
    # Create a defaultdict with a default value of an empty list
    word_positions = defaultdict(list)

    # Populate the defaultdict with the positions of each word in group A
    for i in range(1, n + 1):
        word_positions[group_a[i - 1]].append(i)

    # Check and print the positions of each word in group B
    for word in group_b:
        if word in word_positions:
            print(*word_positions[word])
        else:
            print(-1)

# Input
n, m = map(int, input().split())
group_a = [input().strip() for _ in range(n)]
group_b = [input().strip() for _ in range(m)]

# Output
word_indices(n, m, group_a, group_b)
