"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.

Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.
"""


def distinct_step_sequences(num: int):
    result = 1
    prev = 1
    prev_2 = 0
    for i in range(num):
        result = prev + prev_2
        prev_2 = prev
        prev = result

    return result


"""
0: 1
1: 1, 1 + 0
2: 2, 1 + 1
3: 3, 2 + 1
4: 5, 3 + 2

"""


if __name__ == "__main__":
    for ind in range(10):
        print(f"{ind}: {distinct_step_sequences(ind)}")
