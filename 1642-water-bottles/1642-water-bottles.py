class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        # count=0
        # while numBottles>=numExchange:
        #     a=numBottles//numExchange
        #     count+=numExchange*a
        #     numBottles=a+(numBottles%numExchange)
        # count+=numBottles
        # return count
        return  numBottles + (numBottles - 1) // (numExchange - 1) 