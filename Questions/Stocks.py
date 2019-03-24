class Stocks:
    def __init__(self, prices):
        self.prices = prices

    """
    Say you have an array for which the ith element is the price of a given stock on day i.

    If you were only permitted to complete at most one transaction
    (i.e., buy one and sell one share of the stock),
    design an algorithm to find the maximum profit.

    Note that you cannot sell a stock before you buy one.

    Example:
    Input: [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                Not 7-1 = 6, as selling price needs to be larger than buying price.
    """
    def maxProfitSingle(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        """
        Explanation: Using a greedy algorithm, start at the very end of the array and go backwards.
        You only care about the max difference up to the point of the end value until you find an end
        value that's greater. At which point, you consider that new max value the end and find the max
        difference up to that point.
        """

        # base case: array is empty or has 1 element
        if len(prices) == 0 or len(prices) == 1: return 0
        
        # start at the end with a max difference of 0
        last = prices[len(prices) - 1]
        maxDiff = 0
        
        # start your comparisons at the element right before the last
        index = len(prices) - 2
        while index >= 0:
            # if you have a new max value, set it as the last (aka the day that you sell the stock)
            if prices[index] > last:
                last = prices[index]
            else:
                # Otherwise, check to see if the difference between where you're at in the array is
                # greater than the difference you're currently keeping
                currDiff = last - prices[index]
                if currDiff > maxDiff:
                    maxDiff = currDiff
            index -= 1
        
        return maxDiff
    
    """
    Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete as many transactions as you like
    (i.e., buy one and sell one share of the stock multiple times).

    Note: You may not engage in multiple transactions at the same time
    (i.e., you must sell the stock before you buy again).

    Example:
    Input: [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
                Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    """
    def maxProfitMulti(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        """
        Explanation: Building off of the last solution, you still use a similar greedy algorithm.
        The main difference is that you attempt to sell your stock as soon as the potential profit dips
        """

        if len(prices) == 0 or len(prices) == 1: return 0
        
        last = prices[len(prices) - 1]
        runningTotal = 0  # keep track of the running total for how much profit you can get
        maxDiff = 0
        
        index = len(prices) - 2
        while index >= 0:
            # Reset once you find a new max value to set as the end (aka day that you sell your stock)
            if prices[index] > last:
                runningTotal += maxDiff
                last = prices[index]
                maxDiff = 0
            else :
                currDiff = last - prices[index]
                if currDiff > maxDiff:
                    maxDiff = currDiff
                else:
                    # If the potential profit dips, sell your stock and reset
                    runningTotal += maxDiff
                    last = prices[index]
                    maxDiff = 0
            index -= 1
        # Add any remaining differences to the running total
        runningTotal += maxDiff
        
        return runningTotal
