'''
Input: a List of integers as well as an integer `k` representing the size of
the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    solution = []
    window = []
    for i in range(len(nums)):
        window = [nums[i]] + window
        if len(window) == k:
            solution.append(max(window))
            window.pop()
    return solution


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    solution = sliding_window_max(arr, k)

    print(f"Output of sliding_window_max function is: {solution}")
