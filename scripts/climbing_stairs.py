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


if __name__ == "__main__":
    for ind in range(10):
        print(f"{ind}: {distinct_step_sequences(ind)}")
