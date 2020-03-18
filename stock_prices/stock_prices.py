#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # loop though prices
    # second loop though the last part of prices, with i.
    # subtract i from j, storing the max_profit_so_far
    # contain max_profit_so_far and current_min_price_so_far
    # record the biggest differece between the two
    max_profit_so_far = -99999
    # current_min_price_so_far = 0
    for i in range(len(prices)):
        print("prices[i]", prices[i:])
        if len(prices[i:]) > 0:
            for j in range(i, len(prices) - 1):
                if j == i:
                    j += 1
                if prices[j] - prices[i] > max_profit_so_far:
                    max_profit_so_far = prices[j] - prices[i]

    return max_profit_so_far


# print(find_max_profit([1050, 270, 1540, 3800, 2]))

# print(find_max_profit([100, 90, 80, 50, 20, 10]))
# print(find_max_profit([10, 7, 5, 8, 11, 9]))

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
