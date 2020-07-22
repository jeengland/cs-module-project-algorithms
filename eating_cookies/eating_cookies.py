'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, arr=None):
    # Cases too small for the algorithm to work on them
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    # Set up empty list and base cases
    perm = [0 for i in range(0, n + 1)]
    perm[0] = 1
    perm[1] = 1
    perm[2] = 2
    # Run algorithm:
    # For a given n, the number of times 1, 2, and 3 will go into it is equal
    # to the number of times it went into the three numbers before it, summed
    # together. So working out the first 3 cases manually, we can iterate
    # from there through n to find our answer
    for i in range(3, n + 1):
        perm[i] = perm[i - 1] + perm[i - 2] + perm[i - 3]

    return perm[n]
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 4

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
