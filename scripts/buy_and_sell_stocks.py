"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design
an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""


def max_profit(nums: list):
    if not nums:
        return 0

    profit = price = 0

    for num in reversed(nums):
        price = max(num, price)
        profit = max(profit, price - num)

    return profit


if __name__ == "__main__":
    print(f"[7, 1, 5, 3, 6, 4]: {max_profit([7, 1, 5, 3, 6, 4])}")
    print(f"[7, 6, 4, 3, 1]: {max_profit([7, 6, 4, 3, 1])}")
    print(f"[7, 1, 5, 3, 6, 4]: {max_profit([7, 1, 5, 3, 6, 4])}")
    print(f"[7, 5, 3, 2, 1]: {max_profit([7, 5, 3, 2, 1])}")
    print(f"[7, 4, 10, 2, 6, 11]: {max_profit([7, 4, 10, 2, 6, 11])}")
