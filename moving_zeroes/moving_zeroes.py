'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    answer = []

    for number in arr:
        if number == 0:
            answer.append(number)

        else:
            answer = [number] + answer

    return answer


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
