"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it
will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.
"""


def max_stolen(house_riches):
    memo = [-1] * len(house_riches)
    return max_stolen_recursive(house_riches, 0, memo)


def max_stolen_recursive(house_riches: list, ind: int, memo: list):
    if not ind < len(house_riches):
        return 0
    if not memo[ind] >= 0:
        memo[ind] = max(house_riches[ind] + max_stolen_recursive(house_riches, ind+2, memo),
                        max_stolen_recursive(house_riches, ind+1, memo))

    return memo[ind]


if __name__ == "__main__":
    print(f"[7, 1, 5, 3, 6, 4]: {max_stolen([7, 1, 5, 3, 6, 4])}")
    print(f"[7, 6, 4, 3, 1]: {max_stolen([7, 6, 4, 3, 1])}")