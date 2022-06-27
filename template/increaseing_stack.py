class Solution:
    """
    @param prices: a list of integer
    @return: return the actual prices
    """
    def FinalDiscountedPrice(self, prices):
        # write your code here
        s, res = [], [prices[i] for i in range(len(prices))]

        for i in range(len(prices)):
        	while len(s) != 0 and prices[s[-1]] >= prices[i]:
        		index = s[-1]
        		s.pop()
        		res[index] = prices[index] - prices[i]
        	s.append(i);
        return res