"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum."""


def max_sub_array(nums: list):
    global_max = nums[0]
    local_max = 0

    for i in range(len(nums)):
        local_max = max(nums[i], nums[i] + local_max)

        if local_max > global_max:
            global_max = local_max

    return global_max


if __name__ == "__main__":
    input_arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sub_array(input_arr))
