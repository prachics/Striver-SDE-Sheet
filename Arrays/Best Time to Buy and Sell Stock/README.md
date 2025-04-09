# Problem: Best Time to Buy and Sell Stock

**Leetcode Link:** [Leetcode 121 - Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Description:
You are given an array `prices` where `prices[i]` is the price of a stock on day `i`. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Approach:
- Track the minimum price so far while iterating through the array.
- For each day, calculate the profit if you sold the stock on that day.
- Keep track of the maximum profit seen so far.

## Time Complexity: O(n)  
## Space Complexity: O(1)

## Tags:
Array, Greedy
